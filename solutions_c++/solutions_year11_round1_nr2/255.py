#include "stdio.h"
#include "stdlib.h"
#include "memory.h"
#include "string.h"

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>(0)?(x):-(x))

typedef struct  
{
	char text[11];
	int id;
}Sslovo;

Sslovo *longest(Sslovo *words, int size, int poss, char *guess, int *length)
{
	int i,j,k,l,m;
	int nmax=-1;
	int idmax = -1;
	bool *bRuledOut;
	int nRuledOut;
	int bad;
	bRuledOut = new bool[poss];
	int charCntBu[26];
	int charCnt[26];
	memset(charCntBu, 0, sizeof(charCntBu));
	int goodToGo;
	for (i=0;i<poss;++i)
	{
		for (j=0;j<size;++j)
		{
			++charCntBu[words[i].text[j]-'a'];
		}
	}
	if (poss==1)
	{
		*length = 0;
		return &words[0];
	}
	for (i=0;i<poss;++i)
	{
		memset(bRuledOut, 0, sizeof(bool)*poss);
		memcpy(charCnt, charCntBu, sizeof(charCnt));
		nRuledOut = 0;
		bad = 0;
		goodToGo = size;
		for (j=0;j<26 && (nRuledOut<poss-1 || goodToGo>0);++j)
		{
			if (charCnt[guess[j]-'a']>0)
			{
				if (strchr(words[i].text, guess[j])==NULL)
				{
					++bad;
					for (k=0;k<poss;++k)
					{
						if ((bRuledOut[k] == false) && (strchr(words[k].text, guess[j])!=NULL))
						{
							++nRuledOut;
							bRuledOut[k] = true;
							for (l=0;l<size;++l)
							{
								--charCnt[words[k].text[l]-'a'];
							}
						}
					}
				}
				else
				{
					for (l=0;l<size;++l)
					{
						if (words[i].text[l] == guess[j])
						{
							--goodToGo;
							for (k=0;k<poss;++k)
							{
								if ((bRuledOut[k] == false) && (words[k].text[l] != guess[j]))
								{
									++nRuledOut;
									bRuledOut[k] = true;
									for (m=0;m<size;++m)
									{
										--charCnt[words[k].text[m]-'a'];
									}
								}
							}
						}
						else
						{
							for (k=0;k<poss;++k)
							{
								if ((bRuledOut[k] == false) && (words[k].text[l] == guess[j]))
								{
									++nRuledOut;
									bRuledOut[k] = true;
									for (m=0;m<size;++m)
									{
										--charCnt[words[k].text[m]-'a'];
									}
								}
							}
						}
					}
				}
			}
		}
		if (bad>nmax)
		{
			nmax = bad;
			idmax = i;
		}
	}
	delete []bRuledOut;
	*length = nmax;
	return &words[idmax];
}

void main(int argc, char **argv)
{
	FILE *f;
	int t,k,i;
	Sslovo *words[11];
	int poss[11];
	char one[11];
	int nWordCnt,cases;
	char guess[27];
	for (i=1;i<=10;++i)
	{
		words[i] = new Sslovo[10000];
	}
	fopen_s(&f, argv[1], "rb");
	fscanf_s(f, "%d", &t);
	for (k=1;k<=t;++k)
	{
		printf("Case #%d: ",k);
		fscanf_s(f,"%d %d\n", &nWordCnt, &cases);
		memset(poss, 0, sizeof(poss));
		for (i=0;i<nWordCnt;++i)
		{
			fscanf_s(f, "%s\n", one, 11);
			strcpy_s(words[strlen(one)][poss[strlen(one)]].text, 11, one);
			words[strlen(one)][poss[strlen(one)]].id = i;
			++poss[strlen(one)];
		}
		while(cases--)
		{
			fscanf_s(f, "%s\n", guess, 27);
			Sslovo *szLongest;
			Sslovo *tmp;
			int longer=-1;
			int lon;
			for (i=1;i<=10;++i)
			{
				if (poss[i]>0)
				{
					tmp = longest(words[i], i, poss[i], guess, &lon);
					if ((lon == longer && tmp->id<szLongest->id) || (lon>longer))
					{
						longer = lon;
						szLongest = tmp;
					}
				}
			}
			printf("%s", szLongest->text);
			if (cases>0)
				printf(" ");
		}
		printf("\n");
	}
	fclose(f);
}