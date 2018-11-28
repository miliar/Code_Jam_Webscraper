#include <stdio.h>

static int park(int r, int k, int n, int* g);
static int park_(int r, int k, int n, int* g,int s);

int main(){

	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int r,k,n;
		scanf("%d %d %d\n",&r,&k,&n);
		int g[n];
		for(int j=0;j<n;j++)
			scanf("%d",&g[j]);
		printf("Case #%d: %d\n",i+1,park(r,k,n,g));
	}

	return 1;
}
static int park(int r, int k, int n, int* g){
	return park_(r,k,n,g,0);
}
static int park_(int r, int k, int n, int* g,int s){
	if(r==0 || k==0 || n==0) return 0;

	long res = 0;
	int c=k;

	int i;
	for(i=0;i<n && g[(s+i)%n]<=c;i++){
		res += g[(s+i)%n];
		c -= g[(s+i)%n];
	}

	return res+park_(r-1,k,n,g,s+i);
}
