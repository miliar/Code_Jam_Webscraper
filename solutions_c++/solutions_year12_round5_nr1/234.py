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

#define PB push_back
#define MP make_pair
#define foreach(e,x) for(typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

using namespace std;

const int MAX_N = 1000 + 10;
int N;
int l[MAX_N], p[MAX_N], order[MAX_N];

int cmp(const int &a, const int &b)
{
	if (p[a] != p[b])
		return p[a] > p[b];
	if (l[a] != l[b])
		return l[a] < l[b];
	return a < b;
}

void solve()
{
	scanf("%d", &N);
	for(int i = 0; i < N; ++ i)
		scanf("%d", &l[i]);
	for(int i = 0; i < N; ++ i) {
		scanf("%d", &p[i]);
		order[i] = i;
	}
	sort(order, order + N, cmp);
	for(int i = 0; i < N; ++ i)
		printf("%d ", order[i]);
	puts("");
}

int main()
{
//	freopen("A.in","r",stdin);
	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		solve();
	}
	return 0;
}
