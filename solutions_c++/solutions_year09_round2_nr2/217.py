#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <sstream>

#define int64 long long

using namespace std;

string taskname = "bb";

int main() {
	freopen((taskname + ".in").c_str(), "r", stdin);
	freopen((taskname + ".out").c_str(), "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	for (int test = 0; test < tests; test++) {
		cerr << test << endl;
		cout << "Case #" << test + 1 << ": ";
	
		char buf[100];
		gets(buf);
		int len = strlen(buf);
		int pos = len - 1;
		while (pos > 0 && buf[pos - 1] >= buf[pos]) {
			pos--;
		}
		if (pos == 0) {
			sort(buf, buf + len);
			int z = 0;
			while (buf[z] == '0') {
				z++;
			}
			cout << buf[z];
			for (int i = 0; i < z + 1; i++) {
				cout << '0';
			}
			for (int i = z + 1; i < len; i++) {
				cout << buf[i];
			}
		} else {
			pos--;
			char cur = (char)'0' + 10;
			int curpos = -1;
			for (int i = pos + 1; i < len; i++) {
				if (buf[i] > buf[pos] && buf[i] < cur) {
					cur = buf[i];
					curpos = i;
				}
			}
			assert(curpos != -1);
			swap(buf[pos], buf[curpos]);
			sort(buf + pos + 1, buf + len);
			printf("%s", buf);
		}

		cout << endl;
	}

	return 0;
}
