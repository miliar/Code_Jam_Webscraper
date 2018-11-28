#include<stdio.h>
#include<string.h>
#include<algorithm>
#define M 110
using namespace std;

int n, k;
struct Node{
	int num[30];
}gg[111];

int g[111][111];
int mat[M],tmat[M];
int m;
int hungry_aug(int i) {
	int v,j;
	for (j = 0 ; j < m; j++)
		if ( g[i][j] && tmat[j]==0) {
			tmat[j]=1;v=mat[j];mat[j]=i;
			if (v==-1 || hungry_aug(v)) return 1;
			mat[j]=v;
		}
		return 0;
}
int hungry() {
	int i,k=0;
	memset(mat,-1,sizeof(mat));
	for (i = 0; i < n; i++) {
		memset(tmat,0,sizeof(tmat));
		k+=hungry_aug(i);
	}
	return k;
}
bool dayu(Node a, Node b);
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int kk=1; kk<=T; kk++){
		scanf("%d%d", &n, &k);
		m=n;
		memset(g, 0, sizeof(g));
		for(int i=0; i<n; i++){
			for(int j=0; j<k; j++){
				scanf("%d", &gg[i].num[j]);
			}
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(dayu(gg[i], gg[j])) g[i][j]=1;
			}
		}
		printf("Case #%d: %d\n", kk, n-hungry());
	}
	return 0;
}


bool dayu(Node a, Node b)
{
	bool flag=true;
	for(int i=0; i<k; i++){
		if(a.num[i]<=b.num[i]) flag=false;
	}
	return flag;
}