#include <iostream>
#include <cstring>
#include <vector>
#include <cstdio>
#include <memory>
#include <string>
using namespace std;
#define N 1100

int m[N];
int pr[11][N];
int flag[N][N];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	scanf("%d",&t);
	for ( int c = 1 ; c <= t; c++ )
	{
		int p;
		int n;
		memset(m,0,sizeof(m));
		memset(m,0,sizeof(pr));
		memset(flag,0,sizeof(flag));
		scanf("%d",&p);
		n = 1<<p;
		for ( int i = 0 ; i < n ; i++ )
			scanf("%d",&m[i]);
		int tem=n;
		for ( int i = 0 ; i < p ; i++ )
		{
			tem = tem>>1;
			for ( int j = 0 ; j < tem ; j++ )
				scanf("%d",&pr[i][j]);
		}
		for ( int i = 0 ; i < n ; i++ )
		{
			int r = m[i];
			int k = i;
			for ( int j = 0 ; j < p ; j++ )
			{
				k = k>>1;
				if ( j<r )
					continue;
				flag[j][k] = 1;
			}
		}
		tem = n;
		int cnt=0;
		for ( int i = 0 ; i < p ; i++ )
		{
			tem = tem>>1;
			for ( int j = 0 ; j < tem ; j++ )
			{
//				printf("%d ",flag[i][j]);
				if ( flag[i][j] )
					cnt++;
			}
//			printf("\n");
		}
		printf("Case #%d: %d\n",c,cnt);
	}
}