#include <iostream>
#include <string>
#define LEN 16
#define MAX_D 5001
using namespace std;

int l, d, n;
string str[MAX_D], word[LEN];

bool search(int i, int j)
{
	int k;
	for (k = 0; k < word[j].length(); ++k)
	{
		if (str[i][j] == word[j][k])
		{
			return true;
		}
	}
	return false;
}

int solve(string temp)
{
	int i, j, result;
	bool res, t = false;
	i = 0;
	
	//分节存储
	for (j = 0; temp[j]; ++j)
	{
		if (temp[j] == '(')
		{
			t = true;
			continue;
		}
		if (temp[j] == ')')
		{
			++i;
			t = false;
			continue;
		}
		if (t)
		{
			word[i] += temp[j];
		}
		else
		{
			word[i++] += temp[j];
		}
	}

	result = 0;

	for (i = 0; i < d; ++i)
	{
		res = true;
		for (j = 0; j < l; ++j)
		{
			if (!search(i, j))
			{
				res = false;
				break;
			}
		}
		if (res)
		{
			++result;
		}
	}

	return result;
}

int main()
{
	int i, j;
	string tempStr;
	freopen("A-large.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	while (cin >> l >> d >> n)
	{
		//保存单词
		for (i = 0; i < d; ++i)
		{
			cin >> str[i];
		}

		//保存外语
		for (i = 1; i <= n; i++)
		{
			cin >> tempStr;
			//处理
			cout << "Case #" << i << ": " << solve(tempStr) << endl;
			for (j = 0; j < l; j++)
			{
				word[j] = "";
			}
		}
	}
	return 0;
}