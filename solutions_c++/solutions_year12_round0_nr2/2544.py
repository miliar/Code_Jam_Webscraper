#include <iostream> //for cout
#include <stdio.h> //for freopen(), scanf()
#include <algorithm> //for max()

/** case values
 * T  1 - 100 inc   Total number of cases
 * N  1 - 3 small   Number of Googlers
 *    1 - 100 large
 * S  0 - N inc     Surprising triplets of scores
 * p  0 - 10 inc    Target best result
 * ti 0 - 10 inc    Total score (one for each of N)
 * Input sequence   N S p ti+
 */

int T, N, S, p, ti, r, n, s;


int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	scanf("%d",&T); //loads the number of cases

	for (int i = 1; (i <= T); i++) //iterate the cases
	{
		scanf("%d %d %d",&N,&S,&p);

		r = 0;
		n = (p*3)-2;
		s = std::max ( 1, (p*3)-4 ); //guard for p<2

		for (int j = 1; (j <= N); j++ ) //iterate through scores
		{
			scanf("%d",&ti);
			if ( ti >= n ) {
				r++;
				} else if ( (S>0) && (ti>=s) ) {
					r++;
					S--;
				}
		}
		std::cout << "Case #" << i << ": " << r << "\n";
	}
	return 0;
}
