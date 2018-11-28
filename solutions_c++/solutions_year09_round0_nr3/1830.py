#include <iostream>
#include <vector>
#include <string>
using namespace std;

char s[550];
int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int n;
	scanf("%d\n", &n);
	string pat = "welcome to code jam";
	for (int test = 1; test <= n; test ++)
	{
		gets(s);
		int len = strlen(s);
		vector <vector <long long> > arr(len+1,vector <long long>(pat.length()+1,0));
		//for (int i = 0; i < len+1; i ++)
		//	arr[i][0] = 1;
		for (int i = 1; i <= len; i ++)
			for (int j = 1; j <= pat.size(); j ++)
				if (s[i-1] == pat[j-1])
				{
					if (j == 1)
						arr[i][j] = 1;
					else

						for (int k = 0; k < i; k ++)
							arr[i][j] += arr[k][j-1]%10000;
				}
		int ans = 0;
		for (int i = 1; i <= len; i ++)
			ans += arr[i][pat.size()];
		ans %= 10000;
		printf("Case #%d: %04d\n",test,ans);

	}
	return 0;
}