#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)
#define FORE(i, a, b) for(typeof(a) i = a ; i <= b ; i++)
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define dbg(x) /*cout << #x << " : " << x << "; " << flush;*/
#define dbge(x) /*cout << #x << " : " << x << ";" << endl;*/
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

int main()
{
    int t = GI;
    FORZ(test, t)
    {
	string giv;
	cin >> giv;
	string t = giv;
	sort(all(t));
	t.erase(unique(all(t)), t.end());
	int base = t.SZ;
	int val[255];
	memset(val, -1, sizeof val);
	val[giv[0]] = 1;
	int i = 1;
	while(i < giv.SZ && giv[i] == giv[0])
	{
	    i++;
	}
	if(i < giv.SZ) 
	    val[giv[i]] = 0;
	else
	{
	    printf("Case #%d: %d\n", test+1, (1LL << giv.SZ)-1);
	    continue;
	}
	dbg(i);dbge(giv[i]);
	int c = 2;
	FORZ(i, giv.SZ)
	    if(val[giv[i]] == -1)
		val[giv[i]] = c++;
	dbge(base);
//	FORZ(i, t.SZ)
//	    cout << t[i] << " " << val[t[i]] << endl;
	LL ans = 0;
	LL b = 1;
	for(int i = giv.SZ - 1; i >= 0 ; i--)
	{
	    ans += val[giv[i]] * b;
	    b *= base;
	}
	cout << "Case #"<<test+1<<": "<<ans<<endl;
    }
    return 0;
}
