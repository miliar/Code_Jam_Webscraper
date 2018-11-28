
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>
#include <set>

using namespace std;

int main(int argc, char* argv[])
{
	int T;

	scanf(" %d", &T);
	for(int t = 1; t <= T; t++)
	{
		int A, B;
		scanf(" %d %d", &A, &B);


		int count = 0;
		for(int i = A; i < B; i++)
		{
			int n_digits = 0;
			int m = i;
			while(m)
			{
				n_digits++;
				m /= 10;
			}
			//printf("%d digits = %d\n", i, n_digits);
			int n = i;
			set<int> myset;
			for (int num_digits = n_digits; num_digits > 0; num_digits--)
			{
			int last_digit = n % 10;
			//printf("last digit=%d\n", last_digit);
			//if (last_digit == 0)
			//	continue;
			n /= 10;
			
			int x_digits = n_digits;
			while(x_digits > 1)
			{
			    last_digit *= 10;	
				x_digits--;
			}
			n += last_digit;
			if (n > i && n <= B)
			{
				if (myset.find(n) == myset.end())
				{
					//printf("%d %d\n", i, n);
					count++;
					myset.insert(n);
				}
			}
			}
		}

		printf("Case #%d: %d\n", t, count);

	}


	return 0;
}

