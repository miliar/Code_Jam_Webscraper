#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;
#define FOR(i,a,n) for(int i = a; i < n; i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back


int main() {
	int n;
	cin >> n;
	REP(i,n) {
		int m;
		cin >> m;
		vector<int> but[2];
		vector <int> order;
		REP(j,m) {
			char c;
			int b;
			cin >> c >> b;
			but[(c == 'O')?0:1].pb(b);
			order.pb((c=='O')?0:1);
			
		}
		
		int ans = 0, posi[2] = {1,1}, p[2] = {0,0};
		REP(j,m) {
			int cur = order[j], pos = posi[cur], nextbut = but[cur][p[cur]];
			int timeneeded = abs(nextbut - pos) + 1;			
			posi[cur] = nextbut;

			if(p[1-cur] < but[1-cur].size()) {
				int opp = 1-cur, opp_nextbut = but[opp][p[opp]];
				if(timeneeded >= abs(opp_nextbut - posi[opp]) + 1) {
					posi[opp] = opp_nextbut;
				}
				else {
					if(opp_nextbut > posi[opp]) {
						posi[opp] += timeneeded;
					}
					else {
						posi[opp] -= timeneeded;				
					}				
				}
			}
			ans += timeneeded;
			p[cur]++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
}			

		
		

