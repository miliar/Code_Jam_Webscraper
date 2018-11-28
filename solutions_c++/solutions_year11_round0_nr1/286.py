#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
using namespace std;
int n;
pair<int,int>a[111];
int main()
{
	freopen("C:\\Users\\daizhy\\Downloads\\A-large (2).in","r",stdin);
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			char s[5];
			scanf("%s",s);
			scanf("%d",&k);
			if (s[0]=='O')
			{
				a[i]=mp(0,k);
			}
			else 
			{
				a[i]=mp(1,k);
			}
		}
		int ans=0;
		int t=0;
		int nx=1,ny=1;
		while (1)
		{
			int x,y;
			if (t==n)break;
			if (a[t].first==0)
			{
				int nxta=a[t].second;
				int nxtb=-1;
				for (i=t+1;i<n;i++)
				{
					if (a[i].first==1)
					{
						nxtb=a[i].second;
						break;
					}
					//printf("t%d %d\n",t,nxtb);
				}
				if (nxta==nx)
				{
					++t;
				}
				if (nxta>nx)
				{
					++nx;
				}
				if (nxta<nx)
				{
					--nx;
				}
				if (nxtb!=-1)
				{
					if (nxtb>ny)
					{
						++ny;
					}
					if (nxtb<ny)
					{
						--ny;
					}
				}
				//printf("%dny=%d\n",ans,ny);
			}
			else 
			{
				int nxtb=a[t].second;
				int nxta=-1;
				for (i=t+1;i<n;i++)
				{
					if (a[i].first==0)
					{
						nxta=a[i].second;
						break;
					}
				}
				if (nxtb==ny)
				{
					++t;
				}
				if (nxtb>ny)
				{
					++ny;
				}
				if (nxtb<ny)
				{
					--ny;
				}
				if (nxta!=-1)
				{
					if (nxta>nx)
					{
						++nx;
					}
					if (nxta<nx)
					{
						--nx;
					}
				}
			}
			//printf("%d %d\n",nx,ny);
			ans++;
		}
		printf("Case #%d: %d\n",++cc,ans);
	}
	return 0;
}
