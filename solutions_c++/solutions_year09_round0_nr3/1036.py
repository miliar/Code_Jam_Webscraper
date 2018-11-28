#include <cstdio>
#include <string>

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

char temp[5000];
std::string scanString()
{
	gets(temp);
	return std::string(temp);
}

std::string str;
std::string substr = std::string("welcome to code jam");
int ans[5000][20];
int main()
{
	OpenFiles();
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		memset(ans, 0, sizeof(ans));
		str = "$" + scanString();

		ans[0][0] = 1;
		for (int i = 1; i < str.size(); i++)
		{
			for (int j = 0; j <= substr.size(); j++)
				ans[i][j] = ans[i-1][j];
			for (int j = 0; j < substr.size(); j++)
				if (str[i] == substr[j])
					ans[i][j+1] += ans[i-1][j];
			
			for (int j = 0; j <= substr.size(); j++)
				ans[i][j] %= 10000;			
		}

		printf("Case #%d: %.4d\n", i+1, ans[str.size()-1][substr.size()]);
	}
	
	return 0;
}