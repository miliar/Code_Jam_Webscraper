#include<cstdio>

bool Z;
int n;
int A[2010];
int ans[2010];

void gen(int f,int l,int sl)
{
	int pp = f, qq;
	while( pp != l )
	{
		qq = A[pp];
		ans[pp] = ans[l] - sl*( l - pp );
		ans[qq] = ans[l] - sl*( l - qq );
		gen( pp+1 , qq , sl+1 );
		pp = qq;
	}
}

bool prog()
{
	for(int c=0;c<2010;c++) A[c] = ans[c] = -1;
	scanf("%d",&n);
	for(int c=1;c<n;c++) scanf("%d",&A[c]);

	/// TEST
	for(int c=1;c<n;c++)
	{
		int next = A[c];
		for(int d=c+1;d<next;d++) if( A[d] > next ) return false;
		//printf("%d OK\n",c);
	}
	///

	int pp = 1, qq;
	while( pp != n )
	{
		qq = A[pp];
		ans[pp] = ans[qq] = 1000000000;
		gen( pp+1 , qq , 1 );
		pp = qq;
	}

	return true;
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("sol1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		Z = true;
		if( prog() ) for(int d=1;d<=n;d++) printf("%d ",ans[d]);
		else printf("Impossible");
		printf("\n");
	}
}
