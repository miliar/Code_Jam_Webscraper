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
	freopen("input_a.txt", "rt", stdin);
	freopen("output_a.txt", "wt", stdout);

	int cases, N, A, B, count;
	scanf("%d", &cases);
	list<int> Ai, Bi;
	list<int>::iterator iterA, iterB;

	for (int i = 1; i <= cases; i++)
	{
		scanf("%d", &N);
		Ai.clear();
		Bi.clear();
		count = 0;

		for (int i = 0; i < N; i++)
		{
			scanf ("%d %d", &A, &B);
			Ai.push_back(A);
			Bi.push_back(B);

			for (iterA = Ai.begin(), iterB = Bi.begin();
				iterA != Ai.end() && iterB != Bi.end();
				iterA++, iterB++)
			{
				if ((*iterA < A && *iterB > B) || (*iterA > A && *iterB < B)) count++;
			}
		}

		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}