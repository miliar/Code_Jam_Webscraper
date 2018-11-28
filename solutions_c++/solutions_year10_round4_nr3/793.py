#if defined(_MSC_VER)
#define _CRT_SECURE_NO_WARNINGS
#include <boost/typeof/typeof.hpp>
#define typeof BOOST_TYPEOF
#endif
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <cassert>
#include <complex>
using namespace std;

const int dr[]={0,-1,0,1,-1,1, 1,-1};
const int dc[]={1,0,-1,0, 1,1,-1,-1};
const double eps=1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef pair<double, double> pdd;
typedef vector<pdd> vpdd;
typedef complex<double> pnt;
typedef vector<pnt> vpnt;
typedef vector<vector<pair<int, long long> > > Graph;

#define fr(i,a,b) for(int i(a),_b(b);i<=_b;++i)
#define frd(i,a,b) for(int i(a),_b(b);i>=_b;--i)
#define rep(i,n) for(int i(0),_n(n);i<_n;++i)
#define reps(i,a) fr(i,0,sz(a)-1)
#define fore(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define maximum(a) (*max_element(all(a)))
#define minimum(a) (*min_element(all(a)))
#define clr(x,a) memset(x,a,sizeof(x))
#define findx(a,x) (find(all(a),x)-a.begin())
#define two(X) (1LL<<(X))
#define contain(S,X) (((S)&two(X))!=0)

template<class T> void print(T const &x) {ostringstream os; os<<x; cout<<os.str()<<endl;}
template<class T> void print(vector<T> const &v) {ostringstream os; for(int i=0; i<v.size(); ++i){if(i)os<<' ';os<<v[i];} cout<<os.str()<<endl;}
template<class T> void print(vector<vector<T> > const &v){ostringstream os; for(int i=0;i<v.size();++i) {for(int j=0;j<v[i].size();++j){if(j)os<<' ';os<<v[i][j];}os<<endl;}cout<<os.str()<<endl;}
template<class T> int sz(const T&c){return (int)c.size();}
template<class T> void srt(T&c){std::sort(c.begin(),c.end());}
template<class T> void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T sqr(T x){return x*x;}
template<class T, class U> T cast (U x) { ostringstream os; os<<x; T res; istringstream is(os.str()); is>>res; return res; }
template<class T> vector<T> split(string s, string x=" ") {vector<T> res; for(int i=0;i<s.size();i++){string a; while(i<(int)s.size()&&x.find(s[i])==string::npos)a+=s[i++]; if(!a.empty())res.push_back(cast<T>(a));} return res;}
template<class T> bool inside(T r,T c,T R, T C){return r>=0 && r<R && c>=0 && c<C;}

int main( int argc, char* argv[] ) {	
    string path = "C:/codejam/C-small-attempt0";
	freopen((path+".in").c_str(),"r",stdin);
	freopen((path+".out").c_str(), "w", stdout);

	int testCases;
	cin>>testCases;

	for(int testCase=1;testCase<=testCases;testCase++){

		int r;
		cin>>r;

		vvi a(100,vi(100));
		rep(i,r){
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			--x1;--y1;--x2;--y2;

			fr(x,x1,x2)fr(y,y1,y2)a[x][y]=1;
		}

		int res=0;

		while(true){
			rep(i,100)rep(j,100)
				if(a[i][j]){goto m1;}

			break;
m1:
			vvi b(100,vi(100));
			rep(row,100){
				rep(col,100){
					bool bn=(row==0 || a[row-1][col]==0);
					bool bw=(col==0 || a[row][col-1]==0);
					if(a[row][col]==1){
						b[row][col]= bn && bw ? 0 : 1;
					} else {
						b[row][col]= !bn && !bw ? 1 : 0;
					}					
				}
			}
			a=b;
			++res;
		}

		cout << "Case #" << testCase << ": " << res << endl;
		cout.flush();
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
