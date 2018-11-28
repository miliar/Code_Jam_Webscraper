// task.cpp: определяет точку входа для консольного приложения.
//

#include <stdio.h>
#include <math.h>
#include <iostream>

using namespace std;

int abs(int a)
{
	if (a > 0) return a; else return -a;
}

int main()
{
	#if 1
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	int tests;
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		int n, ans = 0, posO = 0, posB = 0, indO = 0, indB = 0, lengO = 0, lengB = 0;
		int X[111], O[111], B[111];
		char L[111];		
		cin >> n;		
		for (int c = 0; c < n; ++c )
		{
			cin >> L[c];
			cin >> X[c];			
			X[c]--;
			if ( L[c] == 'O' ) 
			{
				O[lengO] = X[c];
				lengO++;
			} else
			{
				B[lengB] = X[c];
				lengB++;
			}
		}
		O[lengO] = O[lengO-1];
		B[lengB] = B[lengB-1];

		// input finished

		int dx;

		for (int i = 0; i < n; ++i)
		{
			if (L[i] == 'O' )
			{
				dx = abs( O[indO] - posO ) + 1;		
				if ( indB < lengB)
				{

					if ( abs( B[indB] - posB ) <= dx ) 
					{
						posB = B[indB];
					} else
					{
						if (posB > B[indB])
						{
							posB -=dx;
						} else
						{
							posB +=dx;
						}
					}
				}				
				posO = O[indO];
				indO++;
				ans +=dx;
			} else
			{
				dx = abs( B[indB] - posB ) + 1;								
				if ( indO < lengO )
				{
					if ( abs( O[indO] - posO ) <= dx ) 
					{
						posO = O[indO];
					} else
					{
						if (posO > O[indO])
						{
							posO -=dx;
						} else
						{
							posO +=dx;
						}
					}			
				}
				
				posB = B[indB];
				indB++;
				ans +=dx;
			}
		}
		cout << "Case #" << t+1 << ": " << ans << endl;
	}
	return 0;
}

