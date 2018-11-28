#include<iostream>
#define Mode 10000
using namespace std;
char tp[505], wc[] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
int n;
int sum;
void dfs(int x, int num)
{
	int i;
	if(num == 19)
	{
		sum ++;
		sum %= Mode;
		return ;
	}
	if(x == n) return ;
	for(i = x; i < n; i ++)
	{
		if(tp[i] == wc[num])
			dfs(i + 1, num + 1);
	}
	return ;
}
int main()
{
	int i, j, T;
	int len; 
	char str[505];
	scanf("%d", &T);
	getchar();
	for(j = 1; j <= T; j ++)
	{
		gets(str);
		len = strlen(str);
		n = 0;
		for(i = 0; i < len; i ++)
		{
			if(str[i] == 'w' || str[i] == 'e' || str[i] == 'l' || str[i] == 'c' || 
			   str[i] == 'o' || str[i] == 'm' || str[i] == 't' || str[i] == 'd' ||
			   str[i] == 'j' || str[i] == 'a' || str[i] == ' ')
			   tp[n ++ ] = str[i];
		}
		tp[n] = '\0';
		sum = 0;
		dfs(0, 0);
		printf("Case #%d: %04d\n", j, sum);
	}
	return 0;
}