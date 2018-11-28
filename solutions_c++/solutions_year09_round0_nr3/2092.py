#include<string>
#include<cstdio>

using namespace std;

int n, res[50][510];
string s, txt = "welcome to code jam";

void debug()
{
	putchar('\n');
	for(int i = 0; i < txt.length(); i++)
	{
		for(int j = 0; j < s.length(); j++)
			printf("%d ", res[i][j]);
		putchar('\n');		
	}
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	char tmp[1000];
	scanf("%d\n", &n);
	for(int k = 0; k < n; k++)
	{	
		gets(tmp);
		s = string(tmp);
		for(int i = txt.length(); i >= 0; i--)
			for(int j = s.length(); j >= 0; j--)
				res[i][j] = 0;
		for(int j = s.length(); j >= 0; j--)
			res[txt.length()][j] = 1;
		//debug();
		for(int i = txt.length() - 1; i >= 0; i--)
		{
			for(int j = s.length() - 1; j >= 0; j--)
			{
				res[i][j] += res[i][j + 1];
				if (s[j] == txt[i]) res[i][j] += res[i + 1][j + 1];
				res[i][j] = res[i][j] % 10000;
			}
			//debug();
		}
		printf("Case #%d: %04d\n", k + 1, res[0][0]);
	}
	return 0;
}