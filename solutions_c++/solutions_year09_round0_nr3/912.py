#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <iostream>
typedef long long LL;
using namespace std;

const int N=501;

char str[]="welcome to code jam";
char A[N];
int D[N][20];

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ic,cas;
	scanf("%d",&cas);
	int i,j,n;
	ic=1;
	while(ic<=cas){
	//for(ic=1;ic<=cas;ic++){
		gets(A);
		if(strlen(A)==0) continue;
		n=strlen(A);
		for(i=0;i<n;i++) D[i][0]=1;
    	for(i=0;i<n;i++){
			for(j=1;j<20;j++){
				if(A[i]==str[j-1]) D[i+1][j]=(D[i][j]+D[i][j-1])%10000;
				else D[i+1][j]=D[i][j];
				//printf("%d\t",D[i][j]);
			}
			//printf("\n");
		}
		printf("Case #%d: %04d\n",ic,D[i][19]);
		ic++;
	}
	return 0;
}
