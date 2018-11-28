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

int v[2000];
int h[2000];
int n;

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";

		cin >> n;
		FOR(i,0,n-1)
			cin >> v[i], v[i]--;
		bool epicfail = false;
		FOR(i,0,n-1) {
			if(v[i] <= i)
				epicfail = true;
			FOR(j,i+1,v[i])
				if(v[j] > v[i])
					epicfail = true;
		}
		if(epicfail) {
			cout << "Impossible" << endl;
		} else {
			h[n-1]=0;
			h[n-2]=0;
			FORD(cur,0,n-2) {
				int f=0;
				if(v[cur] == cur+1)
					h[cur] = 0;
				else {
					FOR(i,cur+1,v[cur]) {
						int dj = i-cur-1;
						int dk = v[cur] - cur - 1;
						int hj = h[i];
						int hk = h[v[cur]];
						int cf = ((dj+1)*hk - (dk+1)*hj) / (dj-dk) + 1;
						f = max(f,cf);
					}
					FOR(i,cur+1,n)
						h[i] += f * (min(i,v[cur])-cur-1);
					h[cur] = 0;
					f = (h[v[cur]]-h[cur])/(v[cur]-cur) + 1;
					FOR(i,cur+1,n)
						h[i] -= f * (i-cur);
				}
			}
			int minh = 0;
			FOR(i,0,n)
				minh = min(minh,h[i]);
			FOR(i,0,n)
				h[i] -= minh;

			FOR(i,0,n) {
				if(i) cout << " ";
				cout << h[i];
			}
			cout << endl;
		}
	}
	return 0;
}
