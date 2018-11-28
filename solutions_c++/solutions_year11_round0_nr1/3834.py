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

vi colors, buttons;

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numtest, test;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        colors.clear();
        buttons.clear();
        char r;
        int i, n, p;
        cin >> n;
        for (i=0; i<n; i++)
        {
            cin >> r >> p;
            if (r == 'O') colors.pb(1); else colors.pb(2);
            buttons.pb(p);
        }
        int b1, b2;
        int t1, t2;
        int ans = 0;
        b1 = 1;
        b2 = 1;
        t1 = 0;
        t2 = 0;
        for (i=0; i<n; i++)
        {
            if (colors[i] == 1)
            {
                ans = max(ans, abs(buttons[i]-b1) + t1 + 1);
                if (ans < t2 + 1) ans = t2 + 1;
                t1 = ans;
                b1 = buttons[i];
            }
            else
            {
                ans = max(ans, abs(buttons[i]-b2) + t2 + 1);
                if (ans < t1 + 1) ans = t1 + 1;
                t2 = ans;
                b2 = buttons[i];
            }
            //cout << i << " - " << t1 << " " << b1 << " - " << t2 << " " << b2 << endl;
        }
		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
