#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

LL N, M, A;

LL area(LL x1, LL y1, LL x2, LL y2, LL x3, LL y3)
{
	x3 -= x1;
	y3 -= y1;
	x2 -= x1;
	y2 -= y1;

	LL ans = x3*y2 - x2*y3;
	return ans < 0 ? -ans : ans;
}

LL x1, y1, x2, y2, x3, y3;


int main(void)
{
	int C;
	cin >> C;
	for (int i=1; i<=C; ++i) {
		cin >> N >> M >> A;

		bool succ = false;
		x1 = 0;
		y1 = 0;
		for (x2=0; x2<=N; ++x2) for (y2=0; y2<=M; ++y2)
		for (x3=0; x3<=N; ++x3) for (y3=0; y3<=M; ++y3) {
			if (area(0, 0, x2, y2, x3, y3) == A) {
				succ = true;
				goto end;
			}
		}

		x1 = 0;
		y2 = 0;
		for (y1=0; y1<=M; ++y1) 
		for (x2=0; x2<=N; ++x2)
		for (x3=0; x3<=N; ++x3) for (y3=0; y3<=M; ++y3) {
			if (area(0, y1, x2, 0, x3, y3) == A) {
				succ = true;
				goto end;
			}
		}

end:
		cout << "Case #" << i << ": ";

		if (!succ) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
		}
	}

	return 0;
}
