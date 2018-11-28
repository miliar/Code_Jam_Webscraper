#include<iostream>
#include<cmath>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<cstdlib>
#include<stack>
#include<list>
#include<deque>
#include<queue>
using namespace std;

typedef long long LL;

#define EPS (1e-8)
#define INF 0x7fffffff
#define SZ(p) ((p).size())

int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);

	int T,CS;
	scanf("%d",&T);
	for(CS=1;CS<=T;CS++)
	{
		int n,i,j,k,l;
		char mp[50][50];
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",mp[i]);
		int ans=0;
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				for(k=i+1;k<n;k++)
				{
					if(mp[j][k]=='1')
						break;
				}
				if(k==n)
					break;
			}
			for(k=j;k>i;k--)
			{
				for(l=0;l<n;l++)
					swap(mp[k][l],mp[k-1][l]);
				ans++;
			}
		}
		printf("Case #%d: ",CS);
		fflush(stdout);

		printf("%d\n",ans);
	}
}