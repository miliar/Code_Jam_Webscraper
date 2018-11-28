#include <cctype>
#include <cstdio>
#include <cstring>

bool ada[15][26];
char kata[5000][16], buffer[1001];
int L, D, N;

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for(int i = 0;i < D;++i)
		scanf("%s", kata[i]);
	gets(buffer);
	for(int i = 0;i < N;++i)
	{
		memset(ada, 0, sizeof(ada));
		gets(buffer);
		bool satu = 1;
		for(int j = 0, k = 0;buffer[j];++j)
			if(buffer[j] == '(')
				satu = 0;
			else if(isalpha(buffer[j]))
			{
				if(satu)
					ada[k++][buffer[j] - 'a'] = 1;
				else
					ada[k][buffer[j] - 'a'] = 1;
			}
			else
			{
				satu = 1;
				++k;
			}
		int ans = 0;
		for(int j = 0;j < D;++j)
		{
			bool nggakada = 0;
			for(int k = 0;k < L;++k)
				if(!ada[k][kata[j][k] - 'a'])
				{
					nggakada = 1;
					break;
				}
			ans += !nggakada;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
