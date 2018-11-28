#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int card[5100];

queue<int> Q;

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		int K;
		scanf("%d", &K);
		memset(card, 0, sizeof card);
		for (int i = 1; i <= K; ++i)
			Q.push(i);

		for (int kk = 0; kk < K; ++kk) {
			for (int c = 0; c < kk; ++c) {
				int curpos = Q.front();
				Q.pop();
				Q.push(curpos);
			}
			int curpos = Q.front();
			Q.pop();
			card[curpos] = kk+1;
		}

		int n, di;
		scanf("%d", &n);
		printf("Case #%d:", tt);
		while (n--) {
			scanf("%d", &di);
			printf(" %d", card[di]);
		}
		puts("");
	}

	return 0;
}
