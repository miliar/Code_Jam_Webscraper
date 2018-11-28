#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGx(x) cerr << #x << " = " << x << endl;
#define DEBUGxy(x,y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define DEBUGxyz(x,y,z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define MP make_pair
#define ST first
#define ND second

typedef long long LL; typedef pair<int,int > PII;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

LL nums[1024];

int R, K, N;
PII next[1024];
LL  cycleTotal[1024];
int cycleNomor[1024];

// O(n)
// [next_index,sum]
PII calc(int idx) {
	int i = 0;
	int sum = 0;
	while(i<N) {
		int x = (i + idx) % N;
		if(sum + nums[x] > K) break;
		sum += nums[x];
		i++;
	}

	return MP((i + idx) % N,sum);
}

// [start,counter]
inline LL simulate(int start,int counter) {
	int i = start;
	LL currentSum = 0;
	while(counter > 0) {
		PII temp = next[i];
		int ni = temp.ST;
		currentSum += LL(temp.ND);
		i = ni;
		counter--;
	}
	return currentSum;
}

LL solve(int R,int ni,int cycleLen,LL cycleSum) {
	LL ret = 0;
	int cycleStart = cycleNomor[ni];
	ret += simulate(0, min(R,cycleStart) );
	// DEBUGx(ret);
	R -= cycleStart;
	if(R>0) {
		int p = R / cycleLen;
		// DEBUGxy(R,p);
		// DEBUGxy(p,cycleSum*p);
		ret += cycleSum * LL(p);

		R -= (p*cycleLen);


		LL plus = simulate( ni, R );
		// DEBUGxy(R,plus);
		ret += plus;
	}

	return ret;
}

int main() {
	OPEN("C");
	REP(ncase,getint()) {
		R = getint();
		K = getint();
		N = getint();
		REP(i,N) nums[i] = getint();
		REP(i,N) next[i] = calc(i);
		REP(i,N) {
			cycleNomor[i] = -1;
			cycleTotal[i] = 0;
		}


		int i = 0;
		int currentNomor = 0;
		cycleNomor[i] = currentNomor++;

		LL currentSum = 0;
		while(1) {
			PII temp = next[i];
			int ni = temp.ST;
			currentSum += LL(temp.ND);
			if(cycleNomor[ni]!=-1) {

				int cycleStart = cycleNomor[ni];
				int cycleLen = currentNomor - cycleNomor[ni];
				LL cycleSum = currentSum - cycleTotal[ni];
				// DEBUGxyz(cycleStart,cycleLen,cycleSum);
				LL ans = solve(R,ni,cycleLen,cycleSum);
				printf("Case #%d: %I64d\n",ncase+1,ans);
				break;
			}else {
				cycleNomor[ni] = currentNomor;
				cycleTotal[ni] = currentSum;
				currentNomor++;

			}
			i = ni;
		}


		// REP(i,N) printf("%d %d %d\n",i, next[i].ST,next[i].ND);
		// puts("");
	}
	return 0;
}
