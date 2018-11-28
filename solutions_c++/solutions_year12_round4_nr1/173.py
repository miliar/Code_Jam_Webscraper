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

using namespace std;

const int MAX_N = 100000 + 10;
int N, D;
int d[MAX_N], l[MAX_N], f[MAX_N];

void solve()
{
	scanf("%d", &N);
	for(int i = 0; i < N; ++ i) {
		scanf("%d%d", &d[i], &l[i]);
		f[i] = -1;
	}
	scanf("%d", &D);
	f[0] = d[0];
	int cur = 1, flag = 0;
	for(int i = 0; i < N; ++ i) {
		if (f[i] < 0) continue;
		f[i] = min(f[i], l[i]);
		if (d[i] + f[i] >= D) {
			flag = true;
			break;
		}
		for( ; cur < N && d[i] + f[i] >= d[cur]; ++ cur)
			f[cur] = d[cur] - d[i];
	}
	if (flag)
		puts("YES");
	else
		puts("NO");
}

int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		solve();
	}
	return 0;
}
