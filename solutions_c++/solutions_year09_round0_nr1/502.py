

#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string words[5001];
char word[2000];
bool isAnswer[5001];

int main()
{
	int i, j, k, t, L, D, N, ca = 0;

	freopen("c:\\A-small-attempt0.in", "r", stdin);
	freopen("c:\\A-small-attempt0.out", "w+", stdout);

	while(scanf("%d%d%d", &L, &D, &N) != EOF)
	{
		for(i = 0;i < D; i++)
		{
			scanf("%s", word);
			words[i] = word;
		}
		
		for(i = 0;i < N; i++)
		{
			scanf("%s", word);
			memset(isAnswer, 1, sizeof(isAnswer));	
			t = 0;
			for(k = 0;k < L; k++)
			{
				string tmp = "";
				if(word[t] == '(')
				{
					t++;
					while(word[t] != ')') tmp += word[t], t++;
					t++;
				}
				else {tmp += word[t]; t++;}

				for(j = 0;j < D; j++)
				{
					if(isAnswer[j])
					{
						string tmp2 = "";
						tmp2 += words[j][k];
						if(tmp.find(tmp2) == string::npos)
							isAnswer[j] = false;
					}
				}
			}

			k = 0;
			for(j = 0;j < D; j++)
			{
				if(isAnswer[j]) k++;
			}
			printf("Case #%d: %d\n", i+1, k);
		}
	}
	return 0;
}

