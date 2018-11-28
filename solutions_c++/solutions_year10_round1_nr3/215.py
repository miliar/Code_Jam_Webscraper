#include <iostream>
#include <cmath>
using namespace std;

int test, a1, a2, b1, b2;

int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%i", &test);
	for (int tt = 1; tt <= test; tt++) {
		scanf("%i%i%i%i", &a1, &a2, &b1, &b2);

		long long sum = 0; 
		double tmp1;
		int tmp2;
		for (int i = a1; i <= a2; i++) {
			tmp1 = i * (1 + sqrt(5.0))/2;
			tmp2 = max((int)tmp1 + 1, b1);

			if (tmp2 <= b2 && tmp2 >= b1) sum += b2 - tmp2 + 1;
		}

		for (int i = b1; i <= b2; i++) {
			tmp1 = i * (1 + sqrt(5.0))/2;
			tmp2 = max((int)tmp1 + 1, a1);

			if (tmp2 <= a2 && tmp2 >= a1) sum += a2 - tmp2 + 1;
		}

		cout << "Case #" << tt << ": " << sum << endl;
	}

	return 0;
}