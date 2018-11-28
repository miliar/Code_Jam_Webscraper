#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>
#define infile "a1.in"
#define outfile "a1.out"

char word[5010][18];
long len,d,ge;

FILE *fin=fopen(infile,"r"),
	*fout=fopen(outfile,"w");

void init()
{
	long i,j,k;
	fscanf(fin,"%ld%ld%ld",&len,&d,&ge);
	for (i=1; i<=d; ++i)
		fscanf(fin,"%s",word[i]);
}

void work()
{
	long w,i,j,k,result,p;
	bool appear[17][26];
	char s[1000];
	for (w=1; w<=ge; ++w)
	{
		result=0;
		fscanf(fin,"%s",s);
		p=0;
		for (i=0; i<len; ++i)
		{
			for (j=0; j<26; ++j)
				appear[i][j]=false;
			if (s[p]!='(')
			{
				appear[i][s[p]-'a']=true;
				++p;
			}
			else {
				++p;
				while (s[p]!=')')
				{
					appear[i][s[p]-'a']=true;
					++p;
				}
				++p;
			}
		}

		result=0;
		for (i=1; i<=d; ++i)
		{
			++result;
			for (j=0; j<len; ++j)
				if (!appear[j][word[i][j]-'a'])
				{
					--result;
					break;
				}
		}

		fprintf(fout, "Case #%ld: %ld\n",w,result);
	}
	fclose(fin);
	fclose(fout);
}

void output()
{

}

int main()
{
	init();
	work();
	output();	
	return 0;
}