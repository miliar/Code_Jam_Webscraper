//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

char words[10000][16];
int  len[10000];
bool possible[10000];
int  nWords;
char l[32];
int  point[10000];

bool currentWordHave[256];

bool currentWordSetHave(char c)
{
	for (int i = 0; i < nWords; ++i)
	{
		if (possible[i])
		{
			for (int j =0; j < len[i]; ++j)
			{
				if (words[i][j] == c)
					return true;
			}
		}
	}
	return false;
}

// init for choose the i-th word
void init(int x)
{
	for (int i = 0; i < nWords; ++i)
	{
		if (len[i] != len[x])
			possible[i] = false;
		else possible[i] = true;
	}
	memset(currentWordHave, 0, sizeof(currentWordHave));
	for (int i=0; i<len[x]; ++i)
	{
		currentWordHave[words[x][i]] = 1;
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T, t, m;
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		scanf("%d %d", &nWords, &m);

		for (int i = 0; i < nWords; ++i)
		{
			scanf("%s", words[i]);
			len[i] = strlen(words[i]);
		}

		for (int i = 0; i < m; ++i)
		{
			scanf("%s", l);
			int maxPoint = -1;
			int maxIndex = -1;
			for (int j = 0; j < nWords; ++j)
			{
				point[j] = 0;
				init(j);
				for (int k = 0; k < 26; ++k)
				{
					char letter = l[k];
					if (currentWordSetHave(letter))
					{
						if (currentWordHave[letter])
						{					
							// OK, reveal letters							
							for (int x = 0; x < len[j]; ++x)
							{
								if (words[j][x] == letter)
								{
									for (int y = 0; y < nWords; ++y)
									{
										if (possible[y] && words[y][x] != letter)
										{
											possible[y] = false;
										}
									}
								}
							}
							
							bool pos[10] = {0};
							for (int x = 0; x < len[j]; ++x)
								if (words[j][x] == letter)
									pos[x] = true;

							for (int x = 0; x < nWords; ++x)
							{
								if (possible[x])
								for (int y = 0; y < len[x]; ++y)
								{
									if (!pos[y] && words[x][y] == letter)
									{
										possible[x] = false;
											break;
									}
								}
							}
						} else
						{
							++point[j];
							for (int x = 0; x < nWords; ++x)
							{
								for (int y = 0; y < len[x]; ++y)
								{
									if (letter == words[x][y])
									{
										possible[x] = false;
										break;
									}
								}
							}
						}
					}
				}
				if (maxPoint < point[j])
				{
					maxPoint = point[j];
					maxIndex = j;
				}
			}
			printf ("%s", words[maxIndex]);
			if (i == m-1)
				printf("\n");
			else printf(" ");
		}
	}
	return 0;
}