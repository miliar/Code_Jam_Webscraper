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
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N;
int mx[100];

int main()
{
	int TT;
	scanf("%d", &TT);
	for (int TC = 1; TC <= TT; ++TC) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			mx[i] = 0;
			char line[100];
			scanf("%s", line);
			for (int j = 0; j < N; ++j) {
				if (line[j] == '1')
					mx[i] = j;
			}
		}

		int swaps = 0;
		for (int i = 0; i < N; ++i) {
			if (mx[i] <= i)
				continue;
			int j;
			for (j = i+1; j < N && mx[j] > i; ++j)
				;
			assert(j != N);
			for (; j != i; --j) {
				swap(mx[j-1], mx[j]);
				swaps += 1;
			}
		}
		printf("Case #%d: %d\n", TC, swaps);
	}
	
	return 0;
}
