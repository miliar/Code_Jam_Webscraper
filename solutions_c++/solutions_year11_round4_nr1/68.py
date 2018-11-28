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
const string task = "";

template <class T> T sqr (T x) {return x * x;}

double x, r, t, s;
int n;
double b[100100], e[100100], w[100100];

double run(double len, double sp){
	double ft = min(t, len / (sp + r - s));
	t -= ft;
	double res = ft + (len - (sp + r-s) * ft) / (sp); 
	return res;
}

double solve(){
	cin >> x >> s >> r >> t >> n;
	forn(i, n)
		cin >> b[i] >> e[i] >> w[i];
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			if (b[j] < b[i]){
				swap(b[j], b[i]);
				swap(e[j], e[i]);
				swap(w[j], w[i]);
			}
	double res = 0;
	double now = 0;
	vector<pair<double, double> > q;
	for (int i = 0; i < n; i++){
		if (b[i] > now)
			q.pb(mp(s, b[i] - now));
		q.pb(mp(w[i] + s, e[i] - b[i]));
		now = e[i];
	}	
	if (now < x)
		q.pb(mp(s, x - now));
	sort(all(q));
	forn(i, q.size())
		res += run(q[i].sc, q[i].fs);
			
	return res;
}	        

int main ()
{
	int tst;
	cin >> tst;
	forn(i, tst)
		printf("Case #%d: %0.9lf\n", i + 1, solve());

	
	return 0;
}
