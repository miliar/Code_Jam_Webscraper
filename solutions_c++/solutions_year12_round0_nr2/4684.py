#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t;
	scanf("%d ", &t);
	for (int i = 0; i < t; i++)
	{
		int N;
		int S;
		int p;
		scanf("%d %d %d ", &N, &S, &p);
		int mas[105] = {0};
		for (int i = 0; i < N; i++)
			scanf("%d ", &mas[i]);
		int res = 0;
		int c_c = 0;
		int c_s = 0;
		for (int i = 0; i < N; i++)
		{
			bool com = false;
			bool sur = false;
			bool was = false;
			for (int j = 0; j <= 10; j++)
			{
				for (int k = 0; k <= 10; k++)
				{
					for (int h = 0; h <= 10; h++)
					{
						if ((abs(j - k) > 1) || (abs(j - h) > 1) || (abs(k - h) > 1))
							continue;
						if ((j + h + k) != mas[i])
							continue;
						int M = max(j, max(k,h));
						if (M >= p)
						{
							com = true;
							was = true;
							break;
						}					
					}
					if (was)
						break;
				}
				if (was)
					break;
			}
			if ((c_s < S) && !com)
			{
				was = false;
				for (int j = 0; j <= 10; j++)
				{
					for (int k = 0; k <= 10; k++)
					{
						for (int h = 0; h <= 10; h++)
						{
							if ((abs(j - k) > 2) || (abs(j - h) > 2) || (abs(k - h) > 2))
								continue;
							if ((j + h + k) != mas[i])
								continue;
							int M = max(j, max(k,h));
							if (M >= p)
							{
								sur = true;
								c_s++;
								was = true;
								break;
							}					
						}
						if (was)
							break;
					}
					if (was)
						break;
				}
			}
			if (com || sur)
				res++;
		}


		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
