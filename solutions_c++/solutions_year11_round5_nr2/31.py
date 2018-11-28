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

const int nmax = 10100;

int cnt[nmax];
int w[nmax], a[nmax], ad[nmax], ca[nmax];
int n;

void solve(){
	cin >> n;
	memset(cnt, 0, sizeof cnt);
	memset(w, 0, sizeof w);
	forn(i, n){
		cin >> a[i];
		cnt[a[i]] ++;
	}

	int l = 0, r = n;
	for (int i = 1; i < nmax; i++)
		ad[i] = max(0, cnt[i] - cnt[i-1]);
	while (l < r){
		int mid = (l + r + 1) / 2;
		memset(ca, 0, sizeof ca);
		for (int i = 1; i < nmax; i++){
		     ca[i] += ad[i];
		     ca[i+mid] -= ad[i];
		}
		int now = 0;
		bool done = 1;
		for (int i = 1; i < nmax; i++){
			now += ca[i];
			if (now > cnt[i])
				done = 0;
		}
		if (done)
			l = mid;
		else
			r = mid - 1;
	}



	cout << l << endl;
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
