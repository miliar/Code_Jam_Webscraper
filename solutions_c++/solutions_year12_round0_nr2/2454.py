#include <iostream>
#include <cmath>
using namespace std;

int a[31] = {0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7 ,8, 8, 8, 9, 9 ,9, 10, 10, 10};
int b[31] = {0, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7 ,8, 8, 8, 9, 9 ,9, 10, 10, 10, 10, 10};

int t, n, s, p, X[100];

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", & t);
	int ID = 0;
	while (t --)
	{
		scanf("%d %d %d", & n, & s, & p);
		int c1 = 0, c2 = 0, c3 = 0;
		for (int i = 0; i < n; ++ i)
		{
			scanf("%d", X + i);
			c1 += (a[X[i]] >= p);
			c2 += (b[X[i]] < p);
			c3 += (b[X[i]] >= p && a[X[i]] < p);
        }
			
		ID ++;
		printf("Case #%d: %d\n", ID, c1 + min(c3, s));
	}
//    fclose(stdout);

	return 0;
}
