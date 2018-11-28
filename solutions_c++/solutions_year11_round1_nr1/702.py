#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <string>

//#include <iostream>

using namespace std;

#define REP(i,v)for(int i=0;i<(v);++i)
#define FOR(i,x,v)for(int i=x;i<=(v);++i)
#define FORD(i,x,v)for(int i=x;i>=(v);--i)
#define VAR(v,n) __typeof(n) v = (n)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define ALL(c) (c).begin(), c.end()
#define PB push_back
#define SZ size
#define MP make_pair
#define FI first
#define SE second
#define CL clear()
#define RS resize
#define INFTY 1000000001
#define EPS 10e-9
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef pair<int,int> PII;
typedef long long LL;
typedef vector<string> VS;

void show(PII p)
{printf("(%d %d)\n",p.FI,p.SE);}

void show(VI e)
{REP(i,SIZE(e)) printf("%d ",e[i]); printf("\n");}

void show(vector<PII> e)
{REP(i,SIZE(e)) printf("(%d %d) ",e[i].FI,e[i].SE); printf("\n");}

void show(VS e)
{REP(i,SIZE(e)) printf("%s\n",e[i].c_str());}

void show(VVI e)
{REP(i,SIZE(e)) show(e[i]);}

int t; 
double pd, pg;
LL n;

int main()
{
	bool kon;

	scanf("%d", &t);

	REP(i,t)
	{
		kon = false;
		printf("Case #%d: ", i+1);
		scanf("%lld%lf%lf", &n, &pd, &pg);
		if(((int) pg == 100 && (int) pd != 100) || ( pg == 0 && pd != 0))
			printf("Broken\n");
		else if(((int) pg == 100 && (int) pd == 100) || (pd == 0 && pg == 0))
			printf("Possible\n");
		else
		{
			REP(j,min(n,(LL) 100))
			{
				if(ceil(pd*(j+1)/100) == floor(pd*(j+1)/100))
				{
					kon = true;
					break;
				}
			}
			if(kon == true || n > 100)
			{		
				printf("Possible\n");
			}
			else
			{
				printf("Broken\n");
			}
		}

	}
	return 0;
}

