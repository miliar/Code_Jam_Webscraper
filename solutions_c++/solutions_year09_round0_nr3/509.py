#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

char w[20] = "welcome to code jam";
char str[502];
vector <int> dyn;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++)
	{
		gets(str);
		int len = strlen(str);
		dyn.assign(len, 0);
		for(int j = 0; j < len; j++)
			if(str[j] == 'w')
				dyn[j] = 1;
		for(int j = 1; j < 19; j++)
		{
			int sum = 0;
			for(int k = 0; k < len; k++)
			{
				sum += dyn[k];
				sum %= 10000;
				dyn[k] = 0;
				if(w[j] == str[k])
					dyn[k] = sum;
			}
		}
		int ans = 0;
		for(int j = 0; j < len; j++)
		{
			ans += dyn[j];
			ans %= 10000;
		}
		printf("Case #%d: %.4d\n", i + 1, ans);
	}
	return 0;
}