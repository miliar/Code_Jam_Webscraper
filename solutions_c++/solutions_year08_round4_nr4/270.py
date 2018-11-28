#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
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
	int cases, casen, k, n, ans, cur, i;
	char last, ch;
	VI a;
	string s;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> k >> s;
		n = SI(s);
		a = VI(k);
		FOR (i,k) a[i] = i;
		ans = n;
		do {
			cur = 0;
			last = ' ';
			FOR (i,n) {
				ch = s[k * (i / k) + a[i % k]];
				if (ch != last) cur++;
				last = ch;
			}
			ans = min(ans, cur);
		} while (next_permutation(BE(a)));
		cout << "Case #" << casen << ": " << ans << endl;
	}
	return 0;
}
