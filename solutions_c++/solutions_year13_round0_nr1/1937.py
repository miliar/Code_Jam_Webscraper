#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <iterator>

using namespace std;

#define dump(n) cout<<"# "<<#n<<'='<<(n)<<endl
#define repi(i,a,b) for(int i=int(a);i<int(b);i++)
#define peri(i,a,b) for(int i=int(b);i-->int(a);)
#define rep(i,n) repi(i,0,n)
#define per(i,n) peri(i,0,n)
#define iter(c) __typeof__((c).begin())
#define foreach(i,c) for(iter(c) i=(c).begin();i!=(c).end();++i)
#define all(c) (c).begin(),(c).end()
#define mp make_pair

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int,int> pii;

const int INFTY=1<<29;
const double EPS=1e-9;

template<typename T1,typename T2>
ostream& operator<<(ostream& os,const pair<T1,T2>& p){
	return os<<'('<<p.first<<','<<p.second<<')';
}
template<typename T>
ostream& operator<<(ostream& os,const vector<T>& a){
	os<<'[';
	rep(i,a.size()) os<<(i?" ":"")<<a[i];
	return os<<']';
}

void solve()
{
	vs b(4);
	rep(i,4) cin>>b[i];
	
	int di[]={0,1,1,1};
	int dj[]={1,0,-1,1};
	rep(i,4) rep(j,4) rep(k,4){
		bool fino=true,finx=true;
		rep(l,4){
			int ii=i+l*di[k],jj=j+l*dj[k];
			if(ii<0 || 4<=ii || jj<0 || 4<=jj || b[ii][jj]=='.')
				fino=finx=false;
			else{
				if(b[ii][jj]=='X') fino=false;
				if(b[ii][jj]=='O') finx=false;
			}
		}
		if(fino || finx){
			cout<<(fino?"O won":"X won")<<endl;
			return;
		}
	}
	
	int cnt=0;
	rep(i,4) rep(j,4) cnt+=b[i][j]!='.';
	if(cnt==16) cout<<"Draw"<<endl;
	else        cout<<"Game has not completed"<<endl;
}

int main()
{
	int tc; scanf("%d",&tc);
	rep(i,tc){
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
