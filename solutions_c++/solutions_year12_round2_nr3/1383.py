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

int T,N;

int main()
{
	cin >> T;
	rep(t,T){
		cin >> N;
		vi S(N);
		map<ll,int> m;
		rep(i,N) cin >> S[i];
		int flag=1;
		bool b=false;
		while(flag!=(1<<N)){
			ll res=0;
			rep(i,N)if(flag&(1<<i)) res+=S[i];
			if(m.find(res)==m.end()) m.insert(mp(res,flag));
			else{
				int f=m[res];
				vi ans1,ans2;
				cout << "Case #" << t+1 << ":" << endl;
				rep(j,N)if(f&(1<<j)) ans1.pb(S[j]);
				rep(j,N)if(flag&(1<<j)) ans2.pb(S[j]);
				rep(j,ans1.size()) printf("%d%c",ans1[j],j!=(int)ans1.size()-1?' ':'\n');
				rep(j,ans2.size()) printf("%d%c",ans2[j],j!=(int)ans2.size()-1?' ':'\n');
				b=true;
				break;
			}
			flag++;
		}
		if(!b) cout << "Case #" << t+1 << ":" << endl << "Impossible" << endl;
	}
	return 0;
}
