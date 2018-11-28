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

int R, k, N;
int g[1000];
int last[1000];
LL earn[1000];

int go(int &cur)
{
    LL tot = g[cur];
    int i = (cur+1) % N;
    while (i != cur && tot + g[i] <= k) { tot += g[i]; i = (i+1)%N; }
    cur = i;
    return tot;
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
        LL ans = 0;
        int i;

        cin >> R >> k >> N;
        for (i=0; i<N; i++) cin >> g[i];
        memset(last, -1, sizeof(last));
        memset(earn, -1, sizeof(earn));

        int cur = 0;
        last[cur] = 0;
        earn[cur] = 0;
        for (i=1; i<=R; i++)
        {
            ans += go(cur);
            if (last[cur] == -1)
            {
                last[cur] = i;
                earn[cur] = ans;
                continue;
            }
            int dif = i - last[cur];
            LL x = ans - earn[cur];
            int left = R - i;
            int lap = left / dif;
            ans += x * lap;
            i = (i + lap * dif + 1);
            break;
        }
        for (j=i; j<=R; j++)
            ans += go(cur);

		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
