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

int L, P, C;

int calc(int be, int en)
{
    if ((LL)be * C >= en) return 0;
    double k2 = (double)en / be;
    double k = sqrt(k2);
    int mi = (int)(be * k);
    
    int res1 = INF;
    if (mi<en && mi>be)
        res1 = 1 + max( calc(be, mi), calc(mi, en) );

    int res2 = INF;
    if (mi-1<en && mi-1>be)
        res2 = 1 + max( calc(be, mi-1), calc(mi-1, en) );

    int res3 = INF;
    if (mi+1<en && mi+1>be)
        res3 = 1 + max( calc(be, mi+1), calc(mi+1, en) );

    return min(res1, min(res2, res3));
}

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
        cin >> L >> P >> C;
        int ans = calc(L, P);
        cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
