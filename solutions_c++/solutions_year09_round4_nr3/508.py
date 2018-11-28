#include<iostream>
#include<string.h>
#define MAXN 120
using namespace std;

int n,m;

int data[120][30];
int g[120][120];
int ans=0;
int res[10000000];
void clique(int n, int* u, int mat[][MAXN], int size, int& max, int& bb, int* res, int* rr, int* c) {
	int i, j, vn, v[MAXN];
	if (n) {
		if (size + c[u[0]] <= max) return;
		for (i = 0; i < n + size - max && i < n; ++ i) {
			for (j = i + 1, vn = 0; j < n; ++ j)
				if (mat[u[i]][u[j]])
					v[vn ++] = u[j];
			rr[size] = u[i];
			clique(vn, v, mat, size + 1, max, bb, res, rr, c);
			if (bb) return;
		}
	} else if (size > max) {
		max = size;
		for (i = 0; i < size; ++ i)
			res[i] = rr[i];
		bb = 1;
	}
}

int maxclique(int n, int mat[][MAXN], int *ret) {
	int max = 0, bb, c[MAXN], i, j;
	int vn, v[MAXN], rr[MAXN];
	for (c[i = n - 1] = 0; i >= 0; -- i) {
		for (vn = 0, j = i + 1; j < n; ++ j)
			if (mat[i][j])
				v[vn ++] = j;
		bb = 0;
		rr[0] = i;
		clique(vn, v, mat, 1, max, bb, ret, rr, c);
		c[i] = max;
	}
	return max;
}

int main()
{
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			for(int j=0;j<m;++j)
				scanf("%d",&data[i][j]);
		memset(g,0,sizeof(g));
		for(int i=0;i<n;++i)
		{
			for(int j=0;j<n;++j)
			{
				for(int k=0;k+1<m;++k)
				{
					if(data[i][k]-data[j][k]<=0
					&&data[i][k+1]-data[j][k+1]>=0
					||
					data[i][k]-data[j][k]>=0
					&&data[i][k+1]-data[j][k+1]<=0)
						g[i][j]=1;
				}
			}
		}
		for(int i=0;i<n;++i)
			g[i][i]=0;
		ans=maxclique(n,g,&res[0]);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
