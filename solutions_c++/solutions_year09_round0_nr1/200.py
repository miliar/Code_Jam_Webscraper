#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
int w[5000][15];
char t[10000];
int main(){
	int i,N,L,D,d,n,l,k,c,j,p;
	char s[20];
	int v[15];
	scanf("%d%d%d\n",&L,&D,&N);
	for (d=0;d<D;d++){
		scanf("%s",s);
		for (i=0;i<L;i++){
			w[d][i]=1<<(s[i]-'a');
		}
	}
	for (n=1;n<=N;n++){
		scanf("%s",t);
		for (p=0,j=0;t[p]&&j<L;j++){
			if (t[p]=='('){
				p++;
				v[j]=0;
				while(t[p]&&t[p]!=')')
				{
					v[j]|=1<<(t[p]-'a');
					p++;
				}
				if (t[p]==')') p++;
			}
			else{
				v[j]=1<<(t[p]-'a');
				p++;
			}
		}
		if (j!=L){
			printf("Case #%d: 0\n",n);
		}
		else{
			c=0;
			for (d=0;d<D;d++){
				for (j=0;j<L;j++)
				if (!(v[j]&w[d][j])) break;
				if (j==L) c++;
			}
			printf("Case #%d: %d\n",n,c);
		}
	}
	return 0;
}
