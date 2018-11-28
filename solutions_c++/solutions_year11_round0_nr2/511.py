#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int ct[30][30];
int ot[30][30];
char s[105];
int main()
{
	int i,j,k,r,t,cas = 1,c,o,l,res;
	bool find;
	char a;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	while (t--)
	{
		memset(ct,0,sizeof(ct));
		memset(ot,0,sizeof(ot));
		scanf("%d",&c);
		for (i = 0;i < c;i++)
		{
			scanf("%s",s);
			ct[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			ct[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		scanf("%d",&o);
		for (i = 0;i < o;i++)
		{
			scanf("%s",s);
			ot[s[0] - 'A'][s[1] - 'A'] = 1;
			ot[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		scanf("%d",&l);
		k = 0;
		s[0] = '\0';
		getchar();
		for (i = 0;i < l;i++)
		{
			scanf("%c",&a);
			s[k++] = a;
			find = false;
			while (!find)
			{
				find = true;
				if (k > 1)
				{
					if (ct[s[k - 1] - 'A'][s[k - 2] - 'A'])
					{
						s[k - 2] = ct[s[k - 1] - 'A'][s[k - 2] - 'A'] + 'A';
						k--;
						find  = false;
						continue;
					}
					for (j = 0;j < k - 1;j++)
					{
						if (ot[s[j] - 'A'][s[k - 1] - 'A'])
						{
							k = 0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [",cas++);
		res = 0;
		for (i = 0;i < k;i++)
		{
			if (res == 0)
			{
				putchar(s[i]);
				res++;
			}
			else
				printf(", %c",s[i]);
		}
		printf("]\n");
	}
	return 0;
}