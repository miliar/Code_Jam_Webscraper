#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>
 
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

int main() {
	int test; scanf("%d",&test); REP(tt,test) {
		int n;
		scanf("%d",&n);
		vector<string> V;
		vector<double> res;
		vector<double> ano;
		string str;
		REP(i,n) { cin >> str; V.pb(str); }
		double oowp = 0;
		REP(i,n) {
			double wp,owp;
			int won = 0,tot = 0;
			REP(j,n) {
				if(V[i][j] != '.') tot++;
				if(V[i][j] == '1') won++;
			}
			wp = double(won)/double(tot);
			//dbg(wp);
			double owpavg = 0;
			int cnt = 0;
			REP(j,n) {
				won = 0, tot = 0;
				if(j == i) continue;
				if(V[i][j] == '.') continue;
			       	REP(k,n) {
					if(k == i) continue;
					if(V[j][k] != '.') tot++;
					if(V[j][k] == '1') won++;
				}
				cnt++;
				owpavg += double(won)/double(tot);
			}
			owpavg /= double(cnt);
			//dbg(owpavg);
			ano.pb(owpavg);
			res.pb(0.25 * wp + 0.50 * owpavg);
		}
		//REP(i,n) cout << res[i] << " ";
		//cout << endl;
		
		REP(i,n) {
			double ans = 0;
			int cnt = 0;
			REP(j,n) {
				if(j == i) continue;
				if(V[i][j] == '.') continue;
				ans += ano[j];
				cnt++;
			}
			ans /= double(cnt);
			res[i] += 0.25 * ans;
		}
		printf("Case #%d:\n",tt+1);
		REP(i,n) printf("%.20lf\n",res[i]);//cout << res[i] << endl;
	}
}

