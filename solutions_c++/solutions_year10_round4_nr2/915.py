#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
using namespace std;

#define forloop(i, s, t) for(__typeof(s) i = s; i t; i++)
#define forrloop(i, s, t) for(__typeof(s) i = s; i t; i--)
#define foreach(itr, c) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); itr++)

#define tpop(x) (x).top(); (x).pop();
#define fpop(x) (x).front(); (x).pop();
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()

#define chmin(a, b) a = min(a, b)
#define chmax(a, b) a = max(a, b)
//inline void chmin(int& a, const int b) { a = min(a, b); }
//inline void chmax(int& a, const int b) { a = max(a, b); }

#define debug(v) #v << '=' << v
#define pdebug(v, w) '(' << debug(v) << ',' << debug(w) << ')'

#define printgrid(g, y, x) forloop(i, 0, < y) {	forloop(j, 0, < x) cout<< g[i][j] << ' ';	cout << endl; }
/*inline void printgrid(RandomAccessIterator g, int y, int x) {
	forloop(i, 0, < y) {
		forloop(j, 0, < x) cout<< g[i][j] << ' ';
		cout << endl;
	}
}*/

#define gcase int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gstate() cerr << "Case: " << gtest << '/' << T << endl
#define gout cout << "Case #" << gtest << ": "

const int INF = numeric_limits<int>::max();
const double EPS = INF*numeric_limits<double>::epsilon();

int P;

bool chrange(int *start, int *end) {
	int nPass = 0;
	forloop(i, start, < end) {
		if((*i)++ >= P) nPass++;
	}
	//cout << debug(nPass) << endl;
	return nPass != (end-start);
}

int main() {
	gcase {
		gstate();
		int M[1024];
		cin >> P;
		forloop(i, 0, < (1<<P)) cin >> M[i];
		forloop(i, 0, < P) {
			int d;
			forloop(j, 0, < (1 << (P-i-1))) cin >> d;
		}
		int ans = 0;
		forloop(i, 0, < P) {
			int parts = 1<<i;
			int partsz = (1<<P)/parts;
			forloop(j, 0, < parts) {
				if(chrange(M+j*partsz, M+(j+1)*partsz)) {
					ans++;
					//cout << "ans++ on part " << j << endl;
				}
			}
			//forloop(i, 0, < (1<<P)) cout << M[i] << ' ';
			//cout << endl;
			/*int nPass = 0;
			forloop(j, 0, < (1<<P)) {
				if(M[j]++ >= P) nPass++;
			}
			if(nPass == (1<<P)) break;
			ans += (1 << i);*/
		}
		gout << ans << endl;
		//cout << endl << endl;
	}
}
