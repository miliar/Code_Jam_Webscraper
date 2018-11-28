/*
 E-Mail : acm.magdi@gmail.com
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

using namespace std;


#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
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

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int R, C, N;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= R || j >= C)
		return false;
	return true;
}

const int SIZE = 1010;

#define SMALL
//#define LARGE
char ch[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'} ;
bool vis[26] ;
int main() {
	freopen("1.in", "rt", stdin);
	freopen("1.out", "rt", stdout);
#ifdef SMALL
	freopen("B-small-attempt2.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif

	cin >> N;
	memset(vis,0,sizeof vis);
	for (int i = 0; i < 8 ; ++i) {
		vis[ch[i]-'A'] = 1 ;
	}
	for (int nn = 1; nn <= N; ++nn) {
		map<pair<char,char> , char> inv ;
		map<char,char> opp ;
		int a, b, n;
		cin >> a;
		string str ;
		for (int i = 0; i < a; ++i) {
			cin >> str ;
			inv.insert(mp(mp(str[0],str[1]),str[2])) ;
			inv.insert(mp(mp(str[1],str[0]),str[2])) ;
		}
		cin >> b ;
		for (int i = 0; i < b; ++i) {
			cin >> str ;
			opp.insert(mp(str[0],str[1]));
			opp.insert(mp(str[1],str[0]));
		}
		cin >> n ;
		cin >> str ;
		vector<char> res ;
		for (int i = 0; i < n ; ++i) {
			if(vis[str[i]-'A']){
				if(res.size()){//check if inv
					if(inv.count(mp(str[i],res[res.size()-1]))!=0){
						res.push_back(inv[mp(str[i],res[res.size()-1])]);
						res.erase(res.end()-2);

					}else if(opp.count(str[i])!=0){
						char op = opp[str[i]] ;
						bool f = 1 ;
						int kk = res.size();
						for (int j = res.size()-1 ; j >= 0; --j) {
							if(res[j] == op){
								f = 0 ;
								res.clear();
								break;
							}
						}
						if(f)res.push_back(str[i]);
					}else res.push_back(str[i]);
				}else res.push_back(str[i]);
			}else{
				res.push_back(str[i]);
			}
		}
		string ans = "[" ;
		for(int i = 0 ; i < res.size() ; i++){
			ans += res[i] ;
			if(i < res.size()-1)
				ans += ", " ;
		}
		ans += "]" ;

		printf("Case #%d: ",nn);
		cout << ans << endl;
#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
