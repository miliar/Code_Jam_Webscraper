#include <cstdio>
#include <algorithm>
#include <cstring>
#define LLD long long int

using namespace std;

const int P = 2*3*5*7;

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		char Cyfry[100];
		scanf("%s",Cyfry);
		LLD Cyf[100];
		int n = strlen(Cyfry);
		for (int i=0;i<n;i++)
			Cyf[i] = Cyfry[i]-'0';
		
		int Typ[P];
		for (int i=0;i<n;i++)
			Typ[i] = 0;
		LLD All = 0;
		while (Typ[n-1]==0)
		{
			LLD Akt = Cyf[0];
			LLD Wyn = 0;
			int Last = 1;
			for (int i=0;i<n-1;i++)
			{
				if (Typ[i] == 0)
				{
					Akt*=10;
					Akt+=Cyf[i+1];
				}
				else
				{
					if (Last == 1)
						Wyn += Akt;
					else
						Wyn -= Akt;
					Akt = Cyf[i+1];
					Last = Typ[i];
				}


			}
				if (Last == 1)
					Wyn += Akt;
				else
					Wyn -= Akt;
				if (Wyn < 0)
				{
					Wyn %= P;
					Wyn += P;
				}
				if ( (Wyn%2==0) || (Wyn%3==0) || (Wyn%5==0) || (Wyn%7==0))
					All++;
			
			Typ[0]++;
			int W = 0;
			while (Typ[W]==3){Typ[W]=0;Typ[++W]++;}
		}
			printf("Case #%d: %lld\n",L,All);
	}	

	return 0;
}
