#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
using namespace std;

char robot[110];
int pos[110];
int steps[110];

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t,n;
	int opos,bpos,otime,btime;
	int allstep;
	fin>>t;
	for (int i=0;i<t;i++)
	{
		allstep=0;
		opos=1;
		otime=0;
		btime=0;
		bpos=1;
		fin>>n;
		for (int j=0;j<n;j++)
		{
			fin>>robot[j];
			fin>>pos[j];
		}
		for (int j=0;j<n;j++)
		{
			if (robot[j]=='O')
			{
				if (otime>=abs(pos[j]-opos))
				{
					otime=0;
					btime++;
					allstep+=1;
					opos=pos[j];
				}
				else 
				{
					btime+=abs(pos[j]-opos)+1-otime;
					allstep+=abs(pos[j]-opos)+1-otime;
					otime=0;
					opos=pos[j];
				}
			}
			else			
			{
				if (btime>=abs(pos[j]-bpos))
				{
					btime=0;
					otime++;
					allstep+=1;
					bpos=pos[j];
				}
				else 
				{
					otime+=abs(pos[j]-bpos)+1-btime;
					allstep+=abs(pos[j]-bpos)+1-btime;
					btime=0;
					bpos=pos[j];
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<allstep<<"\n";
		//printf("Case #%d: %d\n",i+1,allstep);
	}
}