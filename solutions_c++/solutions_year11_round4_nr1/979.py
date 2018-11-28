
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;

int dist[1000001];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcase;
	cin >> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int X,S,R,N;
		double T;
		double result = 0;
		cin >> X >> S >> R >> T >>N;
		int wsum = 0;
		memset(dist,0,sizeof dist);
		REP(i,N) {
			int B,E,W;
			cin >> B >> E >> W;
			dist[W] += E-B;
			wsum += E-B;
		}
		dist[0] += X - wsum;
		REP(i,1000001) {
			if(dist[i]==0)continue;
			double v;
			if(T<=0) v = S+i;
			else v = R+i;
			double t = dist[i] / v;
			if(T>=t) {
				result += t;
				T -= t;
			}
			else {
				t = T;
				double moved = t * v;
				double notmoved = dist[i]-moved;
				double slowtime = notmoved / (S+i);
				result += t + slowtime;
				T -= t;
			}
		}

		printf("Case #%d: %.9lf\n",tc,result);

	}
}
