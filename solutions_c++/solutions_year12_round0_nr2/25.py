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

int n,s,p;

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";
		cin >> n >> s >> p;
		int thres = (p-1)*3;
		int res=0;
		FOR(i,0,n) {
			int x;
			cin >> x;
			if(x>thres)
				res++;
			else if(p>1 && x+2>thres && s>0)
				res++,s--;
		}
		cout << res << endl;
	}
	return 0;
}
