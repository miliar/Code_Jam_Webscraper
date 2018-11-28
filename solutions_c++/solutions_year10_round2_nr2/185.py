#include <iostream>
#include <string>
#include <cstring>
#include <map>

using namespace std;
int X[64],a[64];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,t,N,K,B,CT,cd,V,c,r,i,j;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		scanf("%d%d%d%d",&N,&K,&B,&CT);
		for (i = 0;i < N;i++)
			scanf("%d",&X[i]);
		c = 0;
		for (i = 0;i < N;i++){
			scanf("%d",&V);
			cd = (B-X[i]-1) / V+1;
			if (cd <= CT)
				a[c++] = i;
		}
		printf("Case #%d: ",t);
		if (c < K) puts("IMPOSSIBLE");
		else{
			r = 0;
			for (i = c-1,j = 0;j < K;i--,j++)
				r += N-a[i]-1-j;
			printf("%d\n",r);
		}
	}
	fclose(stdout);
}
