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

int N, K, B, T;
LL org[55];
LL v[55];
bool good[55];

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);

    //freopen("B-small-attempt1.in", "r", stdin);
    //freopen("B-small-attempt1a.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int numtest, test;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> N >> K >> B >> T;
        int i, j;
        for (i=0; i<N; i++) cin >> org[i];
        for (i=0; i<N; i++) cin >> v[i];
        int ans = 0;
        int reach = 0;
        memset(good, false, sizeof(good));
        for (i=N-1; i>=0; i--)
        {
            int canReach = org[i] + v[i]*T;
            if (canReach < B)
            {
                good[i] = false;
                continue;
            }
            good[i] = true;
            for (j=i+1; j<N; j++) if (!good[j]) ans++;
            reach++;
            if (reach==K) break;
        }
        if (reach < K)
		    cout << "Case #" << (test) << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
