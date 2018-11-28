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
template<class T> T inside(T r,T c,T R, T C){return r>=0 && r<R && c>=0 && c<C;}

vs a;
int R,C;

bool isDangerous(vpii cur){
	bool res=false;
	vb vis(sz(cur));
	vis[0]=true;
	reps(steps,vis)
		reps(i,vis)if(vis[i]){
			int r1=cur[i].first;
			int c1=cur[i].second;
			reps(j,cur){
				int r2=cur[j].first;
				int c2=cur[j].second;
				if(abs(r1-r2)+abs(c1-c2)==1){
					vis[j]=true;
				}
			}
	}
	reps(i,vis)if(!vis[i])return true;
	return false;
}

bool bad(vpii cur){
	bool res=false;
	vb vis(sz(cur));
	vis[0]=true;
	reps(steps,vis)
		reps(i,vis)if(vis[i]){
			int r1=cur[i].first;
			int c1=cur[i].second;
			reps(j,cur){
				int r2=cur[j].first;
				int c2=cur[j].second;
				if(abs(r1-r2)<=1 && abs(c1-c2)<=1){
					vis[j]=true;
				}
			}
	}
	reps(i,vis)if(!vis[i])return true;
	return false;
}

int main( int argc, char* argv[] ) {	
    //string path = "C:/codejam/A-small-attempt0";
	//string path = "C:/codejam/A-small";
	string path = "C:/codejam/A-large";
	freopen((path+".in").c_str(),"r",stdin);
	freopen((path+".out").c_str(), "w", stdout);

	int testCases;
	cin>>testCases;

	for(int testCase=1;testCase<=testCases;testCase++){
		cin>>R>>C;
		a.assign(R,string());
		vpii start,finish;
		rep(i,R){
			cin>>a[i];
			reps(j,a[i]){
				if(a[i][j]=='o'||a[i][j]=='w')start.pb(mp(i,j));
				if(a[i][j]=='x'||a[i][j]=='w')finish.pb(mp(i,j));
			}
		}

		srt(start);		
		srt(finish);

		queue<vpii> q;
		q.push(start);
		map<vpii,int> m;
		m[start]=0;
		
		int res=-1;

		if(!bad(start))
		while(!q.empty()){
			vpii cur=q.front(); q.pop();
			if(cur==finish){
				res=m[cur];
				break;
			}
			bool dangerous =isDangerous(cur);

			reps(i,cur){
				int r=cur[i].first;
				int c=cur[i].second;
				rep(d,4){
					int nr1=r+dr[d];
					int nc1=c+dc[d];
					int nr2=r-dr[d];
					int nc2=c-dc[d];
					if(inside(nr1,nc1,R,C) && inside(nr2,nc2,R,C) && a[nr1][nc1]!='#' && a[nr2][nc2]!='#' && 
						find(all(cur),mp(nr1,nc1))==cur.end()&&find(all(cur),mp(nr2,nc2))==cur.end()){
						vpii nxt=cur;
						nxt[i].first=nr1;
						nxt[i].second=nc1;
						srt(nxt);
						if(dangerous && isDangerous(nxt))continue;
						if(m.count(nxt))continue;
						m[nxt]=m[cur]+1;
						q.push(nxt);
					}
				}
			}
		}

		cout << "Case #" << testCase << ": " << res << endl;
		cout.flush();
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
