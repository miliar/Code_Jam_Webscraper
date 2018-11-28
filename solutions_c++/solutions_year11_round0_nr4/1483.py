#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int a[1005];
bool mk[1005];
int N;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	int ans=0;
	memset(mk,0,sizeof mk);
	for (int i=1;i<=N;++i)
		if (!mk[i])
		{
			int cnt=0,u=i;
			while (!mk[u])
			{
				mk[u]=true;
				u = a[u];
				++cnt;
			}
			ans += cnt==1 ? 0 : cnt;
		}
	printf("%d.000000\n",ans);
}

int main()
{
	freopen( "D-large.in" , "r" , stdin ) ;
	freopen( "D-large.out" , "w" , stdout ) ;
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	return 0;
}
