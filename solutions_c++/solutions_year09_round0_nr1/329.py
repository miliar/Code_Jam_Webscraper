#include <iostream>
using namespace std;
int L, D, N;
char ss[5005][16];
char s[10000];
char flag[16][30];
inline bool checkok(int j)
{
	int i;
	for(i = 0; i < L; i++)
		if(flag[i][ss[j][i]-'a'] == 0) return false;
	return true;
}
int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d%d%d", &L, &D, &N);
	int i;
	for(i = 0; i < D; i++) scanf("%s", ss[i]);
	int Case;
	for(Case = 1; Case <= N; Case++)
	{
		scanf("%s", s);
		int len = strlen(s);
		int j, k = 0, id = 0;
		memset(flag, 0, sizeof(flag));
		for(j = 0; j < len; j++)
		{
			if(s[j] == '(')
			{
				j++;
				while(s[j] != ')') 
				{
					flag[id][s[j]-'a'] = 1;
					j++;
				}
				id++;
			}
			else
			{
				flag[id][s[j] - 'a'] = 1;
				id++;
			}
		}
		int ans = 0;
		for(j = 0; j < D; j++)
		{
			if(checkok(j))
				ans++;
		}
		printf("Case #%d: %d\n", Case, ans);
	}
}