//Arek Wróbel - skater
#include <cstdio>
using namespace std;

char s[61];
int dlug;

char cyf[60];
int ilec;

long long int wy;
char lit[300];
bool czy;
int pom;

long long int pot(const int &a, const int &b)
{
	long long int wyn=1;
	for (int i=0; i<b; ++i) wyn=wyn*a;
	return wyn;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		//wej
		scanf("%s", s);
		//opr. wej
		ilec=0;
		for (int i=0; i<60; ++i)
			cyf[i]=0;
		for (int i=0; i<300; ++i)
			lit[i]=0;
		for (int i=0; s[i]!=0; ++i)
		{
			czy=true;
			for (int j=0; j<ilec; ++j)
				if (s[i]==cyf[j]) czy=false;
			if (czy) cyf[ilec++]=s[i];
		}
		//prog
		
		//bez zera na poczatku
		pom=cyf[0];
		cyf[0]=cyf[1];
		cyf[1]=pom;
		//tworzenie lit[]
		for (int i=0; i<ilec; ++i)
			lit[cyf[i]]=i;
		//tworzenie dlug
		for (dlug=0; s[dlug]!=0; ++dlug);
		//obliczanie wyniku
		int wyk=0;
		wy=0;
		for (int i=dlug-1; i>=0; --i)
		{
			wy=wy+(pot(ilec, wyk)*lit[s[i]]);
			++wyk;
		}
		//jesli takie same
		if (wy==0)
		{
			wy=pot(2, dlug)-1;
		}
		//wyj
		printf("Case #%d: ", lpt);
		printf("%I64d\n", wy);
	}
	return 0;
}
