//Arek Wróbel - skater
#include <cstdio>
using namespace std;

const char w[20]="welcome to code jam"; //19 liter
char s[501];
int tab[500][19];
int wy;
int pom;

char c;
int main()
{
	int n;
	scanf("%d%c", &n);
	for (int lpt=1; lpt<=n; ++lpt)
	{
		//wej
		gets(s);
		//prog
		//reset
		for (int i=0; s[i]!=0; ++i)
			for (int j=0; j<19; ++j)
				tab[i][j]=0;
		//dynamik
		//1 linia
		for (int i=0; s[i]!=0; ++i)
			if (s[i]=='w') tab[i][0]=1;
		//nastepne linie
		for (int i=0; i<18; ++i)
		{
			pom=tab[0][i];
			for (int j=1; s[j]!=0; ++j)
			{
				if (s[j]==w[i+1]) tab[j][i+1]=pom;
				if (s[j]==w[i]) pom+=tab[j][i];
			}
		}
		
		/*for (int j=0; j<19; ++j)
		{
			for (int i=0; s[i]!=0; ++i)
			{
				printf("%3d ", tab[i][j]);
			}
			printf("\n");
		}*/
		wy=0;
		for (int i=0; s[i]!=0; ++i)
			wy+=tab[i][18];
		//wyj
		printf("Case #%d: ", lpt);
		if (wy/1000==0) printf("0");
		if (wy/100==0) printf("0");
		if (wy/10==0) printf("0");
		printf("%d\n", wy%10000);
	}
	return 0;
}
