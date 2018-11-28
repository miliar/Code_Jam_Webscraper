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

int l, d, n;
string dict[10000], s;

vector < string > getChars(string s)
{
	vector < string > res;
	res.clear();
	int pos = 0;
	string cur;
	while (pos < s.size())
	{
		cur = "";
		if (isalpha(s[pos]))
		{
			cur.pb(s[pos++]);
			res.pb(cur);
			continue;
		}
		while(pos < s.size() && !isalpha(s[pos]))
			++pos;
		while (pos < s.size() && isalpha(s[pos]))
			cur.pb(s[pos++]);
		++pos;
		res.pb(cur);
	}
	return (res);
}

bool Check(string pattern, string dict)
{
	vector < string > v;
	v.clear();
	v = getChars(s);
	fi(dict.size())
	{
		bool ok = false;
		fj(v[i].size())
			if (v[i][j] == dict[i])
				ok = true;
		if (ok == false)
			return (false);
	}
	return (true);
}

void solve()
{
	cin >> l >> d >> n;
	fi(d)
		cin >> dict[i];

	fi(n)
	{
		int ans = 0;
		cin >> s;
		fj(d)
			if (Check(s, dict[j]))
				++ans;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}

void initf()
{
	freopen("in.txt", "r",  stdin);
	freopen("out.txt", "w",  stdout);
}

int main()
{
	initf();
	solve();
	return (0);
}