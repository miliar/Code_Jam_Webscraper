#include <iostream>
#include <string>
using namespace std;

#define ONLINEJUDGE
#define MAXL 600

char szBuf[MAXL];
string str;
const string Token = "welcome to code jam";

int F[MAXL][50];
char Precede[50];

void BuildPrecede()
{
	int i, j;
	for(i = Token.length() - 1; i > 0 ; i--)
	{
		Precede[i] = Token[i - 1]; 
	}
}

int main()
{
#ifdef ONLINEJUDGE
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif

	int iCaseTimes;
	int i, j, k, m;
	scanf("%d", &iCaseTimes);
	getchar();
	
	BuildPrecede();
	for(k = 0; k < iCaseTimes; k++)
	{
		gets(szBuf);
		str = szBuf;

		memset(F, 0, sizeof(F));

		for(i = str.length() - 1; i >= 0; i--)
		{
			if(str[i] == 'm')
			{
				F[i][Token.length() - 1] = 1;
			}
			for(m = 0; m < i; m++)
			{
				for(j = 1; j < Token.length(); j++)
				{
					if(F[i][j] == 0) continue;

					if(Precede[j] == str[m])
					{
						F[m][j - 1] = (F[m][j - 1] + F[i][j]) % 10000;
					}
				}
			}
		}

		int iRet = 0;
		for(i = 0; i < str.length(); i++)
		{
			if(str[i] == 'w')
				iRet = (iRet + F[i][0]) % 10000;
		}
		printf("Case #%d: ", k + 1);
		char Output[20];
		sprintf(Output, "%d", iRet);
		string str3 = Output;
		for(i = str3.length(); i < 4; i++)
			printf("0");
		printf("%s\n", str3.c_str());

	}
	return 0;
}

