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
typedef vector<vector<pair<int, long long> > > Graph;
typedef complex<double> pnt;
typedef vector<pnt> vpnt;


#define fr(i,a,b) for(int i(a),_b(b);i<=_b;++i)
#define frd(i,a,b) for(int i(a),_b(b);i>=_b;--i)
#define rep(i,n) for(int i(0),_n(n);i<_n;++i)
#define repd(i,n) for(int i((n)-1);i>=0;--i)
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
template<class T> T inside(T r,T c,T R, T C){return r>=0 && r<R && c>=0 && c<C;}


int x[64],y[64],r[64];
int p[64];

pnt getCenter(ll Ax,ll Ay,ll Bx,ll By,ll Cx,ll Cy,ll d){
	ll cx=By*Ax*Ax-Cy*Ax*Ax-By*By*Ay+Cy*Cy*Ay+Bx*Bx*Cy+Ay*Ay*By+Cx*Cx*Ay-Cy*Cy*By-Cx*Cx*By-Bx*Bx*Ay+By*By*Cy-Ay*Ay*Cy;
	ll cy=Ax*Ax*Cx+Ay*Ay*Cx+Bx*Bx*Ax-Bx*Bx*Cx+By*By*Ax-By*By*Cx-Ax*Ax*Bx-Ay*Ay*Bx-Cx*Cx*Ax+Cx*Cx*Bx-Cy*Cy*Ax+Cy*Cy*Bx;
	double rx=double(cx)/d;
	double ry=double(cy)/d;
	return pnt(rx,ry);
}


int main( int argc, char* argv[] ) {
	freopen("C:/codejam/D-small.in","r",stdin);
	freopen("C:/codejam/D-small.out", "w", stdout);

	int testCases;
	cin>>testCases;

	for(int testCase=1;testCase<=testCases;testCase++){
			int n;
			cin>>n;

			rep(i,n)scanf("%d%d%d",&x[i],&y[i],&r[i]);

			double res=1e20;

			rep(i1,n){
				double r1,rx,ry;
				r1=r[i1];
				rx=x[i1];
				ry=y[i1];
				int n1=0;
				rep(i,n){
					double d2=hypot(rx-x[i],ry-y[i])+r[i];
					if(d2>r1+1e-5)p[n1++]=i;
				}
				if(n1==0)checkmin(res,r1);

				rep(k1,n1)fr(k2,k1,n1){
					double r2,rx,ry;
					if(k1==k2){
						rx=x[p[k1]];
						ry=y[p[k1]];
						r2=r[p[k1]];				
					} else{
						r2=(hypot(x[p[k1]]-x[p[k2]],y[p[k1]]-y[p[k2]]) + r[p[k1]]+r[p[k2]])/2.;
						int dx=x[p[k1]]-x[p[k2]];
						int dy=y[p[k1]]-y[p[k2]];
						if(dx||dy){
							rx=(x[p[k1]] + r[p[k1]]*dx/hypot(dx,dy) +  x[p[k2]] - r[p[k2]]*dx/hypot(dx,dy))/2.;
							ry=(y[p[k1]] + r[p[k1]]*dy/hypot(dx,dy) +  y[p[k2]] - r[p[k2]]*dy/hypot(dx,dy))/2.;
						} else {
							rx=(x[p[k1]] + x[p[k2]])/2.;
							ry=(y[p[k1]] + y[p[k2]])/2.;
						}
					} 
					bool ok=true;
					rep(i,n1){
						double d2=hypot(rx-x[p[i]],ry-y[p[i]])+r[p[i]];
						if(d2>r2+1e-5){ok=false;break;}
					}
					if(ok)checkmin(res,max(r1,r2));
				}
			}

			printf("Case #%d: %.10f\n", testCase, res);		
			cout.flush();
		}
	

	fclose(stdin);
	fclose(stdout);
	return 0;
}
