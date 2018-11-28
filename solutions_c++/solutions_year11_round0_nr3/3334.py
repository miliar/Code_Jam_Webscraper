#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

int m[1001];
int N;

int read(){
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		scanf("%d", &m[i]);
	}
	return 1;
}

int mask[1<<16], total[1<<16];

void process(){
	mask[0] = 0;
	for(int i = 1; i < (1<<N); i++){
		mask[i] = 0;
		total[i] = 0;
		for(int j = 0; j < N; j++)if((i>>j)&1){
			mask[i] ^= m[j];
			total[i] += m[j];
		}
	}
	int full = (1<<N)-1;
	int maxi = -1;
	for(int i = 1; i < full; i++){
		//printf("i(%d) (%d, %d)\n", i, mask[i], total[i]);
		if(mask[i] == mask[full-i]){
			maxi = max(maxi, max(total[i], total[full-i]));
		}
	}
	if(maxi == -1){
		printf("NO\n");
	}else printf("%d\n", maxi);
}

// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
