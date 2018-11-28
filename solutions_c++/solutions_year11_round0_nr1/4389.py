#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;

int t, n, time, tmp;
int pos[101];
char str[101];
int pre;

int main() {
	int i;
	freopen("output_1.txt","w",stdout);
	freopen("A-large.in", "r", stdin);

	scanf ("%d", &t);
	for (int ii = 1; ii <=t; ++ii) {
		time = tmp = 0;
		scanf ("%d", &n);
		str[0] = 'A';
		pos[0] = 1;
		pre = 1;
		for (i = 1; i <= n; ++i) {
			cin >> str[i] >> pos[i];
			if (str[i] == str[i - 1]) {
				time += abs(pos[i] - pos[i - 1]) + 1;
				tmp += abs(pos[i] - pos[i - 1]) + 1;
			}
			else {
				int len = abs(pos[i] - pre);
				if (tmp <len) {
					time += abs(len - tmp);
					tmp = abs(len - tmp);
				}
				else {
					tmp = 0;
				}
				time += 1;
				tmp += 1;
				pre = pos[i - 1];
			}
		}
		printf ("Case #%d: %d\n", ii, time);
	}
	return 0;
}