#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <ctime>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<string> vs;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (int i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

vector<pii> vine;
vi maxlen;

int nextvine=0;

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";

		vine.clear();
		maxlen.clear();

		int n,D;
		cin >> n;
		FOR(i,0,n) {
			int d,l;
			cin >> d >> l;
			vine.push_back(pii(d,l));
			maxlen.push_back(-1);
		}
		cin >> D;
		vine.push_back(pii(D,0));
		maxlen.push_back(-1);
		sort(all(vine));

		maxlen[0] = vine[0].first;
		nextvine = 1;

		FOR(i,0,n) {
			if(i>=nextvine)
				break;
			if(nextvine>n)
				break;
			if(vine[nextvine].first <= vine[i].first + maxlen[i]) {
				maxlen[nextvine] = min(vine[nextvine].second, vine[nextvine].first - vine[i].first);
				nextvine++;
				i--;
			}
		}
		if(nextvine>n)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
