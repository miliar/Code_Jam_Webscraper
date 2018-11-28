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
#define INF 1000000

int a[21];

int silly_sum(int x, int y)
{
    int i, res = 0;
    for (i=0; i<=21; i++)
    {
        int k = 0;
        if (x & (1<<i)) k++;
        if (y & (1<<i)) k++;
        if (k == 1) res += (1<<i);
    }
    return res;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int numtest, test;
    int i, j;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        int ans = 0;
        int i, N, mi;

        cin >> N;
        mi = 1000000;
        for (i=0; i<N; i++)
        {
            cin >> a[i];
            mi = min(mi, a[i]);
        }
        
        int silly_total = 0, total = 0;
        for (i=0; i<N; i++)
        {
            total += a[i];
            silly_total = silly_sum(silly_total, a[i]);
        }

        ans = total - mi;

        if (silly_total > 0) cout << "Case #" << (test) << ": " << "NO" << endl;
        else
        {
		    cout << "Case #" << (test) << ": " << ans << endl;
        }
	}
	return 0;
}
