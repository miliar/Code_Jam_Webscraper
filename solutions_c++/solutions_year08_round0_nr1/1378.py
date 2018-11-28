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

int main()
{
    int nC = GI;
    for(int ni = 1; ni <= nC; ++ni)
    {
	int num = GI;
	char arr[110];
	getchar();
	map<string, bool> vis;
	FORZ(i,num)
	{
	    gets(arr);
	    vis[arr] = 0;
	}
	int q = GI;
	getchar();
	int cnt = num;
	int ret = 0;
	while(q--)
	{
	    gets(arr);
	    if(!vis.count(arr))
		continue;
	    if(vis[arr] == 0)
		vis[arr] = 1, cnt--;
	    if(cnt == 0)
	    {
		ret++;
		cnt = num;
		FORI(itr, vis.begin(), vis.end())
		    itr -> second = 0;
		vis[arr] = 1;
		cnt--;
	    }
	}
	printf("Case #%d: %d\n", ni,ret);
    }
}
