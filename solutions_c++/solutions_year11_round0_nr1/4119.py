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



//#define _small_
#define _large_
int main() {

#ifdef _small_
	freopen("A-small.in", "rt", stdin);
#endif
#ifdef _large_
	freopen("A-large.in", "rt", stdin);
#endif
	freopen("A.out", "wt", stdout);

	//-----------------------

	int T,N,pos,b,o,tm,slack;
	bool isO;
	char c;
	cin >> T;

	for (int tt = 1; tt <= T; ++tt) {
		isO = slack = tm = 0;
		b = o = 1;
		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> c >> pos;//cout <<tm << endl;
			if(isO && c == 'O')
			{
				slack += abs(pos - o )+ 1;
				tm += abs(pos - o) + 1;
				o = pos;
			}
			else if(isO && c == 'B')
			{
				int toAdd = abs(pos - b) + 1 - slack;
				tm += (toAdd > 0 ? toAdd : 1);
				slack = (toAdd > 0 ? toAdd : 1);
				isO = 0;
				b = pos;
			}
			else if(!isO && c == 'B')
			{
				slack += abs(pos - b) + 1;
				tm += abs(pos - b) + 1;
				b = pos;
			}
			else if(!isO && c == 'O')
			{
				int toAdd =abs( pos - o)+ 1 - slack;
				tm += (toAdd > 0 ? toAdd : 1);
				slack = (toAdd > 0 ? toAdd : 1);
				isO = 1;
				o = pos;
			}

		}

		printf ("Case #%d: %d\n",tt,tm);
	}

	return 0;
}
