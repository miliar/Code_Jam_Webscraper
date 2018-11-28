#include <stdio.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <math.h>
#include <map>
#define MaxLength INT_MAX
#define MaxNode 1000000
using namespace std;

int N,T,C,D;
char trans[26][26];
char opp[26][26];

char result[105];
char ss[105];
int main(){
	int i,j,k,len,t,n,m,maxv,max,a,b,c,v;
	scanf("%d",&T);
	for(t=1; t<=T;t++){
		for(i=0; i<26;i++)
			for(j=0; j<26;j++)
				opp[i][j] = trans[i][j]=0;

		//puts("Trans:");

		scanf("%d",&C);
		for(i=0; i<C;i++){
			getchar();
			a=getchar();
			b=getchar();
			c=getchar();
			
			//printf("%c + %c--> %c\n",a,b,c);
			trans[b-'A'][a-'A'] = trans[a-'A'][b-'A']=c;
		}

		//puts("Opp:");

		scanf("%d",&D);
		for(i=0; i<D;i++){
			getchar();
			a=getchar();
			b=getchar();
			
			//printf("%c <> %c\n",a,b);
			opp[b-'A'][a-'A'] = opp[a-'A'][b-'A']=1;
		}
		scanf("%d ",&N);
		gets(ss);
		len=0;

		for(i=0; i<N;i++){
			result[len] = ss[i];
			while(len>0 && trans[result[len]-'A'][result[len-1]-'A']!=0){
				result[len-1] = trans[result[len]-'A'][result[len-1]-'A'];
				len--;
			}
			len++;
			for(j=0; j<len-1;j++)
				if(opp[result[len-1]-'A'][result[j]-'A']!=0)
					len=0;				
			
		}

		printf("Case #%d: [",t);
		//printList();
		if(len>0){
			printf("%c",result[0]);
			for(i=1; i<len;i++)
				printf(", %c",result[i]);
		}
		puts("]");

	}
	
	return 0;
}
