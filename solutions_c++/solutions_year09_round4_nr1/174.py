#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;
typedef long long int64;
int main()
{
freopen("r2\\A-large.in", "r", stdin);
freopen("r2\\A-large.out", "w", stdout);
	int cas;scanf("%d", &cas);
	int case_id = 1;
	int64 arr[64];
	while (cas--)
	{
		int n;scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			char buff[50];
			scanf("%s", buff);
			int64 value = 0;
			for (int j = 0; j < n; ++j) value += (1LL << j) * (buff[j] - '0');
			arr[i] = value;
		}
		int ans = 0;
		for (int i = 0; i < n; ++i)
		{
			int pos = -1;
			for (int j = i; j < n; ++j) if (arr[j] < (1LL<<(i+1))) {pos = j;break;}
			if (pos == -1 || i == pos) continue;
			for (int x = pos; x > i; --x) swap(arr[x], arr[x-1]), ++ans;
		}
		printf("Case #%d: %d\n", case_id++, ans);
	}
	return 0;
}
