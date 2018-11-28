// USTU Frogs
// Accepted
// I'm Feeling Lucky!

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cassert>
//#include <cmath>

using namespace std;

#define fr(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define fi(n) for(int i = 0; i < (n); ++i)
#define fj(n) for(int j = 0; j < (n); ++j)
#define fk(n) for(int k = 0; k < (n); ++k)
#define pb push_back
#define mp make_pair
#define clr(a) memset((a), 0, sizeof(a))
#define CLR(a,b) memset((a), (b), sizeof(a))
#define all(v) (v).begin(),(v).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull; 
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = (1 << 30);
const double eps = 1e-5;

char buf[1000];
int n, m;
vector <string> v1[200], v2[200];

vector < string > parse()
{
	vector < string > v;
	int pos = 0, len = strlen(buf);

	while (pos < len)
	{
		string s = "";
		while (pos < len && buf[pos] != '/')
			s.pb(buf[pos++]);
		if (s != "")
			v.pb(s);
		++pos;
	}
	return (v);
}

int make(const vector < string > &v)
{
	int common = 0;
	fi(n)
	{
		int lim = min(v1[i].size(), v.size()), cur = 0;;
		fj(lim)
			if (v[j] == v1[i][j])
				cur++;
			else
				break;
		common = max(common, cur);
	}
	return ((int)v.size() - common);
}

void solve()
{
	fi(200)
	{
		v1[i].clear();
		v2[2].clear();
	}

	gets(buf);
	sscanf(buf, "%d%d", &n, &m);

	fi(n)
	{
		gets(buf);
		v1[i] = parse();
	}

	fi(m)
	{
		gets(buf);
		v2[i] = parse();
	}

	sort(v1, v1 + n);
	sort(v2, v2 + m);

	int ans = 0;
	fi(m)
	{
		ans += make(v2[i]);
		v1[n++] = v2[i];
	}
	cout << ans << endl;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	gets(buf);
	sscanf(buf, "%d", &t);
	fi(t)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
} 
