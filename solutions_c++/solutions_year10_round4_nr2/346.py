using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e9
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;



int mem[100000][20], p, m[2000], mm[100000], k[20][2000], wt[100000], next, lastStart;

int go(int cur, int extra) {
	int &res = mem[cur][extra];
	if(res != -1) return res;	
	res = INF;

	if(cur >= lastStart) {

		if(extra >= m[cur]) {
//		cout << "m["<<cur<<"] is " << m[cur]<<endl;
//cout << cur << " " << extra << " returns with "<< 0 << endl;		
			return res = 0;
		}
		return res = INF;
	}
	
	int left = 2*cur+1, right = 2*cur+2;

	int cand1 = wt[cur] + go(left, extra+1);
	if(cand1 < INF) cand1 += go(right,extra+1);

	int cand2 = go(left, extra);
	if(cand2 < INF) cand2 += go(right,extra);

//cout << cur << " " << extra << " returns with "<< min(cand1,cand2) << endl;
	return res = min(cand1, cand2);

}
int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		memset(mem,-1,sizeof(mem));
		p = GI;		
		int power = 1<<p;
		REP(i,power) {
			mm[i] = GI;
			mm[i] = p - mm[i];
		}
		int st = (1<<p)/2;
		REP(i,p) {
			REP(j,st) k[i][j] = GI;
			st /= 2;
		}
		next=0; st = 1;
		for(int i = p-1; i>= 0; i--) {
			for(int j = 0; j < st; j++) {
				wt[next++] = k[i][j];
			}
			lastStart = next;			
			st *= 2;
		}
		REP(i,power) m[lastStart+i] = mm[i];
	//	cout << lastStart << endl; continue;
		//continue;

		 int g = go(0,0);
	  	 printf("Case #%d: %d\n", kase, g);
	}
}
