//      hello world


//DS includes
#include<bitset>
#include<complex>
#include<deque>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

//Other Includes
#include<algorithm>
#include<cassert>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<sstream>

#define oo 			0xBADC0DE
#define s(n)			scanf("%d",&n)
#define sl(n) 			scanf("%lld",&n)
#define sf(n) 			scanf("%lf",&n)
#define fill(a,v) 		memset(a, v, sizeof a)
#define ull 			unsigned long long
#define ll 				long long
#define bitcount 		__builtin_popcount
#define all(x) 			x.begin(), x.end()
#define pb( z ) 		push_back( z )
#define gcd				__gcd

#define FOR(i,n) for (int i=0; i < (n); i++)

using namespace std;

int main(int argc, char** argv) {
	//freopen("ip.txt", "r", stdin); 
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	//freopen("C-small-attempt3.in", "r", stdin); freopen("C-small-attempt3.out", "w", stdout);
	
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int runs; cin>>runs;
	for (int T=1; T <= runs; T++) {
		printf("Case #%d: ", T);
		int N; cin>>N;
		vector<int> a( N );
		int allXor = 0;
		int allSum = 0;
		int minVal = (int)1e9;
		for (int i=0; i < N; i++) {
			cin>>a[i];
			minVal = min(minVal, a[i]);
			allSum += a[i];
			allXor ^= a[i]; 
		}
		if (allXor) {
			puts("NO");
		} else {
			printf("%d\n", allSum-minVal);
		}
	}
	return 0;
}
