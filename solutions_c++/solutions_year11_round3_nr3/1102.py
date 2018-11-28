#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define SZ(v) (int)v.size()

#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;

const int oo = (int) 1e9;
const double PI = 3.141592653589793;
const double eps = 1e-11;



#define _small_
//#define _large_

int main() {

#ifdef _small_
	freopen("C-small.in", "rt", stdin);
#endif
#ifdef _large_
	freopen("C-large.in", "rt", stdin);
#endif
	freopen("C.out", "wt", stdout);

	//-----------------------

	int T, N ,L ,H;
	vector<int> v;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {

		cin >> N >> L >> H;
		v.clear();
		v.resize(N);
		for (int k = 0; k < N; ++k) {
			cin >> v[k];
		}
		bool ok =1;
		int i;
		for (i = L; i <= H; ++i) {
			ok =1;
			for (int j = 0; j < N; ++j) {
				if(!(i % v[j] == 0 || v[j] % i == 0))
				{
					ok = 0;
					break;
				}
			}
			if(ok)
				break;

		}

		printf ("Case #%d: ",tt);
		if(ok)
			cout << i <<endl;
		else
			cout<<"NO\n";
	}

	return 0;
}
