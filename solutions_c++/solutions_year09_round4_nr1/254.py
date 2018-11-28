	#include <iostream>
#include <cassert>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int inf = (int)1E+9;

typedef long long int64;
typedef pair<int,int> pii;
typedef  double real;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define last(a) (int)a.size() - 1
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())


int n;
char a[50][50];

int calc(){
	int res = 0;
	forn(i,n){
		for (int j = i; j < n; j++){
			bool now = 1;
			for (int k = i+1; k < n; k++)
				if (a[j][k] == '1')
					now = 0;
			if (now){
				for (int p = j; p > i; p--){
					forn(k,n)
						swap(a[p-1][k], a[p][k]);
					res++;
				}
				break;
			}
		}
/*		forn(x,n){
			forn(y,n)
				cerr << a[x][y];
			cerr << endl;
		}
		cerr << endl;
*/	}
	return res;

}

int main(){
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);
	

	int tst;
	cin >> tst;
	forn(i,tst){
		cin >> n;
		forn(i,n)
			forn(j,n)
				cin >> a[i][j];
	
		printf("Case #%d: %d\n", i+1, calc());
	}

	return 0;
}
