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
#define mp make_pair
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 5000;
const int inf = 1000000000 + 7;
const double eps = 1e-5;

int a[20][1000];

void solve()
{
	string s, temp = "welcome to code jam";
	getline(cin, s, '\n');

	clr(a);
	fi(s.size())
		if (s[i] == 'm')
			a[18][i] = 1;

	for(int i = temp.size() - 2; i >= 0; --i)
	{
		fj(s.size())
			if (s[j] == temp[i])
				for(int k = j + 1; k < s.size(); ++k)
					a[i][j] = (a[i][j] + a[i + 1][k]) % 10000;
	}
	int ans = 0;
	fi(s.size())
		ans = (ans + a[0][i]) % 10000;
	printf("%.4d\n", ans);
}

void initf()
{
	//freopen("in.txt", "r",  stdin);
	//freopen("out.txt", "w",  stdout);
}

int main()
{
	initf();
	int t;
	scanf("%d\n", &t);
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}