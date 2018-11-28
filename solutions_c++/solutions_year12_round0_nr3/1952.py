
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>

#include <vector>
#include <set>
#include <algorithm>
#include <complex>
#include <assert.h>
#include <queue>

using namespace std;

int main (void)
{
	int T,A,B, count;
	int i;

	scanf ("%d", &T);
	for (i = 1; i <= T; i++) {
		char num[255];
		printf ("Case #%d: ", i);
		scanf ("%d %d", &A, &B);
		count = 0;
		for (int j = A; j <= B; j++) {
			set<int> s;
			sprintf (num, "%d", j);
			for (int k = 0; k < strlen(num); k++) {
				char temp;
				int cur;
				temp = num[0];
				memcpy (num, num+1, strlen(num)-1);
				num[strlen(num)-1] = temp;
				sscanf (num, "%d", &cur);
//				printf ("%d, ", cur);
				if (cur > j && cur <= B) {
					int size = s.size();
					s.insert(cur);
					if (s.size() == size) { break; }
					count++;
//					printf ("%d: %d-%d\n", count, j, cur);
				}
			}
		}
		printf ("%d\n", count);
	}

	return 0;
}

