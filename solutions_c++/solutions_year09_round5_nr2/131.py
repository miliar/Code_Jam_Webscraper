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
#define MAXA 26
#define MOD 10009

using namespace std;

int n, k, count_[MAXA], data[MAX][MAXA], ans;
int tmp[MAX];
char str[MAX], word[MAX][MAX];

void reset_data() {
	int i, j;
	for(i = 0; i < MAX; i++)
		for(j = 0; j < MAXA; j++)
			data[i][j] = 0;
}

void run(int index, int max) {
	int i, j, sum;

	if(index == max) {
		sum = 1;
		for(i = 0; str[i] != 0; i++) {
			if(str[i] == '+') {
				ans = (ans + sum) % MOD;
				sum = 1;
			} else {
				sum = (sum * count_[str[i] - 'a']) % MOD;
			}
		}
		return;
	}

	i = 0;
	for(; i < n; i++) {
		tmp[index] = i;
		for(j = 0; j < MAXA; j++)
			count_[j] += data[i][j];
		/*for(j = 0; word[i][j] != 0; j++) {
			count_[word[i][j] - 'a']++;
		}*/
		run(index + 1, max);
		for(j = 0; j < MAXA; j++)
			count_[j] -= data[i][j];
		/*for(j = 0; word[i][j] != 0; j++) {
			count_[word[i][j] - 'a']--;
		}*/
	}
}

void find_ans() {
	int i, j;

	reset_data();

	scanf("%s %d", str, &k);
	for(i = 0; str[i] != 0; i++);
	str[i] = '+';
	str[i + 1] = 0;

	scanf("%d", &n);
	for(i = 0; i < n; i++) {
		scanf("%s", word[i]);
		for(j = 0; word[i][j] != 0; j++)
			data[i][word[i][j] - 'a']++;
	}

	for(i = 1; i <= k; i++) {
		ans = 0;
		run(0, i);
		printf(" %d", ans);
	}
}

int main(int argc, char *argv[])
{
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d:", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
