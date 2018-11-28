#include <iostream> //for cout
#include <stdio.h> //for freopen(), scanf()
#include <string> //for std::string
#include <math.h> //for pow(), fmod()
#include <set>

int T, d;
long int A, B, m, n;
std::set<long int> found;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d",&T);
	for (int i = 1; (i <= T); i++)
	{
		scanf("%ld %ld",&A, &B);

		found.erase(found.begin(), found.end());
		d = 0;
		for (long int j = B; j > 0; )
		{
			j = j / 10;
			d++;
		}

		for (long int n = A; n < B; n++)
		{
			m = n;
			int factor = pow(10,d-1);
			for (int j = 1; j < d ; j++)
			{
				m = (m / 10) + (m % 10) * factor;
				if ( (n < m) && (m <= B) )
				{
					found.insert( (n + m * pow(10,d)) );
				}
			}
		}

		std::cout << "Case #" << i << ": " << found.size() << "\n";
	}
	return 0;
}
