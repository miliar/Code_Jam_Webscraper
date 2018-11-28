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

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define For(i,m) for(int i=0;i<(int)(m);i++)
#define For2(i,n,m) for(int i=n;i<(int)(m);i++)
#define It(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
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
const double PI = 2 * acos((double)0);
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
int n;


int arr[2009];
//#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
	freopen("a.out", "wt", stdout);
#ifdef SMALL
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	
	int diff;
	char rob;
	cin >> N;
	For2(nn,1,N+1) {
		int posO=1,posB=1,next,Ot=0,Bt=0,time=0;
		cin>>n;
		For(i,n){
			cin >> rob;
			cin >> next;
			if(rob == 'O'){
				diff = (next > posO) ? next-posO:posO-next;
				if(Ot!=0)
					diff= (diff > Ot) ? diff-Ot:0;
				time+=diff;
				Bt+=diff;
				posO=next; Ot=0;
				Bt++; time++;
			}
			else {
				diff = (next > posB) ? next-posB:posB-next;
				if(Bt!=0)
					diff= (diff > Bt) ? diff-Bt:0;
				time+=diff;
				Ot+=diff;
				posB=next; Bt=0;
				Ot++; time++;

			}
		}

		printf("Case #%d: ", nn);
		cout<<time<<endl;
	}
	return 0;
}