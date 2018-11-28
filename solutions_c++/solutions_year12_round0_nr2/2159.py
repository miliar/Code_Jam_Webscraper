#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int n,N;

class Triplet{
public:
	int T, normal, surprising;


	void calc()
	{
		normal = T/3 + (T%3 != 0);
		surprising = T/3 + (T > 0) + (T%3 == 2);
	}
};

//#define SMALL
#define LARGE
int main() {
//	freopen("B.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	int S,P;
	cin >> N;

	for(int nn = 1 ; nn <= N ; nn++ ) {
		cin >> n >> S >> P;
		vector<Triplet>googlers(n);
		for (int i = 0; i < n; ++i) {
			cin >> googlers[i].T ;
			googlers[i].calc();
		}
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			if(googlers[i].normal >= P)
				cnt++;
			else
			{
				if(S && googlers[i].surprising >= P)
				{
					cnt++;
					S--;
				}
			}
		}
		printf("Case #%d: %d\n", nn, cnt);
	}
	return 0;
}
