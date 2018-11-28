/**
 * Google code jam 2010 Round 1
 * A. 
 *
 * singleheart@gmail.com
 */

#include <cmath>
#include <cstdio>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	scanf("%d\n", &T);

	for (int x=1; x <= T; ++x)
	{
		int L, P, C;
		scanf("%d %d %d\n", &L, &P, &C);

		int y = 0;
		if (L * C >= P)
			y = 0;
		else 
		{
			double d = static_cast<double>(P) / L;
			double result = log(log(d) / log(C))/log(2);
			y = result;
			if (y != static_cast<int>(ceil(result)))
				y += 1;
		}

		printf("Case #%d: %d\n", x, y);
	}

	return 0;
}
