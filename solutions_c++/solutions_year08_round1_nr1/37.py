#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long int64;


const int maxn=1000+5;

int n,m;
int64 l1[maxn],l2[maxn];
int p1[maxn],p2[maxn];
int64 G[maxn][maxn];
bool v1[maxn],v2[maxn];

bool find(int v)
{
	v1[v]=true;
	for (int i=1;i<=n;i++)
		if (!v2[i] && G[v][i]==l1[v]+l2[i])
		{
			v2[i]=true;
			if (p2[i]==0 || find(p2[i]))
			{
				p1[v]=i;
				p2[i]=v;
				return true;
			}
		}
	return false;
}
int64 solve()
{
	int i,j,u,v;
	for (i=1;i<=n;i++)
		l2[i]=0;
	for (i=1;i<=n;i++)
	{
		l1[i]=0;
		for (j=1;j<=n;j++)
			if (G[i][j]>l1[i])
				l1[i]=G[i][j];
	}
	memset(p1,0,sizeof(p1));
	memset(p2,0,sizeof(p2));
	for (i=1;i<=n;i++)
		while (1)
		{
			memset(v1,false,sizeof(v1));
			memset(v2,false,sizeof(v2));
			if (find(i))
				break;
			int64 m=10000000LL*10000000LL;
			for (u=1;u<=n;u++) if (v1[u])
				for (v=1;v<=n;v++)
					if (!v2[v] && l1[u]+l2[v]-G[u][v]<m)
						m=l1[u]+l2[v]-G[u][v];
			for (u=1;u<=n;u++)
				if (v1[u])
					l1[u]-=m;
			for (v=1;v<=n;v++)
				if (v2[v])
					l2[v]+=m;
		}
	int64 result=0;
	for (i=1;i<=n;i++)
		result+=G[i][p1[i]];
	return result;
}

int main()
{
	freopen("..\\input.txt","r",stdin);
//	freopen("..\\input.txt","r",stdin);
//	freopen("..\\output.txt","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d",&n);
		int A[maxn],B[maxn];
		for (int i=1;i<=n;i++) scanf("%d",&A[i]);
		for (int i=1;i<=n;i++) scanf("%d",&B[i]);
		cout<<"Case #"<<caseId<<": ";
		int64 W=1000000LL*1000000LL;
		for (int i=1;i<=n;i++) for (int j=1;j<=n;j++)
			G[i][j]=W-(int64)A[i]*(int64)B[j];
		int64 result=solve();
		result=W*n-result;
		cout<<result<<endl;
	}
	return 0;
}

