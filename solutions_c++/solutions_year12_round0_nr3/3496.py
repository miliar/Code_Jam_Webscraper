#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int  T, a, b ,l, n, flag, pair, m;
	char x[20], y[20];
	scanf("%d",&T);
	for (int t = 1; t <= T; t++ )
	{
		pair = 0;
		scanf("%d %d",&a,&b);
		for (int i = a; i <= b; i ++ )
		{
			for (int k = i; k <= b; k++ )
			{
				n = sprintf(y, "%d", k);
				sprintf(x, "%d", i);

                for (int j = 0; j < n; j++ )
                {
					if ( y[j] == x[0] )
					{
						l = j+1;
						m = 1;
						flag = 1;
						while ( m != n )
						{
							if ( l == n )
								l = 0;
							if ( y[l] != x[m] ) {
								flag = 0;
								break;
							}
                            l++;
                            m++;
						}
                        if ( flag )
                        {
							if ( j != 0 )
								pair++;
							break;
						}

					}

				}

			}

		}
		printf("Case #%d: %d\n",t,pair);
	}
	return 0;
}
