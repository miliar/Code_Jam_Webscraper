#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <list>

#define MAX 64

using namespace std;

int n, data[MAX], ans;
char map[MAX][MAX];

int swap(int i, int j) {
	int tmp = data[i];
	data[i] = data[j];
	data[j] = tmp;
	ans++;
}

void reset_data() {
}

void find_ans() {
	int i, j;

	reset_data();

	scanf("%d", &n);
	for(i = 0; i < n; i++) {
		scanf("%s", map[i]);
		data[i] = -1;
		for(j = 0; j < n; j++)
			if(map[i][j] == '1')
				data[i] = j;
	}

	ans = 0;
	for(i = 0; i < n; i++) {
		for(j = i; data[j] > i; j++);
		for( ; j > i; j--) {
			swap(j, j - 1);
		}
	}
	printf("%d", ans);
}

int main(int argc, char *argv[])
{
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
