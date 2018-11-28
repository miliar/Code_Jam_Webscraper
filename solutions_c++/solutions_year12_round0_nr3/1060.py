/*
 * Google Code Jam 2012 - Qualification Round
 * Problem C: Recycled Numbers
 */

#include <stdio.h>
#include <string.h>
#include <set>

using namespace std;

int main() {

	int test_no;
	set<int> used;

	// Obtain the test number.
	scanf("%d", &test_no);

	// Loop each sentence.
	for(int i = 0; i < test_no; i++) {

		int a, b;
		int count = 0;

		scanf("%d%d", &a, &b);

		for(int n = a; n <= b; n++) {

			used.clear(); // make the set empty

			int size = 1;
			while(size <= n) {
				size *= 10;
			}

			int mod = 10;
			while(mod < size) {

				int front = n / mod;
				int back = n % mod;

				if(back / (mod / 10) > 0) { // indicate non-zero leading of the back portion

					int m = front + back * (size / mod);

					if(m > n && m <= b && used.find(m) == used.end()) {
						++count;
						used.insert(m);
					}

				}

				mod *= 10;
			}

		}

		printf("Case #%d: %d\n", i+1, count);
	}

	return 0;
}