#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <ctime>
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const int MAX_D = 5000;
const int MAX_L = 15;
const int MAX_N = 500;
const int MAX_LEN = 28 * 15;

int n, d, l;
char word[MAX_D][MAX_L + 1];
char buf[MAX_LEN];
bool flag[MAX_D];
bool accepted[26];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	for (int i = 0; i < d; i++)
		scanf("%s", word[i]);
	for (int i = 0; i < n; i++)
	{
		scanf("%s", buf);
		char* p = buf;
		fill(flag, flag + d, true);
		for (int j = 0; j < l; j++, p++)
		{
			fill(accepted, accepted + 26, false);
			if (*p == '(')
			{
				for (++p; *p != ')'; ++p)
					accepted[*p - 'a'] = true;
			}
			else 
				accepted[*p - 'a'] = true;
			for (int k = 0; k < d; k++)
				flag[k] &= accepted[word[k][j] - 'a'];
		}
		printf("Case #%d: %d\n", i + 1, count(flag, flag + d, true));
	}
	return 0;
}
