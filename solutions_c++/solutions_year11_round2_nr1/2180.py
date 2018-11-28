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

//#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
	freopen("a.out", "wt", stdout);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	double WP[100],OWP[100][100],AOWP[100],OOWP[100];
	int op[100];
	char table[100][100];
	cin >> N;
	For2(nn,1,N+1) {
		mem(WP,0);
		mem(OWP,0);
		mem(AOWP,0);
		mem(OOWP,0);
		mem(table,0);
		mem(op,0);
		cin>>n;
		For(i,n){
			getchar();
			For(j,n){
				scanf("%c",&table[i][j]);
			}
		}
		getchar();
		For(i,n){
			double wp=0;
			int count=0; 
			For(j,n){
				if(table[i][j]=='1')		wp++;
				if(table[i][j]!='.')	count++;
			}
			WP[i]= count==0? 0:wp/count;
		}

		For(i,n){
			For(j,n){
				if(j==i || table[i][j]=='.') continue;
				op[i]++;
				double owp=0;
				int c=0;
				For(k,n){
					if(k==i ) continue;
					if(table[j][k]=='1') owp++;
					if(table[j][k]!='.') c++;
				}
				OWP[i][j]= c==0? 0:owp/c;	
			}
		}

		For(i,n){
			For(j,n){
				AOWP[i]+=OWP[i][j]/op[i];
			}
		}

		For(i,n){
			For(j,n){
				if(j!=i && table[i][j]!='.')
					OOWP[i]+=AOWP[j]/op[i];
			}
		}


		printf("Case #%d:\n", nn);
		For(i,n) printf("%0.8f\n",0.25*WP[i]+0.5*AOWP[i]+0.25*OOWP[i]);
		//cout<<endl;
	}
	return 0;
}
