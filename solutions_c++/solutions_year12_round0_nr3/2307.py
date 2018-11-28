//============================================================================
// Name        : Qua-C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <algorithm>
#include <stdio.h>
using std::sort;
int id[2100000];
int sequence[2100000][8];
int nid;

int length(int x) {
	int s = 0;
	while (x) {
		s++;
		x /= 10;
	}
	return s;
}
void process(int x, int l) {
	int mod = 10;
	int c = 1;
	int len = 1;
	sequence[nid][len] = x;
	for (int i = 1; i < l; ++i)
		c *= 10;
	for (int i = 1; i < l; ++i) {
		int left = (x / mod);
		int right = (x % mod);
		int next = left + right * c;

		if (next <= 2000000 && length(next) == l) {
			int j;
			for (j = 1; j <= len; ++j)
				if (sequence[nid][j] == next)
					break;
			if (j == len + 1) {
				len++;
				sequence[nid][len] = next;
				id[next] = nid;
			}
		}
		mod *= 10;
		c /= 10;
	}
	sequence[nid][0] = len;
	std::sort(sequence[nid] + 1, sequence[nid] + len + 1);
}
void print(int xid) {
	printf("%d: length:%d\n", xid, sequence[xid][0]);
	for (int i = 1; i <= sequence[xid][0]; ++i)
		printf("%d ", sequence[xid][i]);
	printf("\n");
}
void init() {
	int x, l;
	nid = 0;
	for (x = 1; x <= 2000000; ++x) {
		if (id[x] == 0) {
			l = length(x);
			nid++;
			process(x, l);
			id[x] = nid;
		}
	}

}
int count(int x, int a, int b) {
	int xid = id[x];
	int len = sequence[xid][0];
	int i, j;
	for (i = 1; i <= len; ++i)
		if (sequence[xid][i] == x)
			break;
	for (j = i + 1; j <= len; ++j)
		if (sequence[xid][j] > b)
			break;
	return j - i - 1;
}
int main() {
	init();
	freopen("/home/panda/program/input", "r", stdin);
	freopen("/home/panda/program/output", "w", stdout);
	int nc, c;
	int a, b, ans;
	scanf("%d", &nc);
	for (c = 1; c <= nc; ++c) {
		scanf("%d%d", &a, &b);
		ans = 0;
		for (int i = a; i <= b; ++i) {
			ans += count(i, a, b);
			//if (count(i, a, b) > 0) {
			//printf("%d:%d:%d\n", i, id[i], count(i, a, b));
			//print(id[i]);
			//}
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}
