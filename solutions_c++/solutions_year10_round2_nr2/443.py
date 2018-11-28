

#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <vector>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i = a; i <b ; i++)
#define FRR(i,a,b) for(int i = b - 1; i >=a ; i--)
#define sz size()
#define pb push_back
#define VI vector<int>
#define VVI vector<VI>
#define eps 1e-9
#define INF 100000000
#define mp make_pair()
#define ll long long int
#define SS stringstream

int go(int k, int t, VI x, VI v){
	int n = x.sz;
	VI willreach;
	int rem = k;
	int ret = 0;
	FOR(i,0,n){
		if(willreach.sz >= k)break;
		bool reach = v[i]*t >= x[i];
		FOR(j,0,willreach.sz){
			int k = willreach[j];
			reach = reach | (t*(v[i] - v[k]) >= x[i] - x[k]);
		}
		if(reach){
			willreach.pb(i);
			rem--;
		}
		else ret+=rem;
	}
	return willreach.sz >= k?ret:INF;
}


int main(){
	int cases;
	cin >> cases;
	FOR(caseNum, 0, cases){
		int n,k,t; 
		ll b;
		cin >> n >> k >> b >> t;
		VI x(n,0),v(n,0);
		int tmp;
		FRR(i,0,n){
			cin >> tmp; tmp = b-tmp; x[i] = tmp;
		}
		FRR(i,0,n){
			cin >> tmp; v[i] = tmp;
		}
		int ans = go(k, t, x, v);
		cout << "Case #" << caseNum+1 << ": ";
		if(ans >= INF) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
	
}