#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

int iabs(int n) {
	return n >? -n;
}

int getops(vector<int> & v) {
	int ret = 0;
	for (int i = 1; i < v.size(); ++i) {
		ret += iabs(v[i] - v[i-1]) + 1;
	}
	return ret;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		int n, pos;
		scanf("%d", &n);
		vector<int> qtmp, qname, qops;
		char str[32];
		int last_o_pos;
		int last_b_pos;
		int last_o_time;
		int last_b_time;
		last_o_pos = last_b_pos = 1;
		last_o_time = last_b_time = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%s %d", str, &pos);
			qname.push_back(str[0]);
			qops.push_back(pos);
		}
		int ret = 0;
		for (int i = 0; i < qname.size(); ++i) {
			if (qname[i] == 'O') {
				int time = iabs(qops[i] - last_o_pos) + 1;
				last_o_time = last_b_time + 1 >? time + last_o_time;
				last_o_pos = qops[i];
			} else {
				int time = iabs(qops[i] - last_b_pos) + 1;
				last_b_time = last_o_time + 1>? time + last_b_time;
				last_b_pos = qops[i];
			}
		}
		printf("Case #%d: %d\n", kase + 1, last_b_time >? last_o_time);
	}
	return 0;
}

