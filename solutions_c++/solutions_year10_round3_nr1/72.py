#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define REP(i,n) for(int i=0;i<n;++i)
#define SZ(v) (int)(v.size())
#define PB push_back
#define MP make_pair
#define CL(v,x) memset(v,x,sizeof(v))

int A[1001], B[1001];
int N;

int main(){
	FILE* fin=freopen("input.in", "r", stdin);
	int T;
	scanf("%d\n", &T);

	for (int t=0;t<T;++t) {
		scanf("%d", &N);
		REP(i, N) scanf("%d%d", &A[i], &B[i]);
		int ret=0;
		REP(i,N) REP(j,N) if (j!=i)
			if ((A[i]<A[j])&&(B[i]>B[j])) ret++;
		printf("Case #%d: %d\n", t+1, ret);
	}

	return 0;
}
