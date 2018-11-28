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

int GCD(int a, int b)
{
	return (b == 0 ? a : GCD(b, a%b));
}
int LCM(int x,int y)
{
        return x*y/GCD(x,y);
}
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

	int T,N,R,C;
	cin >> T;
	vector<  string > v;
	for (int tt = 1; tt <= T; ++tt) {
		v.clear();

		cin >> R >> C;
		v.resize(R);
		for (int i = 0; i < R; ++i) {
			cin >> v[i];

		}
		bool ok = 1;
		for (int i = 0; i < R - 1; ++i) {
			for (int j = 0; j < C - 1; ++j) {
				if(v[i][j] == '#')
				{
					if(v[i][j] == '#' && v[i][j+1] == '#' && v[i+1][j] == '#' && v[i+1][j+1] == '#' )
						{
							v[i][j] = v[i + 1][j + 1] = '/';
							v[i][j+1] = v[i+1][j] = '\\';
						}
					else
					{
						ok = 0;
						break;
					}

				}

			}
			if(!ok)
				break;
		}

		for (int i = 0; i < R; ++i) {
			ok &= v[i][C-1] != '#';
		}
		for (int j = 0; j < C; ++j) {
			ok &= v[R-1][j] != '#';
		}
		printf ("Case #%d:\n",tt );
		if(ok)
		{

			for (int i = 0; i < R; ++i) {
				cout<< v[i] <<endl;
			}
		}
		else
		{
			cout << "Impossible\n";
		}
	}

	return 0;
}
