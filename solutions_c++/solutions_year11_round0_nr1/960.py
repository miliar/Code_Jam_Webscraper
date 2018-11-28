#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

struct button {
	char col;
	int loc;
};

using namespace std;

int main()
{
	ofstream fout;
	fout.open("output.txt");
	int cases;
	cin>>cases;
	vector<button> fulllist;
	vector<int> olist;
	vector<int> blist;
	char inpc;
	int inpi;
	int bgoal=0;
	int ogoal=0;
	int oloc=1;
	int bloc=1;
	for (int y=0;y<cases;y++)
	{
		fulllist.clear();
		olist.clear();
		blist.clear();
		int steptime;
		int overalltime=0;
		int buttons;
		cin>>buttons;
		oloc=bloc=1;
		ogoal=bgoal=0;
		for (int i=0;i<buttons;i++)
		{
			cin>>inpc;
			cin>>inpi;
			button but;
			but.col=inpc;
			but.loc=inpi;
			fulllist.push_back(but);
			if (inpc=='B') blist.push_back(inpi);
			else olist.push_back(inpi);
		}
		blist.push_back(0);
		olist.push_back(0);
		for (int i=0;i<buttons;i++)
		{
			if (fulllist[i].col=='O')
			{
				steptime = abs(fulllist[i].loc-oloc)+1;
				oloc=fulllist[i].loc;
				ogoal++;
				if (steptime>=abs(blist[bgoal]-bloc)) bloc=blist[bgoal];
				else 
				{
					if (abs(bloc-blist[bgoal]+steptime)<abs(bloc-blist[bgoal]-steptime)) bloc+=steptime;
					else bloc-=steptime;
				}
			}
			else
			{
				steptime = abs(fulllist[i].loc-bloc)+1;
				bloc=fulllist[i].loc;
				bgoal++;
				if (steptime>=abs(olist[ogoal]-oloc)) oloc=olist[ogoal];
				else 
				{
					if (abs(oloc-olist[ogoal]+steptime)<abs(oloc-olist[ogoal]-steptime)) oloc+=steptime;
					else oloc-=steptime;
				}
			}
			overalltime+=steptime;
		}
		fout<<"Case #"<<y+1<<": "<<overalltime<<endl;
	}
	fout.close();
	return 0;
}