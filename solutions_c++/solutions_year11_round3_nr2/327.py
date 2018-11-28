#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) (a.begin(),a.end())
#define rall(a) (a.rbegin(),a.rend())
#define INF (int)1e9
#define EPS (double)1e-9

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef pair< int, ii > pi;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

LL dist[1010];
int ocount[1010];

struct elem {
	LL value;
	int idx;
};

bool cmp(elem a, elem b) {
	return a.value > b.value;
}

int main() {
	int T = GI;
	FOR(z,1,T+1) {
		LL L = GL, t = GL, N = GL, C = GL, total = 0, rtotal = 0;
		LL quo = N/C, rem = N%C;
		REP(i,C) {
			dist[i] = GL;
			total += dist[i];
			if (i < rem) rtotal += dist[i];
		}

		LL tans = 2*(quo*total + rtotal);
		LL bsum = (t/(2*total))*total;
		int bpt = -1;
		LL bdiff = 0;
		if (bsum > tans/2) bsum = 0, bpt = C-1;
		else
		REP(i,C) {
			if (i == C-1 || bsum + dist[i] > t/2) {
				bpt = i;
				bdiff = max(0LL, bsum+dist[i]-t/2);
				break;
			}
			bsum += dist[i];
		}

/*		int bpt = -1;
		LL bdiff = 0, bsum = 0;
		REP(i,N) {
			if (i == N-1 || bsum + fdist[i] > t/2) {
				bpt = i;
				bdiff = max(0LL, bsum+fdist[i]-t/2);
				break;
			}
			bsum += fdist[i];
		}
*/

	//	cout << "tans = " << tans << endl;
	//	cout << "bpt = " << bpt << " bsum = " << bsum << " bdiff = " << bdiff << endl;

	//	cout << "quo = " << quo << "   " << (t/(2*total)) << endl;		

		REP(i,C) {
			ocount[i] = max(0LL, (tans/(2*total)) - (t/(2*total) + 1));
			if (i < rem) ocount[i]++;
		}
		FOR(i,bpt+1,C) {
			ocount[i]++;	
		}

	//	REP(i,C) {
	//		cout << "count " << i << " = " << ocount[i] << endl;
	//	}

		vector<elem> subdist(C);
		REP(i,C) {
			subdist[i].value = dist[i];
			subdist[i].idx = i;
		}

		sort(subdist.begin(), subdist.end(), cmp);

//		REP(i,sz) cout << "subdist = " << subdist[i] << endl;

		REP(i,C) {
			if (L == 0) break;

			if (bdiff > subdist[i].value) {
				tans -= bdiff;
				L--;
				bdiff = 0;
			}			

			int cnt = min(L, (LL)ocount[subdist[i].idx]);
			tans -= cnt*subdist[i].value;
			L -= cnt;
		}

		cout << "Case #" << z << ": " << tans << endl;
	}		
	return 0;
}
