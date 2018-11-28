#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <memory.h>

using namespace std;

#define fr(i,a,b) for(int i = (a); i <= (b); ++i)
#define frR(i,a,b) for(int i = (a); i >= (b); --i)
#define fi(a) for(int i = (0); i < (a); ++i)
#define fj(a) for(int j = (0); j < (a); ++j)
#define fk(a) for(int k = (0); k < (a); ++k)
#define CLR(a, b) memset((a), (b), sizeof((a)))
#define clr(a) CLR((a), 0)
#define pb push_back
#define mkp make_pair
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 5000;
const int inf = 1000000000 + 7;
const double eps = 1e-5;

int n, a[100][100];
char s[1000];

void Swap(int i, int j)
{
	fk(n)
		swap(a[i][k], a[j][k]);
}

void solve()
{
	scanf("%d\n", &n);
	fi(n)
	{
		gets(s);
		fj(n)
			a[i][j] = s[j] - '0';
	}

	int ans = 0;
	fi(n)
	{
		for(int j = i; j < n; ++j)
		{
			bool ok = true;
			for(int k = i + 1; k < n; ++k)
				if (a[j][k] == 1)
				{
					ok = false;
					break;
				}
			if (ok)
			{
				for(int k = j; k > i; --k)
					Swap(k, k - 1);
				ans += j - i;
				break;
			}
		}
	}
	cout << ans << endl;
}

void initf()
{
	freopen("in.txt", "r",  stdin);
	freopen("out.txt", "w",  stdout);
}

int main()
{
	//initf();
	int t;
	scanf("%d", &t);
	fi(t)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return (0);
}