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

char R[105];
int B[105];
int SB[105];
int SO[105];
int N,T;

int main(){
	int i,j,k,l,t,n,m,maxv,max,a,b,c,v,result;
	int po, pb;
	char ss[10005];
	scanf("%d",&T);
	for(t=1; t<=T;t++){
		scanf("%d",&N);
		int so=0, sb=0;
		for(i=0; i<N;i++){
			scanf(" %c %d",&R[i], &B[i]);
			if(R[i]=='O')
				SO[so++]=B[i];
			else
				SB[sb++]=B[i];
		}
		SO[so]=-1;
		SB[sb]=-1;
		po=1, pb=1, result=0,sb=0, so=0;
		i=0;
		bool push = false;
		while(SO[so]!=-1 || SB[sb]!=-1){

			if(push == false && R[i] == 'O' && po==B[i]){
				i++;so++;
				push=true;
				//printf("Push O ");
			}else if(SO[so] != -1){
				//printf("O %d --> ",po);
				if(SO[so] > po)
					po++;
				else if(SO[so] < po)
					po--;
				//printf("%d, ",po); 
			}
			
			
			if(push == false && R[i] == 'B' && pb==B[i]){
				i++;sb++;
				push=true;
				//printf("Push B ");
			}else if(SB[sb] != -1 && SB[sb]!=pb){
				//printf("B %d --> ",pb);
				if(SB[sb] > pb)
					pb++;
				else pb--;
				//printf("%d",pb); 
			}
			//puts("");
			result++;
			if(push)
				push=false;
		}
		printf("Case #%d: %d\n",t,result);

	}
	
	return 0;
}
