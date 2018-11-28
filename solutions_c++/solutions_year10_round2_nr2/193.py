#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int num, aim, dis, time;
		scanf("%d%d%d%d", &num, &aim, &dis, &time);
		vector<int> pos(num), speed(num);
		for (int i = 0; i < num; i++) {
			scanf("%d", &pos[i]);
		}
		for (int i = 0; i < num; i++) {
			scanf("%d", &speed[i]);
		}
		printf("Case #%d: ", caseIndex);
		if (aim == 0) {
			puts("0");
			continue;
		}
		int ans = 0;
		int cur = 0;
		int cnt = 0;
		for (int i = num - 1; i >= 0 && cur < aim; i--) {
			if (pos[i] + speed[i] * time >= dis) {
				ans += cnt;
				cur++;
			} else {
				cnt++;
			}
		}
		if (cur == aim) {
			printf("%d\n", ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
