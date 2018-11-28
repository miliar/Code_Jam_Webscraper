#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);

		int N;
		cin >> N;
		vector<int> ivec(N);

		for (int i = 0; i < N; i++)
			cin >> ivec[i];

		bool has = false;
		for (int k = 1; k < (2 << 20); k++)
		{
			vector<int> vec;
			int val = k;
			for (int j = 0; j < 20; j++)
			{
				if (val % 2 != 0)
					vec.push_back(ivec[j]);
				val /= 2;

				if (val == 0)
					break;
			}

			if (vec.size() < 2)
				continue;

			int p = 1;
			for (int i = 0; i < vec.size(); i++)
				p *= 2;
			for (int i = 1; i < p; i++)
			{
				int s1 = 0;
				int s2 = 0;
				int val = i;
				vector<int> v1;
				vector<int> v2;

				for (int j = 0; j < vec.size(); j++)
				{
					if (val % 2 == 0)
					{
						s1 += vec[j];
						v1.push_back(vec[j]);
					}
					else
					{
						s2 += vec[j];
						v2.push_back(vec[j]);
					}

					val /= 2;
				}

				if (s1 == s2)
				{
					for (int j = 0; j < v1.size(); j++)
						printf("%d ", v1[j]);
					printf("\n");
					for (int j = 0; j < v2.size(); j++)
						printf("%d ", v2[j]);
					has = true;
					break;
				}
			}

			if (has)
				break;
		}

		if (!has)
			printf("Impossible");
		printf("\n");
	}

	return 0;
}