#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

class Painter
{
public:
	int S,D,K;
	Painter(int s,int d,int k):S(s),D(d),K(k){}
};

vector< pair<int,int> > PsK[301];

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		int n;
		scanf("%d",&n);
		map<string,int> Kolory;
		int NrK = 0;
		vector<Painter> Ps;

		for (int i=0;i<n;i++)
		{
			char Tekst[20];
			int Skad,Dokad;
			scanf("%s%d%d",Tekst,&Skad,&Dokad);
			string Temp = Tekst;
			if (Kolory.find(Temp) == Kolory.end())
				Kolory[Temp] = NrK++;
			Ps.push_back( Painter(Skad,Dokad,Kolory[Temp]) );
		//	printf("%d %d %d\n",Ps[Ps.size()-1].S,Ps[Ps.size()-1].D,Ps[Ps.size()-1].K);
		}

		for (int i=0;i<NrK;i++)
			PsK[i].clear();

		for (int i=0;i<Ps.size();i++)
			PsK[ Ps[i].K ].push_back( make_pair( Ps[i].S, Ps[i].D ) );

	//	for (int i=0;i<NrK;i++)
	//		printf("%d\n",PsK[i].size());

		vector<pair<int,int> > T;
		int TheBest = n+1;

		for (int f=0;f<NrK;f++)
			for (int g=f;g<NrK;g++)
				for (int h=g;h<NrK;h++)
				{
					T.clear();
					for (int i=0;i<PsK[f].size();i++)
						T.push_back( PsK[f][i] );
					if(f!=g)
					for (int i=0;i<PsK[g].size();i++)
						T.push_back( PsK[g][i] );
					if(g!=h)
					for (int i=0;i<PsK[h].size();i++)
						T.push_back( PsK[h][i] );
					sort( T.begin(), T.end() );


					int FUn = 1;
					int MG = 10000;
					int NrUsed = 0;
					int Ind = 0;

					while (FUn <= MG)
					{
						int NajD = -1;
						while (Ind<T.size() && T[Ind].first<=FUn)
						{
							NajD = max(NajD, T[Ind].second);
							Ind++;
						}
						if (NajD == -1)
							break;
						FUn = NajD+1;
						NrUsed++;
					}
					if (FUn>MG)
						TheBest = min(TheBest,NrUsed);
				}
		

		if (TheBest == n+1)
			printf("Case #%d: IMPOSSIBLE\n",L);
		else
			printf("Case #%d: %d\n",L,TheBest);
	}

	return 0;
}
