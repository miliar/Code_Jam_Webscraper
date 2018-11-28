#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn = 505;

int a[maxn][maxn];
int b[maxn][maxn];
int deg[maxn];
int n;
int ans;


bool same( int x,int y )
{
	return x<0 || y<0 || x==y;
}
bool good( int size )
{
	for(int i=1;i<=size;i++)
	for(int j=1;j<=min(i,2*size-i);j++)
	{
		//put here
		bool flag = true;
		int ru,rv;
		for(int u=1;u<=2*n-1 && flag;u++)
		for(int v=1;v<=min(u,2*n-u);v++)
		{
			ru = u+i-1;
			if( u<=n ) rv = v+j-1;else
				rv = v + j-1 + (u-n);
			if( ru > size ) rv -= (ru-size);
			if( ru > 2*size-1 || rv > min(ru,2*size-ru) || rv<1 )
			{
				flag = false;
				break;
			}
		}

		if(flag)
		{
			for(int u=1;u<=2*size-1;u++)
			for(int v=1;v<=min(u,2*size-u);v++)
				b[u][v] = -1;
		
			
			for(int u=1;u<=2*n-1 && flag;u++)
			for(int v=1;v<=min(u,2*n-u);v++)
			{
				ru = u+i-1;
				if( u<=n ) rv = v+j-1;else
					rv = v + j-1 + (u-n);
				if( ru > size ) rv -= (ru-size);
				b[ru][rv] = a[u][v];
			}

			for(int u=1;u<=2*size-1 && flag;u++)
			for(int v=1;v<=min(u,2*size-u);v++)
			if( !same(b[u][v],b[2*size-u][v]) || !same(b[u][v],b[u][ min(u,2*size-u)+1-v ]) )
			{
				flag = false;break;
			}
			if(flag) return true;
		}
	}
	return false;
}
int main()
{
	int TT;
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++)
	{
		printf("Case #%d: ",T);
		scanf("%d",&n);
		for(int i=1;i<=2*n-1;i++)
		{
			deg[i] = min(i,2*n-i);
			for(int j=1;j<=deg[i];j++) scanf("%d",a[i]+j);
		}

		int ans = n;
		while( !good(ans) ) ans++;
		printf("%d\n",ans*ans-n*n);
		fflush(stdout);
	}
	return 0;
}
