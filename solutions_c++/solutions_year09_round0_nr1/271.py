#include <stdio.h>
#include <memory.h>
#define SIZE 5100

char word[SIZE][20];
char pat[300];
bool used[20][30];
int main()
{
	int i,j,l,d,n,no,ans,t;
	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	for(i = 0; i < d; i++)
		scanf("%s",word[i]);
	for(no = 1; no <= n; no++)
	{
		scanf("%s",pat);
		t = 0;
		memset(used,0,sizeof(used));
		for(i = 0; pat[i]; i++)
		{
			if(pat[i] == '(')
			{
				while(pat[++i] != ')')
					used[t][pat[i]-'a'] = true;
				t++;
				continue;
			}
			else if(pat[i] >= 'a' && pat[i] <= 'z')
			{
				used[t++][pat[i]-'a'] = true;
			}
		}
		ans = 0;
		if(t == l)
		{
			for(i = 0; i < d; i++)
			{
				for(j = 0; j < l; j++)
				{
					if(!used[j][word[i][j] - 'a'])
						break;
				}
				if(j == l)
					ans++;
			}
		}
		printf("Case #%d: %d\n",no,ans);
	}
	return 0;
}
