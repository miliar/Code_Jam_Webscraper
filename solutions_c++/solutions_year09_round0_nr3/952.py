#include <cstdio>
#include <vector>
#include <set>
#include <string>

using namespace std;

string pattern = "welcome to code jam";

int solve(string inp)
{
//	if (inp.length() <= pattern.length())
//		return 0;

	int cases[50][1500] = {0};
	cases[0][0] = 1;

	for(int i = 0; i < pattern.length(); ++i)
	{
		for(int j = 0; j < inp.length(); ++j)
		{
			if (inp[j] == pattern[i])
			{
				for(int k = 0; k  <= j; ++k)
				{
					cases[i+1][j+1] = (cases[i+1][j+1] + cases[i][k]) % 10000;
				}
			}
//			printf("%5d", cases[i+1][j]);
		}
//		printf("%5d\n", cases[i+1][inp.length()]);
	}

	int result = 0;
	for(int i = 0; i <= inp.length(); ++i)
	{
		result = (result + cases[pattern.length()][i])%10000;
	}

	return result;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("D:/downloads/C-large.in", "r", stdin);
	freopen("C:/Users/kiheon/Desktop/output.txt", "w", stdout);

	char inp[2048];
	int z;
	scanf("%d", &z);
	gets(inp);
	for(int i = 0; i < z; ++i)
	{
		gets(inp);

		printf("Case #%d: %04d\n", i+1, solve(inp));
	}
}