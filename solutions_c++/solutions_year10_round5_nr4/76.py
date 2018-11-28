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

int base, aim;
bool mat[10][10];
int ans;

void search(int cur, int from) {
	if (cur == aim) {
		ans++;
	}
	for (; from + cur <= aim; from++) {
		vector<int> vec;
		int num = from;
		while (num) {
			vec.push_back(num % base);
			num /= base;
		}
		bool isOk = true;
		for (int i = 0; i < vec.size(); i++) {
			if (mat[i][vec[i]]) {
				isOk = false;
				break;
			}
		}
		if (isOk) {
			for (int i = 0; i < vec.size(); i++) {
				mat[i][vec[i]] = true;
			}
			search(cur + from, from + 1);
			for (int i = 0; i < vec.size(); i++) {
				mat[i][vec[i]] = false;
			}
		}
	}
}

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		scanf("%d%d", &aim, &base);
		ans = 0;
		memset(mat, false, sizeof(mat));
		search(0, 1);
		printf("Case #%d: %d\n", caseIndex, ans);
	}
	return 0;
}
