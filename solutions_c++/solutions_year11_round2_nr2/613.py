
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

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcase;
	cin >> testcase;
	for(int tc=1;tc<=testcase;tc++) {
		int C,D;
		cin >> C >> D;
		D*=2;
		vector<int> V;
		double ret = 0;
		REP(i,C) {
			int P,v;
			cin >> P >> v;
			P*=2;
			while(v--) V.PB(P);
		}
		while(1) {
			//check to validate
			bool good = 1;
			REP(i,V.size()-1) {
				if(V[i+1] - V[i] < D) good =0;
			}
			if(good) break;
			for(int i=0;i<V.size();i++) {
				if(i==0) {V[i]--;continue;}
				if(V[i] - V[i-1] > D) V[i]--;
				else if(V[i] - V[i-1] < D) V[i]++;
			}

			ret += 0.5;
		}
		printf("Case #%d: %.1lf\n",tc,ret);
		
	}
}
