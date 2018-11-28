#include<string>
#include<vector>
#include<fstream>
#include<cstdlib>
#include<iostream>
#define mp make_pair
#define pb push_back
using namespace std;

vector< pair<int,int> > l;
vector<int> lo,lb;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	string line;

	int t;
	getline(in,line);
	t=atoi(line.c_str());
	
	for(int i=0;i<t;i++)
	{
		getline(in,line);
		string s1="";
		int ind=0;
		while(line[ind]!=' ')
		{
			s1+=line[ind];
			++ind;
		}
		int n=atoi(s1.c_str());
		++ind;
		for(;;)
		{
			char tip=line[ind];
			ind+=2;
			s1="";
			while(ind<(int) line.size() && line[ind]!=' ')
			{
				s1+=line[ind];
				++ind;
			}
			int poz=atoi(s1.c_str());
			if(tip=='O')
			{
				l.pb(mp(0,poz));
				lo.pb(poz);
			}
			else
			{
				l.pb(mp(1,poz));
				lb.pb(poz);
			}
			if(ind>=(int) line.size())
				break;
			++ind;
		}
		
		int to,tb,t=0,indexo=-1,indexb=-1;
		int sizeo=(int) lo.size();
		int sizeb=(int) lb.size();
		if(sizeo>0)
			to=t+lo[0]-1;
		if(sizeb>0)
			tb=t+lb[0]-1;
		for(int j=0;j<(int) l.size();j++)
		{
			pair<int,int> p;
			p=l[j];
			if(p.first==0) //orange
			{
				if(t<=to)
					t=to;
				else
					to=t;
				++t;
				++to;
				++indexo;
				if(indexo<sizeo)
				{
					if(lo[indexo]<=lo[indexo+1])
						to+=lo[indexo+1]-lo[indexo];
					else
						to+=lo[indexo]-lo[indexo+1];
				}
			}
			else //blue
			{
				if(t<=tb)
					t=tb;
				else
					tb=t;
				++t;
				++tb;
				++indexb;
				if(indexb<sizeb)
				{
					if(lb[indexb]<=lb[indexb+1])
						tb+=lb[indexb+1]-lb[indexb];
					else
						tb+=lb[indexb]-lb[indexb+1];
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<t<<"\n";
		l.clear();
		lo.clear();
		lb.clear();
	}
	in.close();
	out.close();
}

