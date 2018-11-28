/*

 E-Mail : ahmed.aly.tc@gmail.com

 Just For You :)

 */

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
const double PI = 2 * acos(0);
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


#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	cin >> N;
	int K;
	rep2(nn,1,N+1) {
		cin>>I>>K;
		J=I;
		vs v(I);
		rep(i,I)
			cin>>v[i];
		vs v2(J,string(I,' '));
		rep(i,I)
			rep(j,J)
				v2[j][I-i-1]=v[i][j];
		swap(I,J);
		bool up=1;
		while(up){
			up=0;
			for(int i=I-2;i>=0;i--)
				rep(j,J)
					if(v2[i+1][j]=='.' && v2[i][j]!='.'){
						up=1;
						v2[i+1][j]=v2[i][j];
						v2[i][j]='.';
					}
		}
		bool R=0,B=0;
		rep(i,I)
			rep(j,J){
			if(v2[i][j]=='R'){
				rep(k,8){
					int ni=i;
					int nj=j;
					int cc=0;
					while(ni<I && nj<J && ni>=0 && nj>=0 && v2[ni][nj]==v2[i][j]){
						cc++;
						ni+=di[k];
						nj+=dj[k];
					}
					if(cc>=K)
						R=1;
				}
			}
			if(v2[i][j]=='B'){
				rep(k,8){
					int ni=i;
					int nj=j;
					int cc=0;
					while(ni<I && nj<J && ni>=0 && nj>=0 && v2[ni][nj]==v2[i][j]){
						cc++;
						ni+=di[k];
						nj+=dj[k];
					}
					if(cc>=K)
						B=1;
				}
			}
		}
		printf("Case #%d: ", nn);
		if(R && B)
			printf("Both\n");
		else if(R)
			printf("Red\n");
		else if(B)
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
