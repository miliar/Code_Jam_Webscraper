#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); i++)
#define sz(a) int((a).size()) 
#define all(c) (c).begin(), (c).end() 
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c, x) ((c).find(x) != (c).end()) 
#define cpresent(c, x) (find(all(c), x) != (c).end())
template<class T> T sqr(T x){return x*x;}
int toint(string s){istringstream sin(s); int x; sin>>x; return x;}
string tostring(int x){ostringstream sout; sout<<x; return sout.str();}

enum {SIZE = 1005};

long long r, k, n, g[SIZE], euro[SIZE], pos, ret, rem, next[SIZE], pref[SIZE], last;

void process(int cas)
{
	map<long long, long long> s;

	scanf("%lld %lld %lld", &r, &k, &n);

	memset(euro, 0, sizeof(euro));
	rem = ret = 0;

	for(int i = 0; i < n; i++)
		scanf("%lld", &g[i]);

	for(int i = 0; i < n; i++) {
		for(int j = i; j < n && euro[i] + g[j] <= k; j++) {
			euro[i] += g[j];
			last = j;
		}
		if(last != n - 1) {
			next[i] = last + 1;
			continue;
		}
		for(int j = 0; j < i && euro[i] + g[j] <= k; j++) {
			euro[i] += g[j];
			last = j;
		}
		next[i] = (last + 1) % n;
	}

	pos = 0;
	
	for(long long i = 0; i < r; i++) {
		if(present(s, pos)) {
			ret = pref[i - 1];
			if(s[pos] != 0)
				ret += (pref[i - 1] - pref[s[pos] - 1])*((r - i)/(i - s[pos]));
			else
				ret += pref[i - 1] * ((r - i)/(i - s[pos]));
			rem = (r - i) % (i - s[pos]);
			break;
		}

		s[pos] = i;
		pref[i] = euro[pos] + ((i > 0) ? pref[i - 1] : 0);
		ret = pref[i];
		pos = next[pos];
	}

	for(long long i = 0; i < rem; i++) {
		ret += euro[pos];
		pos = next[pos];
	}

	printf("Case #%d: %lld\n", cas, ret);
}

int main()
{
	int t;

	scanf("%d", &t);
	
	for(int i = 1; i <= t; i++)
		process(i);
	
	return 0;
}
