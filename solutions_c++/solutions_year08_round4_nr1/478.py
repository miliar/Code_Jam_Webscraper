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

inline int LEFT(int x) { return 2*x; }
inline int RIGHT(int x) { return 2*x+1; }

const int inf = 10010;

int N;
int M, V;
int changeable[10010];
int isand[10010];
int value[10010];

int cache[10010][2];

int solve(int pos, int val)
{
	if (pos >= (M-1)/2+1) {
		if (value[pos] == val)
			return 0;
		return 1234567;
	}
	int &res = cache[pos][val];
	if (res != -1)
		return res;
	res = 12345678;
	if (val == 0) {
		if (isand[pos]) {
			min2(res, min(solve(LEFT(pos),0),solve(RIGHT(pos),0)));
		} else {
			min2(res, solve(LEFT(pos),0)+solve(RIGHT(pos),0));
		}

		if (changeable[pos]) {
			if (isand[pos]) {
				min2(res, 1+solve(LEFT(pos),0)+solve(RIGHT(pos),0));
			} else {
				min2(res, 1+min(solve(LEFT(pos),0),solve(RIGHT(pos),0)));
			}
		}
	} else {
		if (isand[pos]) {
			min2(res, solve(LEFT(pos),1)+solve(RIGHT(pos),1));
		} else {
			min2(res, min(solve(LEFT(pos),1),solve(RIGHT(pos),1)));
		}

		if (changeable[pos]) {
			if (isand[pos]) {
				min2(res, 1+min(solve(LEFT(pos),1),solve(RIGHT(pos),1)));
			} else {
				min2(res, 1+solve(LEFT(pos),1)+solve(RIGHT(pos),1));
			}
		}
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d %d", &M, &V);
		for (int i = 1; i <= (M-1)/2; ++i) {
			scanf("%d %d", &isand[i], &changeable[i]);
		}
		for (int i = (M-1)/2+1; i <= M; ++i) {
			scanf("%d", &value[i]);
		}

		memset(cache, -1, sizeof cache);
		int res = solve(1,V);
		if (res < inf)
			printf("Case #%d: %d\n", tt, solve(1,V));
		else
			printf("Case #%d: IMPOSSIBLE\n", tt);
	}

	return 0;
}
