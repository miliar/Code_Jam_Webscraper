#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <list>

#define MAX 128

using namespace std;

int n, k, check;
int map[MAX][MAX], tmp[MAX];
int data[MAX][MAX];

void reset_data() {
}

void gen_map() {
	int i, j, x, y;

	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			if(i == j)continue;
			for(x = 1; x < k; x++) {
				if(data[i][x - 1] >= data[j][x - 1] && data[i][x] <= data[j][x])break;
				if(data[i][x - 1] <= data[j][x - 1] && data[i][x] >= data[j][x])break;
			}
			if(x < k)
				map[i][j] = 1;
			else map[i][j] = 0;
		}
	}
}

void find(int index, int max) {
	int i, j;

	if(check)return;
	if(index == max) {
		check = 1;
		return;
	}

	i = 0;
	if(index > 0)
		i = tmp[index - 1] + 1;
	for( ; i < n; i++) {
		for(j = 0; j < index; j++)
			if(!map[tmp[j]][i])break;
		if(j == index) {
			tmp[index] = i;
			find(index + 1, max);
		}
	}
}

void find_ans() {
	int i, j;

	reset_data();

	scanf("%d %d", &n, &k);
	for(i = 0; i < n; i++)
		for(j = 0; j < k; j++)
			scanf("%d", &data[i][j]);
	gen_map();

	/*printf("\n");
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++)
			printf("%d ", map[i][j]);
		printf("\n");
	}*/

	for(i = 2; i <= n; i++) {
		check = 0;
		find(0, i);
		if(!check)break;
	}
	printf("%d", i - 1);
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
