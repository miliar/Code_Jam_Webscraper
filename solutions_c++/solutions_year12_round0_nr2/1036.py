/*
 * Google Code Jam 2012 - Qualification Round
 * Problem B: Dancing With the Googlers
 */

#include <stdio.h>
#include <string.h>

#define MAX_N 100

int main() {

	int test_no;

	// Obtain the test number.
	scanf("%d\n", &test_no);

	// Loop each sentence.
	for(int i = 0; i < test_no; i++) {

		int n, s, p;
		scanf("%d%d%d", &n, &s, &p);

		int count = 0;

		for(int j = 0; j < n; j++) {

			int score;
			scanf("%d", &score);

			if(score > 0 && (score+2)/3 >= p) { // score can definitely be above p
				++count;
			}
			else if(score > 0 && (score+4)/3 >= p && s > 0) { // score can be above p if suprising
				++count;
				--s;
			}
			else if(score == 0 && p == 0) {
				++count;
			}
		}

		printf("Case #%d: %d\n", i+1, count);
	}

	return 0;
}