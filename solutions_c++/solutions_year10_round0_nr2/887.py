#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <ctime>
#include <cmath>

using namespace std;

int nod(int x, int y)
{
	if ( x == 0)
	{
		return y;
	}
	else
	{
		return nod(y % x, x);
	}
}

int abs(int a, int b)
{
	return (a > b) ? a - b : b - a; 
}

int main()
{
	freopen("B-small-attempt5.in", "r", stdin);
	freopen("B-small-attempt5.out", "w", stdout);

	int C;
	cin >> C;

	int N;
	for ( int i = 1; i <= C; i++)
	{
		cin >> N;
		int *mas = new int[N];
		for ( int j = 0; j < N; j++)
		{
			cin >> mas[j];
		}

		cout << "Case #" << i << ": ";
		if ( N == 2)
		{
			sort(mas, mas + N);
			cout << ((mas[1] - mas[0]) - mas[0] % (mas[1] - mas[0])) % (mas[1] - mas[0]) << endl;
		}else
		{
			sort(mas, mas + N);
			for ( int j = 1; j < N; j++)
			{
				mas[j] = mas[j] - mas[0];
			}

			for ( int j = N - 2; j >= 1; j--)
			{
				mas[j] = nod(mas[j], mas[j + 1]);
			}
			
			int d = nod(mas[0], mas[1]);
			int y = 0;
			
			int z = sqrt((double)mas[1]);
			int j = 1;
			
			if ( mas[0] % mas[1] == 0)
			{
				cout << 0 << endl;
			}
			else
			{
				while ( j <= z)
				{
					if ( mas[1] % j == 0)
					{
						if ( j > d)
						{
							d = j;
							y = j - mas[0] % j;
						}

						int l = mas[1] / j;
						if ( l > d)
						{
							d = l;
							y = l - mas[0] % l;
						}
					}
					j++;
				}
				cout << y << endl;
			}
		}
	}
}