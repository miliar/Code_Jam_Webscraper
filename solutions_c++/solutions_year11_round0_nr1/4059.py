#include <iostream>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstring>
using namespace std;

int getTime(char *ch)
{
	int cases;
	stringstream ss;
	ss<<ch;
	ss>>cases;
	int BPos=1;
	int OPos=1;
	int prevOw=1;
	int prevBw=1;
	int freemB=0;
	int freemO=0;
	int atime;
	int time = 0;
	int tempPos=0;
	for(int l=0;l<cases;l++)
	{
		char cc;
		ss>>cc;
		if(cc=='O')
		{
			atime=time;
			prevOw=OPos;
			ss>>tempPos;
			//string tmp=ch[l+1];
			//cout<<tempPos<<endl;
			if(OPos > tempPos)
			{
				int temp2=OPos - tempPos-freemB;
				if(temp2>0)
				time=time+temp2;
			}
			else
			{
				int temp2=tempPos - OPos -freemB;
				if(temp2>0)
				time=time+temp2;
			}
			freemB=0;
			time=time+1;
			freemO=freemO+time-atime;	
			OPos=tempPos;
		}
		else
		{
			atime=time;
			ss>>tempPos;
			prevBw=BPos;
			if(BPos > tempPos)
			{	
				int temp2=BPos - tempPos - freemO;
				if(temp2>0)
				time=time+temp2;
			}
			else
			{
				int temp2=tempPos - BPos -freemO;
				if(temp2>0)
				time=time+temp2;
			}
			freemO=0;
			time=time+1;
			freemB=freemB+time-atime;
			BPos = tempPos;
		}
	}
	
	return time;
}
main()
{
	int n;
	string s;
	char name[500];
	//cin.ignore();
	ifstream inp;
	inp.open("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
	inp>>n;
	inp.getline(name,499);
	
	
	for(int i=0;i<n;i++)
	{
		inp.getline(name,499);
		//cout<<i<<" th line is : "<<name<<endl;
		out<<"Case #"<<i+1<<": ";
		int tm=getTime(name);
		out<<tm<<endl;
	}
}