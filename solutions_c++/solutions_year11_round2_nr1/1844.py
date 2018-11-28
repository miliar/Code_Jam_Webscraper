#include<iostream>
#include<iomanip>
#include<algorithm>
#include<sstream>
#include<vector>
#include<queue>
#include<string>

using namespace std;

#define FOR(i,a,b) for ( int i = a ; i <= b ; i ++ )
#define FRD(i,a,b) for ( int i = a ; i >= b ; i -- )
#define FR(i,a) FOR(i,0,a-1)
#define FZ(i,a) FRD(i,a,0)
#define sz size()
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define FRV(i,v) FR( i , v.sz - 1 )
#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vs vector<string>
#define vc vector<char>

#define mp make_pair
#define ii <int,int>
#define id <int,double>
#define ss stringstream
#define MAX_INT ((1<<31)-1)

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

int ni() { int n; cin >> n ; return n; }
string ns() { string s; cin >> s ; return s; }
char nc() { char c; cin >> c ; return c; }
string nline() { string n; do { getline(cin,n); } while(n == ""); return n;}

void main(){
	int T;

	T = ni();

	FOR(tcn,1,T){
		int N = ni();
		vector<vi> g(N,vi(N,0));
		vf WP(N,0.0), OWP(N,0.0), OOWP(N,0.0);

		FR(i,N){
			int w=0,t=0;
			FR(j,N){
				g[i][j] = nc();
				if ( g[i][j] != '.' ) {
					t++;
					if ( g[i][j] == '1' ) w ++;
				}
			}
			WP[i] = (float)w/(float)t;
		}

		FR(ignore,N){
			int opo = 0;
			FR(i,N){
				if ( g[ignore][i] == '.' ) continue;
				opo ++;
				int w = 0, t = 0;
				FR(j,N){
					if ( j == ignore ) continue;
					if ( g[i][j] == '.' ) continue;
					if ( g[i][j] == '1' ) w ++;
					t ++;
				}
				OWP[ignore] += (float)w/(float)t;
			}
			OWP[ignore] /= opo;
		}

		FR(i,N){
			int opo = 0;
			float t = 0.0;
			FR(j,N)
				if ( g[i][j] != '.' ) t+= OWP[j],opo++;

			OOWP[i] = t / (float)opo;
		}
		
		ss res;
		cout << "Case #" << tcn << ": "<<res.str()<<endl;
		FR(i,N){
			float RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			cout << RPI <<endl;
		}
	}
}