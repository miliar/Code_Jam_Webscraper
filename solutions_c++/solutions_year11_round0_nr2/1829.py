//============================================================================
// Name        : gcj@2011-QR-B.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

char map[30][30];
bool conflict[30][30];
char str[105];

int main() {
//	freopen("test.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	int index = 1;
	scanf ("%d", &t);
	while (t --) {
		int n;
		memset(map, 0, sizeof (map));
		memset(conflict, false, sizeof (conflict));

		scanf ("%d", &n);
		while (n --) {
			scanf ("%s", str);
			int a = str[0] - 'A';
			int b = str[1] - 'A';
			char c = str[2];
			map[a][b] = map[b][a] = c;
		}

		scanf ("%d", &n);
		while (n --) {
			scanf ("%s", str);
			int a = str[0] - 'A';
			int b = str[1] - 'A';
			conflict[a][b] = conflict[b][a] = true;
		}

		scanf ("%d", &n);
		scanf ("%s", str);
		int j = -1;
		int a, b;
		for (int i = 0; i < n; i ++) {
			if (j < 0) {
				str[++j] = str[i];
				continue;
			}
			a = str[j] - 'A';
			b = str[i] - 'A';
			if ('A' <= map[a][b] && map[a][b] <= 'Z') {
				str[j] = map[a][b];
			} else {
				bool flag = false;
				for (int k = 0; k <= j; k ++) {
					a = str[k] - 'A';
					if (conflict[a][b]) {
						j = -1;
						flag = true;
						break;
					}
				}
				if (flag == false) {
					str[++j] = str[i];
				}
			}
		}
		str[++j] = 0;
		printf ("Case #%d: [", index ++);
		for (int i = 0; i < j; i ++) {
			if (i != 0) {
				printf (", ");
			}
			printf ("%c", str[i]);
		}
		puts("]");
	}
	return 0;
}
