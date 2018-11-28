#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

void solve(){
	string s;
	cin >> s;
	int cnt = 0;
	vector<int> a;
	int64 now = 0;
	forn(i, s.size()){
		if (s[i] == '?')
			a.pb(s.size() - i - 1);
		if (s[i] == '1')
			now += 1ll << (s.size() - i - 1);
	}	
	
	cnt = a.size();
	forn(i, 1 << cnt){
		int64 cur = now;
		forn(j, a.size())
			if (i & (1 << j))
				cur += (1ll << a[j]);
		int64 w = sqrt(cur);
		if (w * w == cur){
			forn(j, a.size())
				if (i & (1 << j))
					s[s.size() - a[j] - 1] = '1';	
				else
					s[s.size() - a[j] - 1] = '0';
			cout << s << endl;
			return;
		}	

	}

}	        

int main ()
{
	int tst;
	cin >> tst;
	forn(i, tst){
		printf("Case #%d: ", i + 1);
		solve();
	}

	
	return 0;
}
