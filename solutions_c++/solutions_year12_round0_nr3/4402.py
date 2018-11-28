#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void ReverseString(char* pStart, char* pEnd)
{
      if(pStart != NULL && pEnd != NULL)
      {
            while(pStart <= pEnd)
            {
                  char temp = *pStart;
                  *pStart = *pEnd;
                  *pEnd = temp;

                  pStart ++;
                  pEnd --;
            }
      }
}

char* RightRotateString(char* pStr, unsigned int n)
{
      if(pStr != NULL)
      {
            int nLength = static_cast<int>(strlen(pStr));
            if(nLength > 0 && n > 0 && n < nLength)
            {
                  char* pFirstStart = pStr;
                  char* pFirstEnd = pStr + nLength - 1 - n;
                  char* pSecondStart = pStr + nLength - n;
                  char* pSecondEnd = pStr + nLength - 1;

                  // reverse the first part of the string
                  ReverseString(pFirstStart, pFirstEnd);
                  // reverse the second part of the strint
                  ReverseString(pSecondStart, pSecondEnd);
                  // reverse the whole string
                  ReverseString(pFirstStart, pSecondEnd);
            }
      }

      return pStr;
}

int main()
{
	int T;
	char ch[5];
	//itoa(a, ch, 10);
	int count = 0;
	int n, m;

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);


	scanf( "%d", &T );

	for(int i = 0; i < T; i++)
	{
		scanf("%d%d", &n, &m);
		for(int i = n; i <= m; i++)
		{
			int temp;
			itoa(i, ch, 10);
			char tmpch[5];
			strcpy(tmpch, ch);

			for(int j = 1; j < strlen(ch); j++)
			{
				RightRotateString(tmpch, j);
				temp = atoi(tmpch);
				if(temp > i && temp <= m)
				{
					//printf("%d  %d\n", i, temp);
					count++;
				}
				strcpy(tmpch, ch);
			}
		}
		printf("Case #%d: %d\n", i+1, count);
		count = 0;
	}


	//printf("%d\n", count);
}