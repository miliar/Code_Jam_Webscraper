#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <bitset>
#include <sstream>
#include <cmath>
#include <ctime>

#define WR printf
#define RE scanf
#define FOR(i,Be,En) for(i=(Be);i<=(En);++i)
#define DFOR(i,Be,En) for(i=(Be);i>=(En);--i)
#define PB push_back
#define SZ(a) (int)((a).size())
#define FIT(i,v) for(i=(v).begin();i!=(v).end();i++)
#define RFIT(i,v) for(i=(v).rbegin();i!=(v).rend();i++)
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define SE second
#define FI first
#define CLR(a) memset(a,0,sizeof(a))
#define LL long long
using namespace std;
typedef vector<int> VI;
typedef vector<string>VS;

int T;

int col[2000];

bool flag[2000];

void init()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	RE("%d",&T);
	
}
bool prime(int a)
{
	int i = 2;
	while (i*i<=a)
	{
		if (a % i ==0) return false;
		i++;
	}
	return true;
}

int main()
{
	init();
	int i ,j, t;
	int a, b, p;
	FOR(t,1,T)
	{
		RE("%d %d %d",&a,&b,&p);
		CLR(col);
		FOR(i,p,b) if (prime(i))
		{
			CLR(flag);
			FOR(j,a,b) if (j%i==0)
			{
				if (col[j]) flag[col[j]] = true;
				col[j] = i;
			}
			FOR(j,a,b) if (flag[col[j]]) col[j] = i;
		}
		CLR(flag);
		int ans = 0;
		//FOR(j,a,b) WR("col[%d]=%d\n",j,col[j]);
		FOR(j,a,b) if (!col[j]) ans++;
		else if (!flag[col[j]])
		{	
			flag[col[j]] = true;
			ans++;
		}
		WR("Case #%d: %d",t,ans);
		if (t<T) WR("\n");
	}
	return 0;
}