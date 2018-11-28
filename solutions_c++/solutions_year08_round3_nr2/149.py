#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <cmath>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int mask[15], ans, len;
char s[15];

LL get(char *ss) {
	for (int i = 0; ss[i]; ++i) {
		if (ss[i] == '+') {
			ss[i] = 0;
			return get(ss)+get(ss+i+1);
		}
		else if (ss[i] == '-') {
			ss[i] = 0;
			return get(ss)-get(ss+i+1);
		}
	}
	LL ret;
	sscanf(ss, "%lld", &ret);
	return ret;
}
void go(int ind) {
	if (ind == len-1) {
		char tmp[30];
		int l = 0;
		tmp[l++] = s[0];
		for (int i = 0; i < len-1; ++i) {
			if (mask[i] == 0) tmp[l++] = s[i+1];
			else if (mask[i] == 1) {
				tmp[l++] = '+';
				tmp[l++] = s[i+1];
			}
			else {
				tmp[l++] = '-';
				tmp[l++] = s[i+1];
			}
		}
		tmp[l] = 0;
		LL sum = get(tmp);
		if ( sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0 )
			ans++;
		return;
	}
	for (int i = 0; i < 3; ++i) {
		mask[ind] = i;
		go(ind+1);
	}
}
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	int N;

	scanf("%d", &N);
	for (int cas = 1; cas <= N; ++cas) {
		scanf("%s", s);
		len = strlen(s);
		ans = 0;
		go(0);
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}

