#include <cstdio>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main()
{
	int lw;
	scanf("%d",&lw);
	for (int L=1;L<=lw;L++)
	{
		int n;
		char T[200];
		string TT;
		map<string,int> Mapa;

		scanf("%d",&n);getchar();
		vector<string> In;
		for (int i=0;i<n;i++)
		{
			TT.clear();
			char C = getchar();
			while (C!='\n')
			{
				TT.push_back(C);
				C = getchar();
			}
			Mapa[TT] = i;
			In.push_back(TT);
		}
		
		int m;
		scanf("%d",&m);getchar();
		vector<int> Wys[200];
		vector< string > Dane;
		for (int i=0;i<m;i++)
		{
			TT.clear();
			char C = getchar();
			while (C!='\n')
			{
				TT.push_back(C);
				C = getchar();
			}
			Dane.push_back(TT);
			if ( Mapa.find(TT) != Mapa.end() )
				Wys[ Mapa[TT] ].push_back(i);
		}
		for (int i=0;i<n;i++)
			reverse( Wys[i].begin(), Wys[i].end() );
		int Best = 0;
		int Gdzie;
		if (Wys[Best].size() == 0) Gdzie = m+1; else
			Gdzie = Wys[Best][ Wys[Best].size()-1 ];

		for (int i=1;i<n;i++)
		{
			int Akt;
			if (Wys[i].size() == 0) Akt = m+1; else
				Akt = Wys[i][ Wys[i].size()-1 ];
			if (Gdzie < Akt)
			{
				Gdzie = Akt;
				Best = i;
			}
		}
		int Ile = 0;
		for (int i=0;i<m;i++)
		{
			if ( In[ Best ] == Dane[i] )
			{
				Ile++;
				Wys[Best].pop_back();
				int Zly = Best;
				Best = 0;
				Gdzie = 0;
				for (int j=0;j<n;j++)
				{
					if (j==Zly) continue;
					int Akt;
					
					while (Wys[j].size()!=0 && Wys[j][ Wys[j].size()-1 ] < i)
						Wys[j].pop_back();

					if (Wys[j].size() == 0) Akt = m+1; else
						Akt = Wys[j][ Wys[j].size()-1 ];

					if (Gdzie < Akt)
					{
					Gdzie = Akt;
					Best = j;
					}
				}
			}
		}
		printf("Case #%d: %d\n",L,Ile);
	}
}
