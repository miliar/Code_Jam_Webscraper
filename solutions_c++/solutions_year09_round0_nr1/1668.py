#include <stdio.h>
#include <string.h>

#define ni(x) scanf("%d", &x)
#define ns(x) scanf("%s", x)

char words[5000+4][16];
char parttern[16*30];
char transfer[16][27];

int nwords;
int lwords;

void parse()
{
	memset(transfer, 0, sizeof(transfer));
	int top=0;
	for(int i=0; i<lwords; ++i)
	{
		char c = parttern[top];
		if( 'a'<=c && c<='z')
		{
			transfer[i][parttern[i] - 'a'] = 1;
			++top;
			continue;
		}
		if( c == '(')
		{
			for(++top; parttern[top]!=')'; ++top)
				transfer[i][parttern[top] - 'a'] = 1;
			++top;
			continue;
		}
		puts("fucker!!!");
	}
}

void count(int ks)
{
	int cnt = 0;
	for(int i=0; i<nwords; ++i)
	{
		//match word words[i]
		char* now = words[i];
		int p=0;
		for(p=0; p<lwords; ++p)
		{
			if (!transfer[p][now[p]-'a'] )
				break;
		}
		if(p==lwords)
			++cnt;
	}
	printf("Case #%d: %d\n", ks, cnt);
}

int main()
{
	int npatterns;
	ni(lwords);
	ni(nwords);
	ni(npatterns);
	for(int i = 0; i< nwords; ++i)
		ns(words[i]);

	for(int ks = 1; ks <= npatterns; ++ks)
	{
		ns(parttern);
		parse();
		count(ks);
	}
}
