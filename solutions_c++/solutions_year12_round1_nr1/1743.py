#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,j,k) for(int i=j;i<(int)(k);++i)
#define foreach(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef long long ll;
const int INF = 99999999;
const double EPS = 1e-9;

int A,B;
int T;

int main()
{
	cin >> T;
	rep(i,T){
		cin >> A >> B;
		int flag=0;
		vector<double> vd(A);
		vector<double> p;
		vector<double> ans(2+A,0);
		rep(j,A) cin >> vd[j];
		while(flag!=(1<<A)){
			double res=1.0;
			rep(j,A){
				if(flag&(1<<j)) res*=(1.0-vd[j]);
				else res*=vd[j];
			}
			p.pb(res);
			++flag;
		}

		rep(j,A+1)rep(k,p.size()){
			flag=k;
			double res=B-A;
			for(int l=A;l>=A-j;--l) flag&=(~(1<<l));
			res+=j*2;
			if(flag!=0) res+=B+1;
			ans[j]+=(double)(res+1)*p[k];
		}

		rep(j,p.size()) ans[ans.size()-1]+=(double)(B+2)*p[j];
		sort(all(ans));
		printf("Case #%d: %.6f\n",i+1,ans[0]);
	}
	
    return 0;
}
