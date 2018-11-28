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

#define SMALL
//#define LARGE

int arr[110] ;
int main() {
	freopen("1.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
#endif

	cin >> N;
	rep2(nn,1,N+1) {
		// code here
		int mn ,mx ;
		cin >> n >> mn >> mx ;
		bool b = 0 ;
		for (int i = 0; i < n; ++i) {
			cin >> arr[i] ;
		}
		int  i = 0 ;
		bool f = 0 ;
		for (i = mn; i < mx+1; ++i) {
			b = 1 ;
			for (int j = 0; j < n ; ++j) {
				if(arr[j] % i != 0 && i%arr[j] !=0  ){
					b = 0 ;
					break ;
				}
			}
			if(b){
				f = 1 ;
				break ;
			}
		}
		if(!f){
			printf("Case #%d: NO\n",nn) ;
		}else{
			printf("Case #%d: %d\n",nn,i) ;
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
