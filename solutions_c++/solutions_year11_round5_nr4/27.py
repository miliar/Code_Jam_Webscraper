#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <assert.h>
#include <math.h>
using namespace std;

#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))

int T;
char zeile[1000];

void find() {
	int l;
	for (l = 0; zeile[l] != '\0' && zeile[l] != '\n'; l++)
		;
	int anz = 0;
	for (int i = 0; i < l; i++)
		if (zeile[i] == '?')
			anz++;
	for (int num = 0; num < (1<<anz); num++) {
		long long r = 0;
		int h = 0;
		for (int i = 0; i < l; i++) {
			r <<= 1;
			if (zeile[i] == '1')
				r++;
			else if (zeile[i] == '?') {
				r += (num>>h)&1;
				h++;
			}
		}
		long long sq = round(sqrt(r));
		if (sq*sq == r) {
			h = 0;
			for (int i = 0; i < l; i++) {
				int g = 0;
				if (zeile[i] == '1')
					g++;
				else if (zeile[i] == '?') {
					g += (num>>h)&1;
					h++;
				}
				printf("%d", g);
			}
			printf("\n");
			return;
		}
	}
}

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%s ", zeile);
		find();
	}
	return 0;
}
