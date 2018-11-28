#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctime>

//ejp mysljylc kd kxveddknmc re jsicpdrysi
//our language is impossible to understand
//0,      0,      101,    115,    111,    0,      0,      0,      100,    117,
//105,    103,    108,    98,     0,      114,    122,    116,    110,    0,
//0,      112,    0,      109,    97,     0,
//rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
//there are twenty six factorial possibilities
//121,    104,    101,    115,    111,    99,     0,      120,    100,    117,
//105,    103,    108,    98,     0,      114,    122,    116,    110,    119,
//0,      112,    102,    109,    97,     0,
//de kr kd eoya kw aej tysr re ujdr lkgc jv
//so it is okay if you want to just give up
//121,    104,    101,    115,    111,    99,     118,    120,    100,    117,
//105,    103,    108,    98,     107,    114,    122,    116,    110,    119,
//106,    112,    102,    109,    97,     0,


void GetGooglerese(char nSize, char* pIn, char* pOut, char* pCharSet)
{
	char	iter;
	char	nPos;

	if(!pIn || !pOut || !pCharSet) return;

	for(iter=0; iter<nSize; iter++)
	{
		if(' ' == pIn[iter])
		{
			continue;
		}
		else
		{
			nPos = pIn[iter]-'a';
		}

		if(0 == pCharSet[nPos])
		{
			pCharSet[pIn[iter]-'a'] = pOut[iter];
		}
	}

	for(iter=0; iter<26; iter++)
	{
		printf("%d,\t", pCharSet[iter]);
	}
	printf("\n");
}

void SetGooglerese(char nSize, char* pIn, char* pOut, char* pCharSet)
{
	char	iter;

	for(iter=0; iter<nSize; iter++)
	{
		pOut[iter] = (' ' == pIn[iter])? ' ' : pCharSet[pIn[iter]-'a'];
	}
}

int main(void)
{
    clock_t				start_time = clock();
	char				iter;
	char				charSet[26] = {
		121,    104,    101,    115,    111,    99,     118,    120,    100,    117,
		105,    103,    108,    98,     107,    114,    122,    116,    110,    119,
		106,    112,    102,    109,    97,     113
	};
	char				strIn[101], strOut[101];
	int					nCounts;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	//memset(charSet, 0, 26*sizeof(char));
	//charSet['q'-'a'] = 'z';

	scanf("%d\n", &nCounts);

	//for(iter=0; iter<nCounts; iter++)
	//{
	//	memset(strIn, 0, 101*sizeof(char));
	//	memset(strOut, 0, 101*sizeof(char));

	//	gets(strIn);
	//	gets(strOut);

	//	GetGoogleErase(strlen(strIn), strIn, strOut, charSet);
	//}

	for(iter=0; iter<nCounts; iter++)
	{
		memset(strIn, 0, 101*sizeof(char));
		memset(strOut, 0, 101*sizeof(char));

		gets(strIn);

		SetGooglerese(strlen(strIn), strIn, strOut, charSet);
		printf("Case #%d: %s\n", iter+1, strOut);
	}	

	fcloseall();
	fprintf(stderr, "Elapsed time : %.3fsec\n", (double)(clock()-start_time)/CLOCKS_PER_SEC);

	return 0;
}