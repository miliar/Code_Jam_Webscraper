/**
 * Google code jam 2010 Round 1
 * A. 
 *
 * singleheart@gmail.com
 */

#include <cstdio>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	scanf("%d\n", &T);

	for (int x=1; x <= T; ++x)
	{
		int N;
		scanf("%d\n", &N);

		int a[N];
		int b[N];

		for (int n=0; n < N; ++n)
			scanf("%d %d\n", &a[n], &b[n]);

		int y = 0;
		for (int i=0; i < N; ++i)
			for (int j=0; j < N; ++j)
				if (((a[i] < a[j]) && (b[i] > b[j])) ||
					(((a[i] > a[j]) && (b[i] < b[j]))))
					++y;
		y /= 2;

		printf("Case #%d: %d\n", x, y);
	}

	return 0;
}
