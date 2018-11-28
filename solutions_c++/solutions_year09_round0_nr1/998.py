#include <cstdio>
#include <string>

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

std::string words[7000];
char str[500];
int l, d, n;

std::string scanString()
{
	gets(str);
	return std::string(str);
}

struct Template
{
	bool mask[20][26];
	int len;
	

	void scan()
	{
		std::string s = scanString();
		len = s.size();
		int pos = 0;
		for (int i = 0; i < s.size(); i++)
		{
			for (int j = 0; j < 26; j++)
				mask[pos][j] = false;

			std::string temp = "";
			if (s[i] == '(')
			{				
				for (i++; s[i] != ')'; i++)
					temp += s[i];
			}
			else
				temp = s[i];

			for (int j = 0; j < temp.size(); j++)
				mask[pos][temp[j] - 'a'] = true;

			pos++;
		}
	}
};

int main()
{
	OpenFiles();
	scanf("%d%d%d\n", &l, &d, &n);
	for (int i = 0; i < d; i++)
		words[i] = scanString();
	Template t;
	for (int i = 0; i < n; i++)
	{
		t.scan();
		int cnt = 0;
		
		for (int j = 0; j < d; j++)
		{
			bool flag = true;
			for (int k = 0; k < l && flag; k++)
			{
				if (!t.mask[k][words[j][k] - 'a'])
					flag = false;
			}

			if (flag)
				cnt++;
		}

		printf("Case #%d: %d\n", i+1, cnt);
	}
	

	return 0;
}