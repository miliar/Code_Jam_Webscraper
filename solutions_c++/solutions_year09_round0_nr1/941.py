#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

int dic[20][256];
char words[5001][20];
char pattern[4096];

int main()
{
	int l,d,n;
	int i,j,k;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	memset(dic, 0, sizeof(dic));

	for (i = 0; i < d; i++)
	{
		scanf("%s", words[i]);
	}
	
	for (i = 0; i < n; i++)
	{
		scanf("%s", pattern);
		memset(dic, 0, sizeof(dic));
		int pos = 0;
		for (j = 0; pattern[j]; j++, pos++)
		{
			if(pattern[j]=='(')
			{
				while(pattern[++j] != ')')
				{
					dic[pos][pattern[j]] = 1;	
				}
			}
			else
			{
				dic[pos][pattern[j]] = 1;
			}
		}

		int ans = 0;
		for(j = 0; j < d; j++)
		{
			for(k = 0; k < l; k++)
			{
				if(dic[k][words[j][k]] == 0)
					break;
			}
			if(k == l)
				ans++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}

	return 0;
}