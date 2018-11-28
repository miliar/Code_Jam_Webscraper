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
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
//const double PI = 2 * acos(0);
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

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
int n;

std::string toString(int i) {
 std::ostringstream buffer;
 buffer << i;
 return buffer.str();
}

int main() {

	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	
	cin >> N;
	string s1;
	getline(cin,s1);
	rep2(nn,1,N+1) {
		int counter = 0;
		int N, S, p;
		cin >> N >> S >> p;

		for(int j = 0 ; j < N ; j++)
		{
			int now;
			cin >> now;

			if(now == 0) {
				if(p == 0) counter++;
				continue;
			}

			else if(now/3 >= p) {
				counter++;
			}
			
			else if(now%3 == 0 && now/3 == p-1 && S > 0) {
				S--;
				counter++;
			}

			else if(now%3 == 1 && now/3 == p-1) {
				counter++;
			}
			
			else if(now%3 == 2 && now/3 == p-1) {
				counter++;
			}

			else if(now%3 == 2 && now/3 == p-2 && S > 0) {
				S--;
				counter++;
			}
		}
		printf("Case #%d: ", nn);
		cout << counter << endl;
	}
	return 0;
}
