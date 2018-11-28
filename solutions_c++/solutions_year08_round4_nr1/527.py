#include<stdio.h>
#include<string.h>
#define INF 1<<29

int gg(int x){
	if (x>INF) return INF;
	return x;
}

int min3(int a,int b,int c){
	if (a<b && a<c) return a;
	if (b<c) return b;
	return c;
}

int gate[50000];
bool c[50000];
int f[50000][2];

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		int n,v; scanf("%d%d",&n,&v);
		for (int i=1; i<=n; i++){
			if (i<=(n-1)/2) scanf("%d%d",&gate[i],&c[i]);
			else scanf("%d",&gate[i]);
		}
		for (int i=n; i>=1; i--){
			if (i*2>n){
				if (gate[i]==1){ f[i][1]=0; f[i][0]=INF; }
				else{ f[i][0]=0; f[i][1]=INF; }
			}else{
				int agate[2]; agate[0]=INF; agate[1]=INF;
				agate[1]=gg(f[i*2][1]+f[i*2+1][1]);
				agate[0]=min3(gg(f[i*2][0]+f[i*2+1][1]),gg(f[i*2][1]+f[i*2+1][0]),gg(f[i*2][0]+f[i*2+1][0]));

				int ogate[2]; ogate[0]=INF; ogate[1]=INF;
				ogate[0]=gg(f[i*2][0]+f[i*2+1][0]);
				ogate[1]=min3(gg(f[i*2][0]+f[i*2+1][1]),gg(f[i*2][1]+f[i*2+1][0]),gg(f[i*2][1]+f[i*2+1][1]));

				if (gate[i]==1) f[i][0]=agate[0],f[i][1]=agate[1];
				if (gate[i]==0) f[i][0]=ogate[0],f[i][1]=ogate[1];

				if (c[i]){
					if (gate[i]==0) f[i][0]<?=agate[0]+1,f[i][1]<?=agate[1]+1;
					if (gate[i]==1) f[i][0]<?=ogate[0]+1,f[i][1]<?=ogate[1]+1;
				}
			}
		}
		printf("Case #%d: ",tt);
		if (f[1][v]>INF-1) printf("IMPOSSIBLE\n");
		else
		printf("%d\n",f[1][v]);
	}
	return 0;
}
