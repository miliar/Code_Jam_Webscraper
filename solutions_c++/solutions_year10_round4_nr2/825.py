#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int caseT;
int n;
int tt = 1;
int m[3000], val;
vector<int> t[2000];
int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &caseT);
	while(caseT--) {
		scanf("%d", &n);
		for(int i = 0; i < (1<<n); ++i) {
			scanf("%d", &m[i]);
		}
		for(int i = n - 1; i >= 0; --i) {
			t[i].clear();
			for(int j = 0; j < (1<<i); ++j) {
				t[i].push_back(0);
				scanf("%d", &val);
			}
		}
		for(int i = 0; i < (1<<n); ++i) {
			int T = n - m[i];
			int s = i;
			vector<int> tmp;
			for(int j = 0; j < n; ++j) {
				tmp.push_back(s/2);
				s /= 2;
			}
			for(int j = 0; j < T; ++j) {
				t[j][tmp[tmp.size() - 1 - j]] = 1;
			}
		}
		int vals = 0;
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < t[i].size(); ++j) {
				if(t[i][j] == 1) {
					++vals;
				}
			}
		}
		printf("Case #%d: ", tt++);
		printf("%d\n", vals * val);
	}
	return 0;
}