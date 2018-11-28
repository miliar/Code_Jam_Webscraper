// Marcin Wrochna
// g++ -O2
// IDE: geany
#include <cstdio>
#include <cstring>
#define REP(x,n) for(int x=0; x<(int)(n); ++x)

char s[501];
const char phrase[19+1] = "welcome to code jam";
int dyn[500][19]; //dyn[i][j] = number of matches of phrase<0..j> in s<0..i> mod 10000

void doit() {
	gets(s); //read till newline, don't include the newline
	memset(dyn, 0, sizeof(dyn));
	dyn[0][0] = (s[0]==phrase[0]);
	
	int i;
	for(i=1; s[i]; i++)
	{
		dyn[i][0] = dyn[i-1][0] + (s[i]==phrase[0]);
		for(int j=1; j<19; j++)
		{
			dyn[i][j]=dyn[i-1][j];
			if(s[i]==phrase[j])
			{
				dyn[i][j]+=dyn[i-1][j-1];
				if(dyn[i][j]>=10000) dyn[i][j]-=10000;
			}
		}
	}

	printf("%04d\n", dyn[i-1][18]);
}

int main()
{
	int NCase;
	scanf("%d\n",&NCase);
	REP(ncase,NCase) {
		printf("Case #%d: ", ncase+1);
		doit();
	}

	return 0;
}
