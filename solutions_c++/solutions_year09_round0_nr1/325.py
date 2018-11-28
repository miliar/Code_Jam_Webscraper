#include <iostream>
using namespace std;

int hash[30];

struct node
{
	char name[20];
	int flag;
}date[10000];

char s[500];

int main()
{
	int i , j , l , d , n , cas = 0 , now , len , ans;
	freopen("1.txt" , "w" , stdout);
	while(scanf("%d %d %d" , &l , &d , &n) == 3)
	{
		for(i = 0 ; i < d ; i ++)
		{
			scanf("%s" , &date[i].name);
			date[i].flag = 0;
		}
		for(cas = 1 ; cas <= n ; cas ++)
		{
			now = 0;
			scanf("%s" , s);
			len = strlen(s);
			for(i = 0 ; i < len ; i ++)
			{
				if(s[i] == '(')
				{
					memset(hash , false , sizeof(hash));
					i ++;
					while(s[i] != ')')
					{
						hash[s[i] - 'a'] = true;
						i ++;
					}
					for(j = 0 ; j < d ; j ++)
					{
						if(now == 0)
						{
							if(hash[ date[j].name[now] - 'a' ] == false)
								date[j].flag = cas - 1;
							else
								date[j].flag = cas;
						}
						else
						{
							if(cas != date[j].flag)
								continue;
							if(hash[ date[j].name[now] - 'a' ] == false)
								date[j].flag = cas - 1;
						}
						
					}
				}
				else
				{
					for(j = 0 ; j < d ; j ++)
					{
						if(now == 0)
						{
							if(date[j].name[now] != s[i])
								date[j].flag = cas - 1;
							else
								date[j].flag = cas;
						}
						else
						{
							if(cas != date[j].flag)
								continue;
							if(date[j].name[now] != s[i])
								date[j].flag = cas - 1;
						}
					}
				}
				now ++;
			}
			ans = 0;
			for(i = 0 ; i < d ; i ++)
			{
				if(date[i].flag == cas)
					ans ++;
			}
			printf("Case #%d: %d\n" , cas , ans);
		}
	}
	return 0;
}