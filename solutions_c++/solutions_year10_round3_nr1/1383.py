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

inline bool intersect(int y1, int y2, int y3, int y4)
{
    bool ret = false;

    if(y3 - y1 != y4 - y2)
        if((y3 > y1 && y4 < y2) || (y1 > y3 && y2 < y4))
            ret = true;

    return ret;
}

int main()
{
	int cases = 0;
	cin >> cases;
	forn(i, cases)
	{
        long long ret = 0;
		int N;
		cin >> N;

        vector <int> a, b;

        forn(j, N)
        {
            int tmp_a, tmp_b;
            cin >> tmp_a >> tmp_b;

            a.PB(tmp_a);
            b.PB(tmp_b);
        }

        forv(j, a)
            for(int k=j+1; k<b.sz; k++)
            {
                if(intersect(a[j], b[j], a[k], b[k]))
                    ret++;
            }

        printf("Case #%d: %lld\n", i+1, ret);
	}
	return 0;
}
