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

int N;
int NA, NB;
int T;

// 0 - a train becomes free at A
// 1 - a train becomes free at B
// 2 - a train starts from A
// 3 - a train starts from B
pair<int,int> events[1024]; // the first int is the time
int E;

int main()
{
	scanf("%d", &N);
	for (int nn = 0; nn < N; ++nn) {
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		E = 0;
		int a, b;
		int h, m;
		for (int i = 0; i < NA; ++i) {
			scanf("%d:%d", &h, &m);
			a = h*60 + m;
			scanf("%d:%d", &h, &m);
			b = h*60 + m;
			events[E++] = MP(a, 2);
			events[E++] = MP(b+T, 1);
		}

		for (int i = 0; i < NB; ++i) {
			scanf("%d:%d", &h, &m);
			b = h*60 + m;
			scanf("%d:%d", &h, &m);
			a = h*60 + m;
			events[E++] = MP(b, 3);
			events[E++] = MP(a+T, 0);
		}

		sort(events, events+E);
		int needA = 0, needB = 0;
		int haveA = 0, haveB = 0;
		for (int i = 0; i < E; ++i) {
			switch (events[i].second) {
			case 0: haveA += 1; break;
			case 1: haveB += 1; break;
			case 2: haveA -= 1; break;
			case 3: haveB -= 1; break;
			}

			if (haveA < 0) {
				haveA = 0;
				needA += 1;
			} else if (haveB < 0) {
				haveB = 0;
				needB += 1;
			}
		}
		printf("Case #%d: %d %d\n", nn+1, needA, needB);
	}
	return 0;
}
