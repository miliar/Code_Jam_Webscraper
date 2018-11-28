#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
 
using namespace std;

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<int, int> pii;
#define LL long long

LL INF;
int P;
int num[1<<12];
LL cache[1<<12][14];

LL calc(int root, int bought)
{
    LL &res = cache[root][bought];
    if (res>=0) return res;
    if (root>=(1<<P)-1)
    {
        res = 0;
        if (P-bought>num[root]) res=INF;
        return res;
    }
    LL left, right;

    // buy here
    left = calc(root*2+1, bought+1);
    right = calc(root*2+2, bought+1);
    res = left+right+num[root];

    // dont buy
    left = calc(root*2+1, bought);
    right = calc(root*2+2, bought);
    res = min(res, left+right);

    return res;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0a.out", "w", stdout);

    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int numtest, test, i;
	cin >> numtest;

    INF = 20000000;
    INF *= INF;

	for (test=1; test<=numtest; test++)
	{
        cin >> P;
        for (i=(1<<(P+1))-2; i>=0; i--) cin >> num[i];
        memset(cache, -1, sizeof(cache));
        LL ans = calc(0, 0);
        cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
