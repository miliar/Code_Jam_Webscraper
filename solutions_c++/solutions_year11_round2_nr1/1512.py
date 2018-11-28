/*
 Name  : Mohammed Magdi
 Email : acm.magdi@gmail.com 
 */
#include <cstring>
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
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int OO = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int N, n;

//#define SMALL
#define LARGE

int pMa[110];
int won[110];
double wonP[110];
double OWP[110];
double OOWP[110];
int main() {
	freopen("1.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif

	cin >> N;
	rep2(nn,1,N+1) {
		// code here
		printf("Case #%d:\n", nn);
		cin >> n;
		string S;
		vector<string> mat;
		mem(pMa,0);
		mem(won,0);
		rep(i,n) {
			cin >> S;
			for (int j = 0; j < S.size(); ++j) {
				if (S[j] != '.') {
					pMa[i]++;
					if (S[j] == '1')
						won[i]++;
				}
			}
			mat.push_back(S);
		}
		for (int i = 0; i < n; ++i) {
			wonP[i] = (double) won[i] / (double) pMa[i];
		}
		for (int i = 0; i < n; ++i) {
			double sum = 0;
			for (int j = 0; j < n; ++j) {
				if( i == j || mat[i][j] == '.') continue ;
				double w = 0, t = 0;
				for (int k = 0; k < n; k++) {
					if (mat[j][k] != '.' && k != i) {
						t++;
						if (mat[j][k] == '1')
							w++;
					}
				}
				sum += w / t;
			}
			OWP[i] = sum / (double) pMa[i];
		}
		for (int i = 0; i < n; ++i) {
			double sum = 0;
			for (int j = 0; j < n; ++j) {
				if (mat[i][j] != '.') {
					sum += OWP[j];
				}
			}
			OOWP[i] = sum / (double) pMa[i];
		}
		for (int i = 0; i < n; ++i) {
			double RPI = 0.25 * wonP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			//				cout << RPI << endl ;
			printf("%.6lf\n", RPI);
		}

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
