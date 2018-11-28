// includes {{{
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
// }}}
// defines {{{
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define all(c) (c).begin(),(c).end()
#define foreach(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
// }}}

int A, B;
int num_cycles;
int cnt;

void cnt_digits(int i)
{
    while (i > 0) {
        i /= 10;
        ++num_cycles;
    }
}

int calc_next(int i)
{
    while (i % 10 == 0)
        i /= 10;

    int move = i % 10;
    i /= 10;

    i += move * pow(10, num_cycles - 1);
    return i;
}

void count_cycle_bigger(int i)
{
    int next = i;
    for (int j = 0; j < num_cycles - 1; ++j) {
        next = calc_next(next);
        if (next == i)
            break;
        //cout << i << ' ' << next << endl;
        if (next > i && next <= B)
            ++cnt;
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int cases;
    cin >> cases;
    for (int c = 1; c <= cases; ++c) {
        cin >> A >> B;

        num_cycles = 0;
        cnt_digits(A);

        cnt = 0;
        for (int i = A; i <= B; ++i)
            count_cycle_bigger(i);

        cout << "Case #" << c << ": " << cnt << endl;
    }

    return 0;
}
