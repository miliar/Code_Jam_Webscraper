#include <iostream>
#include <map>
#include <vector>
using namespace std;

#define MMAX 1440

map<int, vector<int> > tripab;
map<int, vector<int> > tripba;

int traina[MMAX+100];
int trainb[MMAX+100];

int main()
{
	int cc;
	cin>>cc;
	for(int ci=1;ci<=cc;ci++)
	{
		int t;
		int na,nb;
		tripab.clear();
		tripba.clear();
		memset(traina,0,sizeof(traina));
		memset(trainb,0,sizeof(trainb));

		cin>>t>>na>>nb;
		int hh1,mm1,hh2,mm2;
		char c;
		while(na--)
		{
			cin>>hh1>>c>>mm1>>hh2>>c>>mm2;
			tripab[hh1*60+mm1].push_back(hh2*60+mm2+t);
		}
		while(nb--)
		{
			cin>>hh1>>c>>mm1>>hh2>>c>>mm2;
			tripba[hh1*60+mm1].push_back(hh2*60+mm2+t);
		}
		
		int ta=0,tb=0;
		map<int, vector<int> >::iterator mi;
		vector<int>::iterator vi;
		int cta=0,ctb=0;
		for(int m=0;m<MMAX;m++)
		{
			cta+=traina[m];
			ctb+=trainb[m];
			mi=tripab.find(m);
			if(mi!=tripab.end())
			{
				for(vi=mi->second.begin();vi!=mi->second.end();vi++)
				{
					if(cta>0) cta--;
					else ta++;

					trainb[*vi]++;
				}
			}

			mi=tripba.find(m);
			if(mi!=tripba.end())
			{
				for(vi=mi->second.begin();vi!=mi->second.end();vi++)
				{
					if(ctb>0) ctb--;
					else tb++;

					traina[*vi]++;
				}
			}
		}

		cout<<"Case #"<<ci<<": "<<ta<<" "<<tb<<endl;
	}

	return 0;
}
