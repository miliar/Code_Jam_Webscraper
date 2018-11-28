#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sqr(a) (a)*(a)

typedef long long int64;
typedef pair<int,int> pii;

const int inf = (int)1E+9;
const double eps = 1e-9;

const string task = "a";
const string inp = task + ".in";
const string oup = task + ".out";

const int nmax = 10000;
typedef vector<int> tlong;

int n;
tlong a[nmax];
tlong res,ans;

void norm(tlong &a){
	while(a.size() > 0 && a.back() == 0)
		a.pop_back();
}


void read(tlong &a){
	a.clear();
	string s;
	cin >> s;
	ford(i,s.size())
		a.pb(s[i]-'0');
}

void write(tlong a){
	if (a.size() == 0) a.pb(0);
	ford(i,a.size())
		printf("%d",a[i]);
	cout << endl;
}
		
bool ls(tlong a, tlong b){
        norm(a);
        norm(b);
	if (a.size() != b.size())
		return a.size() < b.size();
	ford(i,a.size())
		if (a[i] != b[i])
			return a[i] < b[i];
	return 0;
}

tlong operator-(tlong a, tlong b){
	forn(i,b.size()){
		a[i] -= b[i];
		while (a[i] < 0){
			a[i] += 10;
			a[i+1] --;
		}
	}
	forn(i,a.size())
		while (a[i] < 0){
			a[i] += 10;
			a[i+1] --;
		}
	norm(a);
	return a;
}

tlong operator*(tlong a, tlong b){
	tlong c(a.size() + b.size() + 1, 0);
	forn(i,a.size())
		forn(j,b.size()){
			c[i+j] += a[i] * b[j];
			if (c[i+j] >= 10){
				c[i+j+1] += c[i+j] / 10;
				c[i+j] %= 10;
			}
		}
	forn(i,c.size())
		if (c[i] >= 10){
			c[i+1] += c[i] / 10;
			c[i] %= 10;
		}
	norm(c);
	return c;
}

tlong operator/(tlong a, tlong b){
	if (ls(a,b)){
		tlong res;
		return res;
	}
	norm(a);
	norm(b);
	tlong c(a.size() - b.size() + 1,0);
	ford(i,c.size()){
		while(!ls(a, b*c))
			c[i] ++;
		assert(c[i] <= 10);
		c[i]--;
	}
	norm(c);
	return c;
}

tlong operator%(tlong a, tlong b){
	tlong c = a / b;
	tlong res = a - b * c;
	norm(res);
	return res;
}


tlong gcd(tlong a, tlong b){
	if (a.size() == 0 || (a.size() == 1 && a[0] == 0)) return b;
	return gcd(b%a,a);
}

void solve(){
	scanf("%d",&n);
	forn(i,n)
		read(a[i]);
	sort(a, a + n,ls);
	res.clear();
	ans.clear();

	forn(i,n-1)
		if (a[i+1] != a[i]){
			if (res.size() == 0) res = a[i+1] - a[i];
			res = gcd(res,a[i+1] - a[i]);
		}
	forn(i,n){
		if (ans.size() == 0) ans = (res - a[i]%res) % res;
		ans = min(ans,(res - a[i]%res) % res);
	}
	write(ans);
	forn(i,n)
		a[i].clear();
}

int main(){
	freopen(inp.data(), "rt", stdin);
	freopen(oup.data(),"wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		printf("Case #%d: ",i+1);
		solve();
	}

	return 0;
}
