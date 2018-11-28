#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int case_cnt;

char line[1024];
char line_permuted[1024];
int K;
int nums[10];

void calc_new() {
	int x,y;
	int steps;
	int len = strlen(line);

	steps = len/K;
	for (y=0; y<steps; y++) {
		for (x=0; x<K; x++) {
			line_permuted[y*K+x] = line[ y*K + nums[x] ];
		}
	}
	line_permuted[strlen(line)] = '\0';
}

int rlc() {
	int x;
	int len = strlen(line_permuted);

	char old = -1;
	int res = 0;

	for (x=0; x<len; x++) {
		if ( line_permuted[x] != old ) {
			old = line_permuted[x];
			res++;
		}
	}
	return res;
}
	
	

int main ( int argc, char ** argv ) {
	int case_nr;
	int x;

	scanf("%d",&case_cnt);
	for (case_nr = 0; case_nr < case_cnt; case_nr++ ) {
		scanf("%d", &K);

		fgets( line,1024, stdin);
		fgets( line, 1024, stdin);

		if ( line[strlen(line)-1] == '\n' ) line[strlen(line)-1] = '\0';

		for (x=0; x<K; x++) {
			nums[x] = x;
		}

		int mini = 100000;

		do {
			calc_new();
			int t = rlc();
			if ( t < mini ) mini = t;
		} while(next_permutation(nums,nums+K));

		printf("Case #%d: %d\n", case_nr+1, mini);
	}

	return 0;
}
