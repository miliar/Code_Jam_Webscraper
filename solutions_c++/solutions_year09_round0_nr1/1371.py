#include<cstdio>
#include<cstring>

long long ans;

char words[5002][30];
int words_matches[5002];

char tokens[30][30];

int l, d, n;
char test_case[15*26 + 15*3];

void get_tokens(char* word)
{
	int i = 0;
	int new_token_pos = 0;
	for(int j = 0; j < l; j++)
	{
		if (word[i] != '(') 
		{
			tokens[j][0] = word[i];
			tokens[j][1] = '\0';
			new_token_pos = 0;
			i++;
		}
		else
		{
			i++;
			for(;;i++) 
			{

				if (word[i] != ')')
				{
					tokens[j][new_token_pos] = word[i];
					new_token_pos++;
				}
				else
				{
					tokens[j][new_token_pos] = '\0';
					i++;
					new_token_pos = 0;
					break;
				}
			}
		}
	}
}
int contains(char *s, char symbol)
{
	int len = strlen(s);
	for(int i = 0; i < len; i++)
	{
		if(s[i] == symbol) 
		{
			return 1;
		}
	}
	return 0;
}
int solve(char * test_word)
{
	int ans = 0;
	memset(words_matches, 0, sizeof(words_matches));
	get_tokens(test_word);
	for(int i = 0; i < d; i++)
	{
		for(int j = 0; j < l; j++)
		{
			if(!contains(tokens[j], words[i][j])) 
			{
				words_matches[i] = 1;
				break;
			}
		}
	}
	for(int i = 0; i < d; i++) 
	{
		if (words_matches[i] == 0)
		{
			ans++;
		}
	}
	return ans;
}
int main()
{
	freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
	scanf("%d %d %d\n", &l, &d, &n);
	for(int i = 0; i < d; i++)
	{
		scanf("%s\n", words[i]);
	}
	for(int i = 0; i < n; i++)
	{
		scanf("%s", test_case);
		printf("Case #%d: %d\n", i+1, solve(test_case));
	}
	return 0;
}
