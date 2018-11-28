#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cassert>
#include <memory.h>

using namespace std;

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <memory.h>
#include <cassert>

using namespace std;

#define fo(a,b,c) for (a = (b); a < (c); a++)
#define fr(a,b) fo(a, 0, (b))
#define fi(n) fr(i, (n))
#define fj(n) fr(j, (n))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define _(a,b) memset((a), (b), sizeof(a))
#define __(a) memset((a), 0, sizeof(a))
#define sz(a) (int)(a).size()
#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1 << 20;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("c-large.txt", "w", stdout);
}

void panic()
{
	cout << "PANIC!" << endl;
	assert(false);
}

long long a[555][555];
int n;

void solve(int test_num)
{
	printf("Case #%d: ", test_num);
	cin >> n;
	int i, j, k;

	long long res = 0;
	n--;
	for (i = 0, j = n; j >= 0; i++, j--)
	{
		res = (res + a[i][j]) % 100003;
	}
	cout << res << endl;
	cerr << test_num << endl;
}

int main()
{
	prepare();
	int k, i, j, tt;
	cin >> tt;
	__(a);
	int n = 501;
	fi(n + 1)
		a[0][i] = 1;
	fi(n + 1) if(i)
	{
		fj (n + 1) if(j)
		{
			a[i][j] = 0;
			fr(k, j + 1)
			{
				if (i - k >= 0)
				{
					a[i][j] += a[i - k][j];
					a[i][j] %= 100003;
				}
			}
		}
	}
	fi(tt)
		solve(i + 1);
	return 0;
}