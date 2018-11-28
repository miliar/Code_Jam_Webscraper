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
#define dbg(x) cout << #x << " : " << x << "; " << flush;
#define dbge(x) cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

int N;
int rel;
int prison[6];
int vis[101];

int find(int u)
{
    int ret = 0;
    int i;
    for(i = u+1; i <= N ; i++)
	if(vis[i] == true)
	    break;
    ret += i - u - 1;
    for(i = u - 1 ; i > 0 ; i--)
	if(vis[i] == true)
	    break;
    ret += u - i - 1;
    return ret;
}

int cal()
{
    int ret = 0;
    FORZ(i, rel)
    {
	vis[prison[i]] = true;
	ret += find(prison[i]);
    }
    return ret;
}

int main()
{
    int t = GI;
    FORZ(test, t)
    {
	N = GI;
	rel = GI;
	FORZ(i, rel)
	    prison[i] = GI;
	int ans = INT_MAX;
	do {
	    memset(vis, false, sizeof vis);
	    ans = min(ans, cal());
	}while(next_permutation(prison, prison + rel));
	printf("Case #%d: %d\n", test+1, ans);
    }
    return 0;
}

