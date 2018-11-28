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

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

int main()
{
	int cases = 0;
	cin >> cases;
	forn(i, cases)
	{
		int N, K;
		cin >> N >> K;
        bool on = true;
        forn(j, N)
        {
            on = (K & 1) && on;
            if(!on)
                break;
            K >>= 1;
        }
        if(on)
            printf("Case #%d: ON\n", i+1);
        else
            printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}
