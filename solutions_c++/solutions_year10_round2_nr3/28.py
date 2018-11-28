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

const int MOD = 100003;
const int MAX = 600;

LL C[MAX][MAX];
LL cache[MAX][MAX];
int n;
LL ans;

void initC()
{
    memset(C, 0, sizeof(C));
    C[0][0] = 1;
    int i, j;
    for (i=1; i<MAX; i++)
    {
        C[i][0] = 1;
        for (j=1; j<MAX; j++) C[i][j]=(C[i-1][j-1] + C[i-1][j]) % MOD;
    }
}

LL calc(int last, int leng)
{
    LL &res = cache[last][leng];
    if (res>=0) return res;
    if (leng==1) return res=1;
    int between = last - leng - 1;
    res = 0;
    int ind;
    for (ind=1; ind<=leng-1; ind++)
        if (leng-1-ind <= between)
        {
            res += calc(leng, ind) * C[between][leng-1-ind];
            res %= MOD;
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
    int i;
	cin >> numtest;

    initC();
    memset(cache, -1, sizeof(cache));

	for (test=1; test<=numtest; test++)
	{
        cin >> n;
        ans = 0;
        for (i=1; i<=n; i++)
        {
            ans += calc(n, i);
            ans %= MOD;
        }
		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
