#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;


int main(void)
{
	int testcase;
	scanf("%d", &testcase);
	for (int case_id=1; case_id<=testcase; case_id++) {
		int N, S, p;
		int i, ok = 0, oks = 0;
		scanf("%d %d %d", &N, &S, &p);
		for (i=0; i<N; i++){
			int t;
			scanf("%d", &t);
			if (t<=30 && t>=p+2*MAX(p-1,0)) ok++;
			else if (t<=30 && t>=p+2*MAX(p-2,0)) oks++;
		}
		printf("Case #%i: %i\n", case_id, ok + MIN(S, oks));
	}
	return 0;
}
