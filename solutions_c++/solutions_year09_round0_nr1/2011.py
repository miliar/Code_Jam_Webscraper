//Arek Wróbel - skater
#include <cstdio>
using namespace std;

int l, d, n;
char dic[5000][16]={0};
bool tab[5000];
char c;
char przedz[27];
int ilep;
int wy=0;
bool czy;

int main()
{
	scanf("%d%d%d", &l, &d, &n);
	//wczytanie slownika
	for (int i=0; i<d; ++i)
		for (int j=0; j<l; ++j)
			scanf(" %c", &dic[i][j]);
	//przypadki testowe
	for (int lpt=1; lpt<=n; ++lpt)
	{
		for (int i=0; i<d; ++i)
			tab[i]=true;
		for (int i=0; i<l; ++i)
		{
			scanf(" %c", &c);
			if (c=='(')
			{
				ilep=0;
				//wczytanie przedzialu
				while (c!=')')
				{
					scanf("%c", &c);
					przedz[ilep]=c;
					++ilep;
				}
				--ilep;
				//spr
				for (int j=0; j<d; ++j)
				{
					czy=false;
					for (int j2=0; j2<ilep; ++j2)
						if (dic[j][i]==przedz[j2]) czy=true;
					if (czy==false) tab[j]=false;
				}
			} else
			{
				for (int j=0; j<d; ++j)
					if (dic[j][i]!=c)
						tab[j]=false;
			}
		}
		wy=0;
		for (int i=0; i<d; ++i)
			if (tab[i]==true)
				++wy;
		//wyj
		printf("Case #%d: %d\n", lpt, wy);
	}
	return 0;
}
