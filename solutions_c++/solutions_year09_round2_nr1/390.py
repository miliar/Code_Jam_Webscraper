#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
using namespace std;
set<string> features;
string description;
char lined[100];
char name[50];

int tc, n, m;
double res;

void find(const string& a, double& value, string& key, string& left, string& right) {
	int pos = 0;
	while (a[pos] == ' ' || a[pos] == '\n' || a[pos] == '(') {
		pos ++;
	}
	value = 0;
	double base = 1.0;
	bool flag = false;
	while ((a[pos] >= '0' && a[pos] <= '9') || a[pos] == '.') {
		if (a[pos] == '.') {
			pos ++;
			continue;
		}
		if (!flag) {
			value = a[pos] - '0';
			flag = true;
			pos ++;
			continue;
		}
		if (flag) {
			base *= 0.1;
			value += base * (a[pos] - '0');
			pos ++;
			continue;
		}
	}
	while (a[pos] == ' ' || a[pos] == '\n') {
		pos ++;
	}
	if (a[pos] == ')') {
		key = "";
		left = "";
		right = "";
		return;
	}
	key = "";
	while (a[pos] >= 'a' && a[pos] <= 'z') {
		key += a[pos];
		pos ++;
	}
	while (a[pos] == ' ' || a[pos] == '\n') {
		pos ++;
	}
	left = "";
	int deep = 1;
	while (deep) {
		left += a[pos];
		pos ++;
		if (a[pos] == '(') deep ++;
		if (a[pos] == ')') deep --;
	}
	left += a[pos ++];
	while (a[pos] == ' ' || a[pos] == '\n') {
		pos ++;
	}
	right = "";
	deep = 1;
	while (deep) {
		right += a[pos];
		pos ++;
		if (a[pos] == '(') deep ++;
		if (a[pos] == ')') deep --;
	}
	right += a[pos ++];
}

void check(const string& stat) {
	double value;
	string key, left, right;
	find(stat, value, key, left, right);
	res *= value;
	if (key.length() == 0) {
		return;
	} else {
		if (features.count(key)) {
			check(left);
		} else {
			check(right);
		}
	}
};

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &tc);
	for (int t = 0; t < tc; t ++) {
		printf("Case #%d:\n", t + 1);
		description.clear();
		scanf("%d\n", &n);
		for (int i = 0; i < n; i ++) {
			gets(lined);
			description.append(lined);
		}
		scanf("%d\n", &m);
		for (int i = 0; i < m; i ++) {
			scanf("%s ", name);
			features.clear();
			int k;
			scanf("%d ", &k);
			string fea;
			for (int j = 0; j < k; j ++) {
				scanf("%s", name);
				fea.clear();
				fea.append(name);
				features.insert(fea);
			}
			res = 1.0;
			check(description);
			printf("%.7lf\n", res);
		}
		//printf("%s\n", description.c_str());
	}
	return 0;
}
