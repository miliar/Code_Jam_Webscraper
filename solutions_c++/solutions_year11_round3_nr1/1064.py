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

#define INF 1.0E+15
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
int n,m;

#define SMALL
#define LARGE
int main() {
freopen("A-small-attempt0.in","rt",stdin);
freopen("A-small.out","wt",stdout);
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	char map[50][50];

	cin >> N;
	For2(nn,1,N+1) {
		bool possible=false; 
		mem(map,0);
		cin>>n;
		cin>>m;
		For(i,n){
			getchar();
			For(j,m) scanf("%c",&map[i][j]);
			
		}

		For(i,n){
			For(j,m){
				if(map[i][j]=='#')
				{
					if(map[i+1][j]=='#' && map[i][j+1]=='#' &&map[i+1][j+1]=='#'){

					map[i][j]='\/';
					map[i][j+1]='\\';
					map[i+1][j]='\\';
					map[i+1][j+1]='\/';
					}	
					else{
						possible = false;
						goto end;
					}
				}
			}
		}
		possible=true;
		end:
		printf("Case #%d:", nn);
		if(!possible)
		 printf("\nImpossible");
		else 
			For(i,n){
				printf("\n");
				For(j,m){printf("%c",map[i][j]);}
				
		}

		cout<<endl;
	}
	return 0;
}
