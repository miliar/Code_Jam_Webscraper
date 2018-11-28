#include<iostream>
using namespace std;

#define max_word_len 15
#define max_dic_num 5000

class pattern
{
	char letter[max_word_len]['z' + 1];

public:
	pattern(string s, int len)
	{
		int i, j;

		for(i = 0; i < len; i++)
			for(j = 'a'; j <= 'z'; j++)
				letter[i][j] = 0;

		j = 0;

		for(i = 0; i < len; i++)
		{
			if(s[j] == '(')
			{
				while(s[++j] != ')')
					letter[i][s[j]] = 1;
			}
			else
			{
				letter[i][s[j]] = 1;
			}
			j++;
		}
	}

	bool cmp(string s)
	{
		int i;

		for(i = 0; i < s.length(); i++)
			if(letter[i][s[i]] == 0) return false;

		return true;
	}
};

int main()
{
	int l, d, n, i, j, k;
	string s;
	string dic[max_dic_num];

	scanf("%d %d %d ", &l, &d, &n);

	for(i = 0; i < d; i++)
		cin >> dic[i];

	for(i = 1; i <= n; i++)
	{
		k = 0;

		cin >> s;

		pattern p(s, l);

		for(j = 0; j < d; j++)
			if(p.cmp(dic[j])) k++;

		printf("Case #%d: %d\n", i, k);
	}
}
