#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases;
	scanf("%d", &cases);

	int N, K, p;
	bool power;

	for (int i = 1; i <= cases; i++)
	{
		int ugly = 0;

		scanf ("%d %d", &N, &K);

		p = (int)pow(2, (double)N);
		power = (K % p) == (p - 1);

		cout << "Case #" << i << ": " << ((power)?"ON":"OFF") << endl;
	}

	return 0;
}