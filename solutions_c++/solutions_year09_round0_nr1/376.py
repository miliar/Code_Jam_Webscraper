#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;


int L, N, D;

char dict[5500][20];
char inp[20000];

int main() 
{
	freopen("A-large.in", "r", stdin);
	
	freopen("A-large.out", "w", stdout);

	scanf("%d %d %d", &L, &D, &N);

	for (int i = 0; i < D; i++) scanf("%s", dict[i]);

	for (int id = 1; id <= N; id++)
	{
		scanf("%s", inp);

		int ans = 0;

		for (int i = 0; i < D; i++) 
		{
			bool match = true;

			int p = 0;

			for (int k = 0; k < L; k++)
			{
				if (inp[p] != '(')
				{
					if (dict[i][k] != inp[p]) 
					{
						match = false;
						break;
					}
				}
				else 
				{
					bool find = false;
					
					while (inp[p] != ')')
					{
						if (inp[p] == dict[i][k])
						{
							find = true;
						}
					
						++p;
					}

					if (!find) 
					{
						match = false;
					    break;
					}
				}

				++p;
			}

            if (match) ++ans;
		}

		printf("Case #%d: %d\n", id, ans);
	}

	return 0;
}
            