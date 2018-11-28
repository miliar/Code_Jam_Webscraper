#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;



int n[800];
int m[800];

static int
do_calc(int *n, int *m, int count)
{
	int i,j;
	double result;
	result = 0;
	for(i=0;i<count;i++) {
		result += n[i] * m[count-i-1];
	}
	return (int)result;
}

int main(void)
{
	int test_cases;
	int i, j;
	int nums;
	int min;

	if(fscanf(stdin, "%d", &test_cases) != 1) {
		fprintf(stderr, "Cannot read number of test cases\n");
		return 1;
	}
	for(i = 0; i < test_cases; i++) {
		if(fscanf(stdin, "%d", &nums) != 1) {
			fprintf(stderr, "Cannot read items\n");
			return 1;
		}
		for(j = 0; j < nums; j++) {
			if(fscanf(stdin, "%d", &n[j]) != 1) {
				fprintf(stderr, "Unexpected EOF\n");
				return 1;
			}
		}
		for(j = 0; j < nums; j++) {
			if(fscanf(stdin, "%d", &m[j]) != 1) {
				fprintf(stderr, "Unexpected EOF\n");
				return 1;
			}
		}
		sort(n, &n[nums]);
		sort(m, &m[nums]);

		min = do_calc(n, m, nums);
		printf("Case #%d: %d\n", i+1, min);
	}
	

	
}
