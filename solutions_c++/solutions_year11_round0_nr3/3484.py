#include  <stdio.h>
#include <string>
#include <cmath>
#include <vector>
#include <cstdlib>

using namespace std;

#define PB push_back
#define ST first
#define ND second
#define ALL(v) v.begin(),v.end()
#define RALL(v) v.rbegin(),v.rend()
#define SZ size()
#define FOR(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define REP(i,m) for(int i=0;i<(int)(m);i++)
#define REP2(i,n,m) for(int i=n;i<(int)(m);i++)
#define MP make_pair

void print_result(int x, int y) {
	printf("Case #%d: %d\n", x, y);
}

int main(){
	int T, N;
	scanf ("%d", &T);
	int i, j, pos;
	int sum;
	int nsum = 0;
	int mn;
	for(i=1; i<=T; i++){
		vector<int> v;
		scanf("%d",  &N);
		sum = 0;
		nsum = 0;
		mn = 10e6+1;
		for(j=0; j<N; j++){
			scanf("%d", &pos);
			v.push_back(pos);
			sum = sum xor pos; 
			nsum += pos;
			mn = min(mn, pos);
		}
		if(sum != 0)
			printf("Case #%d: %s\n", i, "NO");
		else
			printf("Case #%d: %d\n", i, nsum-mn);
	}
	return 0;
}
