#include<iostream>
using namespace std;
int main()
{
	int i, j, k, L, D, N;
	scanf("%d %d %d", &L, &D, &N);
	char dic[5005][20];
	char str[1000];
	for(i = 0; i < D; i ++)
		scanf("%s", dic[i]);
	int num[5005], d;
	for(int p = 1; p <= N; p ++)
	{
		num[p] = 0;
		scanf("%s", str);
		for(i = 0; i < D; i ++)
		{
			for(k = 0,j = 0; j < L; j ++)
			{
				d = 0;
				if(str[k] == '(')
				{
					while(str[k] != ')')
					{
						if(str[k] == dic[i][j])
							d = 1;
						k ++;
					}
					if(d) k ++;
					else break;
				}
				else
				{
					if(str[k] == dic[i][j]) k++;
					else break;
				}
			}
			if(j == L) num[p] ++;
		}
	}
	for(i = 1; i <= N; i ++)
		printf("Case #%d: %d\n", i, num[i]);
	return 0;
}