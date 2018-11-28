#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define dbg(x) cout << #x << " -> " << x << "\t" << flush;
#define dbge(x) cout << #x << " -> " << x << "\t" << endl;
#define LET(x,a) typeof(a) x(a)
#define FORI(i,a,b) for(LET(i,a);i!=(b);++i)
#define FOR(i,a,b) for(LET(i,a);i < (b);++i)
#define FORZ(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define CS c_str()
#define PB push_back
#define SZ size()
#define INF (int)1e9+1
char arr[2001][2001];
int N, M;
bool sat[2001];
int res[2001];
bool vis[2001][3];
typedef pair<int, bool> PII;
int main()
{
    int nC = GI;
    for(int nc = 1; nc <= nC; ++nc)
    {
	N = GI;
	M = GI;
	vector<PII> arr[M];
	FORZ(i,M)
	{
	    int T = GI;
	    while(T--)
	    {
		int a = GI;
		int b = GI;
		a--;
		arr[i].PB(PII(a,b));
	    }
	}
	int x = 1 << N;
	bool good = 0;
	printf("Case #%d:",nc);
	FORZ(as,x)
	{
	    int f = 1;
	    FORZ(j,M)
	    {
		bool f1 = 0;
		FORZ(i,arr[j].SZ)
		{
		    bool val = as &(1 << arr[j][i].first);
		    if(val == arr[j][i].second)
		    {
			f1 = 1;
			break;
		    }
		}
		if(f1 == 0)
		{
		    f = 0;
		    break;
		}

	    }
	    if(f)
	    {
		good = 1;
		FORZ(i,N)
		{
		    int val = as & (1 << i);
		    printf(" %d",!!val);
		}
		break;
	    }

	}
	if(!good)
	    printf(" IMPOSSIBLE");
	printf("\n");
    }
}
