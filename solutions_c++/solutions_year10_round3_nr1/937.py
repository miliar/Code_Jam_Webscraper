#include <assert.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <climits>
#include <cmath>
#include <time.h>
#include <iomanip>

using namespace std;

#define MAXN 100005

int T, N;
typedef struct {
	int left, right;
} Line;

Line lines[MAXN];

bool cmp(Line line1, Line line2) {
	return line1.left < line2.left;
}

int main() {
	cin >> T;
	for (int caseid = 1; caseid <= T; caseid++) {
		cin >> N;
		for (int i = 0; i < N ;i++) {
			cin >> lines[i].left >> lines[i].right;
		}

		sort(lines, lines + N, cmp);

		int cnt = 0;
		for (int i = 0; i < N ;i++) {
			for (int j = i + 1; j < N; j++) {
				if (lines[j].right < lines[i].right)
					cnt++;
			}
		}

//		for (int i = 0; i < N ;i++) {
//			cout <<  lines[i].left << ' ' <<  lines[i].right << endl;
//		}

		cout << "Case #" << caseid << ": " << cnt << endl;
	}
}
