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
#define FR(i,a) FOR(i,0,a)
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
		int R = ni(), C = ni();
		vector<vc> g(R,vc(C,0));
		FR(i,R-1)
			FR(j,C-1)
				g[i][j] = nc();


		FR(i,R-1)
			FR(j,C-1)
		{
			if ( g[i][j] == '#' ){
				if ( i < R-1  && j < C-1 ){
					if ( g[i][j] == '#' && g[i+1][j] == '#' && g[i][j+1] == '#' && g[i+1][j+1] == '#' ){
						g[i+1][j+1] = g[i][j] = '/';
						g[i][j+1] = g[i+1][j] = '\\';
					}
				}
			}
		}

		bool impossible = false;
		FR(i,R-1)
				FR(j,C-1) if ( g[i][j] == '#' ) {impossible = true; break;}
		ss res;
		cout << "Case #" << tcn << ": "<<endl;
		if ( impossible ){
			cout <<"Impossible"<<endl;
		}else{
			FR(i,R-1){
				FR(j,C-1){
					cout << g[i][j];
				}
				cout << endl;
			}
		}
	}
}