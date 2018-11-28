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
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const int MAX = 100;

int n, ans;
int a[MAX];

void process()
{
	int i, j, k;
	ans = 0;
	RP(i, n)
	{
		if (a[i] <= i) continue;
		FR(j, i+1, n-1) if (a[j] <= i)
		{
			int tmp = a[j];
			for (k=j; k>=i+1; k--) a[k] = a[k-1];
			a[i] = tmp;
			ans += j-i;
			break;
		}
	}
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	int tc, testcase, i, j;
	string str;

	cin >> tc;

	RP(testcase, tc)
	{
		cin >> n;
		RP(i, n)
		{
			cin >> str;
			a[i] = 0;
			RP(j, n) if (str[j]=='1') a[i] = j;
		}
		process();
		printf("Case #%d: %d\n", (testcase+1), ans);
	}

	return 0;
}
