#include <iostream>
#include <string>
#include <string.h>

using namespace std;

string cmp = "welcome to code jam";

int ans;

int len, ll = cmp.length();
char in[1000];
void dfs(int t, int k)
{
	if(k == ll)
	{
		ans ++;
		if(ans >= 10000)
			ans -= 10000;
		return ;
	}

	if(t == len)
		return ;
	

	for(int i = t; i < len; i ++)
	{
		if(in[i] == cmp[k])
			dfs(i+1, k +1);
	}
	return ;
}
int main()
{
    freopen("C-small-attempt0.in.txt", "r", stdin);
    freopen("c-small.txt", "w", stdout);
	int Test = 1, i , j ,T;
	scanf("%d",&Test);
	getchar();
	for(T = 1; T <= Test; T ++)
	{
		gets(in);
		len = strlen(in);
		ans = 0;
		dfs(0, 0);
		printf("Case #%d: ", T);
		if(ans >= 1000)
			printf("%d", ans);
		else if(ans >= 100)
			printf("0%d", ans);
		else if(ans >= 10)
			printf("00%d", ans);
		else 
			printf("000%d", ans);

		printf("\n");
	}
	return 0;
}
