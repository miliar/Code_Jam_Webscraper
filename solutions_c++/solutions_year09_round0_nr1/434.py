#include <iostream>
using namespace std;

int L, D, N;
char words[5001][106];
char sen[5000];


int Count(char* sen)
{
	int res = 0;
	for (int i = 0; i < D; i++)
	{
 		bool flag = true;
		int jj = 0;
		for (int j = 0; j < L; j++)
		{

			char a = words[i][j];
			if (sen[jj] == '(')
			{
				int k = jj+1;
				while (sen[k] != ')')
				{
					if (sen[k] == a)
					{
						break;
					}
					k++;
				}
				if (sen[k] == ')')
				{
					flag = false;
					break;
				}
				else
					while (sen[k] != ')') k++;

				jj = k+1;
			}
			else
			{
				if (sen[jj] != a)
				{
					flag = false;

				}
				else
					jj++;
			}
			if (!flag) break;
		}
		if (flag) res++;
	}
	return res;

}

int  main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		scanf("%s", words[i]);

	}

	for (int i = 0; i < N; i++)
	{
		scanf("%s", sen);
		int res = Count(sen);
		printf("Case #%d: %d\n", i+1, res);
	}

	return 0;
}
