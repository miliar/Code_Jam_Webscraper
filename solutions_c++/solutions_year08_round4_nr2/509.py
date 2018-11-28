#include <algorithm>
#include <cstdio>
#include <map>
#include <utility>
#include <iostream>
using namespace std;

int totCase, caseNum;

int prime[5000], cnt;
pair <int, int> sum[5000];

int n, m, s;

map <int, pair <int, int> > node;

bool isPrime(int x) {
	for (int i = 0; i < cnt; ++i)
		if (x % prime[i] == 0)
			return false;
	return true;
}


void init();
void work();
void dfs(int k, int tot, int cur, int sumCnt);
bool cptNum(int k, int sumCnt, pair <int, int> & num, int s1, int s2);

int main() {
	init();
	scanf("%d", &totCase);
	for (caseNum = 1; caseNum <= totCase; ++caseNum) {
		scanf("%d %d %d", &n, &m, &s);
		printf("Case #%d: ", caseNum);
		work();
	}
	return 0;
}

void init() {
	cnt = 0;
	for (int i = 2; i <= 10000; ++i)
		if (isPrime(i)) {
			prime[cnt++] = i;
		}
}

void work() {
	node.clear();
	node[0] = make_pair(0, 0);
	dfs(0, n * m, 1, 0);
	int x1, y1, x2, y2, x3, y3;
	x1 = y1 = -1;
	for (map <int, pair <int, int> >::iterator it = node.begin();
			it != node.end(); ++it) {

		int s1 = it->first, s2 = s1 - s;
		if (s1 >= s && node.find(s2) != node.end()) {
			x1 = 0, y1 = 0;
			x2 = node[s1].first, y3 = node[s1].second;
			y2 = node[s2].first, x3 = node[s2].second;
			break;
		}
	}
	if (x1 == -1)
		printf("IMPOSSIBLE\n");
	else
		printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
}

void dfs(int k, int tot, int cur, int sumCnt) {
	if (k == cnt || tot / cur < prime[k]) {
		if (node.find(cur) != node.end())
			return;
		pair <int, int> num;
		if (cptNum(0, sumCnt, num, 1, 1)) {
			node[cur] = num;
		}
	} else {
		int tmp = 1;
		for (int i = 0; ; ++i) {
			if (tot / tmp >= cur) {
				if (i > 0) {
					sum[sumCnt] = make_pair(prime[k], i);
					dfs(k + 1, tot, cur * tmp, sumCnt + 1);
				} else {
					dfs(k + 1, tot, cur * tmp, sumCnt);
				}
				tmp *= prime[k];
			} else
				break;
		}
	}
}

bool cptNum(int k, int sumCnt, pair <int, int> &num, int s1, int s2) {
	if (k == sumCnt) {
		num = make_pair(s1, s2);
		return true;
	} else {
		int t1 = sum[k].first, t2 = sum[k].second;
		int tmp = 1;
		for (int i = 0; i < t2; ++i) {
			tmp *= t1;
		}
		for (int i = 0, j = 1; i <= t2; ++i, j *= t1) {
			if (s1 * j <= n && tmp / j * s2 <= m) {
				bool flag = cptNum(k + 1, sumCnt, num, s1 * j, tmp / j * s2);
				if (flag)
					return true;
			}
		}
		return false;
	}
}


