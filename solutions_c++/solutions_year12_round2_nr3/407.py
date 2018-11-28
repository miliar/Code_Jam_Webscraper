#include<cstdio>

int n;
int A[600];
int from[3000000][2];

void pr(int k)
{
	if( k == 0 ) return;
	printf(" %d",from[k][0]);
	pr(k-from[k][0]);
}

void f()
{
	for(int c=0;c<3000000;c++) from[c][0] = from[c][1] = -1;
	scanf("%d",&n);
	for(int c=1;c<=n;c++) scanf("%d",&A[c]);
	from[0][0] = 0;
	for(int i=1;i<=n;i++) for(int c=2000000;c>=0;c--) if( from[c][0] != -1 )
	{
		if( from[c+A[i]][0] == -1 ) from[c+A[i]][0] = A[i];
		else if( from[c+A[i]][1] == -1 ) from[c+A[i]][1] = A[i];
	}
	for(int c=1;c<=2000000;c++) if( from[c][1] != -1 )
	{
		printf("%d",from[c][0]); pr(c-from[c][0]); printf("\n");
		printf("%d",from[c][1]); pr(c-from[c][1]); printf("\n");
		return;
	}
	printf("Impossible\n");
}

int main()
{
	freopen("3.in","r",stdin);
	freopen("3.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d:\n",c);
		f();
	}
}
