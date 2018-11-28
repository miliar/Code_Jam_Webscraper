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

int a,b;
int nd;
int ndt;

int cycle(int i) {
	int ld=0;
	while(ld == 0)
		ld = i%10,i/=10;
	return i+ld*ndt;
}

void numdigits(int i) {
	nd=0;
	while(i)
		nd++,i/=10;
	ndt=1;
	FOR(i,0,nd-1) ndt*=10;
}

int main() {
	int tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";
		cin >> a >> b;
		int res=0;
		FOR(i,a,b) {
			numdigits(i);
			int cur=cycle(i);
			while(cur != i) {
				if(cur > i && a <= cur && cur <= b)
					res++;
				cur=cycle(cur);
			}
		}
		cout << res << endl;
	}
	return 0;
}
