#include <iostream>
#include <vector>

using namespace std;

struct akcja
{
	char robot;
	int nrPozycji;
	akcja() {}
	akcja(char robot, int nrPozycji) : robot(robot),nrPozycji(nrPozycji) {}
};

typedef vector<int> VI;
typedef vector<akcja> VA;

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int N; cin>>N;
		int bluePoz=1,orangePoz=1;
		int blueNr=0,orangeNr=0;

		VA Akcje(N); VI Orange,Blue;
		for (int i=0; i<N; ++i)
		{
			char robot; int poz;
			cin>>robot>>poz;
			if (robot=='O')
			{
				Orange.push_back(poz);
				Akcje[i]=akcja(robot,(int)Orange.size()-1);
			}
			else
			{
				Blue.push_back(poz);
				Akcje[i]=akcja(robot,(int)Blue.size()-1);
			}
		}

		int blueIle=(int)Blue.size(),orangeIle=(int)Orange.size();
		int licznik=0;

		for (int i=0; i<N; ++i)
		{
			while (true)
			{
				bool next=false;
				++licznik;
				if (blueNr<blueIle)
				{
					int docPoz=Blue[blueNr];
					if (bluePoz<docPoz) ++bluePoz;
					else if (bluePoz>docPoz) --bluePoz;
					else if (Akcje[i].robot=='B')
					{
						++blueNr;
						next=true;
					}
				}
				if (orangeNr<orangeIle)
				{
					int docPoz=Orange[orangeNr];
					if (orangePoz<docPoz) ++orangePoz;
					else if (orangePoz>docPoz) --orangePoz;
					else if (Akcje[i].robot=='O')
					{
						++orangeNr;
						next=true;
					}
				}
				if (next) break;
			}
		}
		cout<<"Case #"<<test<<": "<<licznik<<endl;
	}

	return 0;
}