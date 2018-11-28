#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <cstdlib>


using namespace std;

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int N=0;
		cin>>N;

		vector<char> bot;
		vector<int> job;

		for (int n=0;n<N;n++)
		{
			int j=0;
			char b;
			cin>>b>>j;

			bot.push_back(b);
			job.push_back(j);

		}

		int oi = 1, bi = 1; 
		int cs = 0; 
		int ps = 0;

		cs = job[0]; 
		
		int count = cs;

		if (bot[0]=='O') oi = job[0]; else bi = job[0];

		for (int i=1;i<N;i++)
		{
			if (bot[i]==bot[i-1])
			{
				count+= abs(job[i] - job[i-1]);
				cs += abs(job[i] - job[i-1]);
				count++;
				cs++;
				if (bot[i]=='O') oi = job[i]; else bi = job[i];
			}
			else 
			{
				int ci = bot[i]=='O'?oi:bi;
				int ct = abs(ci - job[i]);

				int s  = ct>cs?cs:ct;
				count += ct - s;
				cs = ct - s;
				count++;
				cs++;
				if (bot[i]=='O') oi = job[i]; else bi = job[i];
				cerr<<"cerr: "<<"ct: "<<ct<<"s: "<<s<<"count: "<<count<<endl;
			}

		}
		
		cout<<"Case #"<<t+1<<": "<<count<<endl;
	
	}//test case for ends

}
