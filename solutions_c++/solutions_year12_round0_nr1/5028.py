#include <vector>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <stdio.h>
#include <tchar.h>
using namespace std;

#define BOOL int
#define TRUE 1
#define FALSE 0
int readi() { int a; scanf( "%d", &a ); return a; }
char sbuf[100005]; string readstr(){ scanf( "%s", sbuf ); return sbuf; }

char *exmInput  = "yeqzejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char *exmOutput = "aozqour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char transMap[26] = {0};
BOOL Flag[26]={0};

// Don't consider excpetion cases.
void buildTransMap()
{
	char chSrc, chDst; int j;
	for (int i = 0; i < strlen(exmInput); ++i)
	{
		chSrc = exmInput[i]; chDst = exmOutput[i]; j = chSrc - 'a';
		if (chSrc == ' ') 
		{
			continue;
		}
		else if (transMap[j] == 0)
			transMap[j] = chDst;
		else if (transMap[j] != chDst)
		{
			printf("error!");
		}
		Flag[chDst - 'a'] = TRUE;
	}

	for (j = 0; j < 26; j++)
	{
		if (!Flag[j]) printf("%c", j + 'a');
	}
}

void outputTransMap()
{
	for (int i = 0; i < 26; ++i)
	{
		if (transMap[i] != 0)
		    printf("\n%c %c", i + 'a', transMap[i]);
		else
			printf("\n%c %c", i + 'a', '--');
	}
}


 BOOL DEBUGIN = FALSE;
 BOOL DEBUGOUT = FALSE;
int main(int argc, char* argv[])
{
	int N;
	string strTemp;
	char ch;
	if (!DEBUGIN) freopen("A-small-attempt0.in","rt",stdin);
	if (!DEBUGOUT) freopen("A-small-attempt0.out","wt",stdout);

    buildTransMap();	
	//outputTransMap();

	N = readi(); scanf("%c", &ch);
	for (int i = 0; i < N; i++)
	{
    	scanf("%c", &ch);
		if (ch == '\n' || ch == '\r' || ch == EOF) continue;

		printf("Case #%d: ", i + 1);
		while (ch != '\n' && ch != '\r' & ch != EOF)
		{
			if (ch  == ' ') 
			{
				printf(" ");
			}
			else
			{
	     		printf("%c", transMap[ch - 'a']);
			}
			scanf("%c", &ch);
		}
		printf("\n");
	}
	return 0;
}

