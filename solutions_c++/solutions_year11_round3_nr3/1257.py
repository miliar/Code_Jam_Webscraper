#include <cstdio>
#include <cmath>
#include <iostream>
#include <string.h>		// For memset function
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <bitset>
#include <sstream>
#include <map>



using namespace std;

#define FOR( i, L, U ) for(int i=(int)L ; i<=(int)U ; i++ )

typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

VI others;

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int TC, tc;
    int N, H, L;
    int ans;
    bool is;
    cin >> TC;

    FOR(tc, 1, TC) {
        cin >> N >> L >> H;

        others = VI(N);

        FOR(i, 0, N-1)
            cin >> others[i];

        FOR(i, L, H) {

            is = true;
            FOR(j, 0, N-1) {
                if(i > others[j] && i % others[j] != 0) {
                    is = false;
                    break;
                }
                else if(others[j] > i && others[j] % i != 0) {
                    is = false;
                    break;
                }
            }

            if(is) {
                ans = i;
                break;
            }
        }

        cout << "Case #" << tc << ": ";
        if(is)
            cout << ans << "\n";
        else cout << "NO\n";


    }

	return 0;
}
