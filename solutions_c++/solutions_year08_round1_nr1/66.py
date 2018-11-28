#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
using namespace std;
typedef vector<int>VI;typedef vector<VI>VVI;
typedef vector<string>VS;
typedef pair<int,int>PII;
#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define BE(a) ((a).begin()),((a).end())
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define FORIT(i,a) for((i)=(a).begin();(i)!=(a).end();(i)++)
#define CLR(a,v) memset((a),(v),sizeof(a))

int main() {
	VI a, b;
	int cases, casen, n, i, j;
	long long x;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n;
		a.resize(n);
		b.resize(n);
		FOR (i,n) cin >> a[i];
		FOR (i,n) cin >> b[i];
		sort(BE(a));
		sort(BE(b), greater<int>());
		x = 0;
		FOR (i,n) x += a[i] * (long long)b[i];
		cout << "Case #" << casen << ": " << x << endl;
	}
	return 0;
}
