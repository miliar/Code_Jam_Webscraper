#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#include <vector>
#include <set>
#include <map>
#include <string.h>


using namespace std;

char nums[1024];
int signs[1024];

int num_len;
int cases;

int cnt_up() {
	int x;
	int more = 1;
	int over;

	over = 1;

	for (x=0; x<=num_len; x++) {

		if ( over && x == num_len ) {
			more = 0;
			break;
		}

		signs[x] = signs[x]+over;

		over = signs[x] / 3;
		signs[x] = signs[x] % 3;

		if ( over == 0 ) break;
	}
/*
	for (x=0; x<num_len; x++) {
		printf(" %d", signs[x]);
	}
	printf("\n");
*/
	return more;
}

int main ( int argc, char ** argv ) {
	int nr,x;
	int to_check;

	scanf("%d", &cases);
	fgets( nums, 1024, stdin );

	for (nr=0; nr<cases; nr++) {
		fgets( nums, 1024, stdin );
		if ( nums[strlen(nums)-1] == '\n' ) nums[strlen(nums)-1] = '\0';

		num_len = strlen(nums) - 1;
		to_check = num_len * num_len * num_len;

		long long hits = 0;
		do {
			long long sum = 0;
			int pos = 0;

			long long the_num = nums[0]-'0';
			int the_sign = 1;

			for (pos=1; pos<=num_len; pos++) {

				if ( signs[pos-1] == 0 ) {
					the_num *= 10;
					the_num += nums[pos]-'0';
					continue;
				}

				if ( signs[pos-1] == 1 ) {
					sum = sum + the_num * the_sign;
					the_sign = 1;
					the_num = nums[pos]-'0';
					continue;
				}

				if ( signs[pos-1] == 2 ) {
					sum = sum + the_num * the_sign;
					the_sign = -1;
					the_num = nums[pos]-'0';
				}
			}

			sum = sum + the_num * the_sign;
		
	

			//printf("Sum is %lld ", sum);
			if ( sum < 0 ) sum *= -1;
			int valid = 0;
			if ( sum == 0 ) valid = 1;
			if ( !(sum%2) ) valid = 1;
			if ( !(sum%3) ) valid = 1;
			if ( !(sum%5) ) valid = 1;
			if ( !(sum%7) ) valid = 1;

			if ( valid ) {
				hits++;
			}

		} while ( cnt_up() );
		printf("Case #%d: %lld\n", nr+1,  hits);
	}
		

	return 0;
}
