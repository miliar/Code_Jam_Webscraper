#include <iostream>

using namespace std;

char str[1000];
int value[300];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	int Test, i ,j ,k ,tt;
	scanf("%d",&Test);
	for(tt = 1; tt <= Test; tt ++)
	{
		j = 1;
		scanf("%s", str);
		memset(value, -1, sizeof(value));
		value[str[0]] = j ++;

		int leap = 1;
		for(i = 1; str[i] != '\0'; i ++)
		{
			if(value[str[i]] == -1)
			{
				if(leap)
					value[str[i]] = 0;
				else
					value[str[i]] = j ++;
				leap = 0;
			}
		}

		long long ans = 0;
		for(i = 0; str[i] != '\0'; i ++)
		{
			ans = ans * j + value[str[i]];
		}
		printf("Case #%d: %lld\n", tt, ans);
	}
	return 0;
}