//Arek Wróbel - skater
#include <cstdio>
#include <algorithm>
using namespace std;

int tab[22];
int poz, poz2, poz3;

int dlug;
char s[22];

inline bool cmp(const int &a, const int &b)
{
	return a>b;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int lpt=1; lpt<=t; ++lpt)
	{
		for (int i=0; i<22; ++i)
			tab[i]=0;
		for (int i=0; i<22; ++i)
			s[i]=0;
		dlug=0;
		//wej
		scanf("%s", s);
		//opr. wej
		while (s[dlug]!=0)
			++dlug;
		for (int i=0; i<dlug; ++i) tab[i]=s[dlug-1-i]-'0';
		//prog
		//gdzie pierwsza malejaca
		poz=1;
		poz2=-1;
		
		while (poz<dlug)
		{
			if (tab[poz]<tab[poz-1]) break;
			++poz;
		}
		if (poz==dlug) //jezeli cyfry sa malejaco (dodac zero)
		{
			sort(tab, tab+dlug, cmp);
			tab[dlug]=tab[dlug-1];
			tab[dlug-1]=0;
			++dlug;
			//jesli zero na pocz.
			if (tab[dlug-1]==0)
			{
				poz3=-1;
				for (int i=dlug-1; i>=0; --i)
					if (tab[i]>0 && (poz3==-1 || tab[i]<tab[poz3])) poz3=i;
				swap(tab[dlug-1], tab[poz3]);
			}
		} else
		{
			for (int i=0; i<poz; ++i)
			{
				//if (tab[i]>tab[poz] && (poz==-1 || tab[i]<tab[poz2])) poz2=i;
				if (tab[i]>tab[poz]) {
					poz2=i;
					break;
				}
			}
			swap(tab[poz], tab[poz2]);
			sort(tab, tab+poz, cmp);
		}
		//for (int i=0; i<dlug; ++i) printf("%d: %d\n", i, tab[i]);
		//opr. wyj
		for (int i=0; i<dlug; ++i) s[dlug-1-i]=tab[i]+'0';
		//wyj
		printf("Case #%d: %s\n", lpt, s);
	}
	return 0;
}
