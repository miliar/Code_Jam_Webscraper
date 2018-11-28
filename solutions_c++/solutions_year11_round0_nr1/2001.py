#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
struct Robot {
	char color;
	int position;
};
int main()
{
	int N, T;
	fin>>T;
	int i,j,k,m,l;
	j=0;
	k=0;
	m=0;
	l=0;
	int totaltime=0;
	Robot bot[101];
	int posO=0;
	int posB=0;
	int lastPositionO=0;
	int lastPositionB=0;
	char temp;
	for (i=0;i<T;i++)
	{
		fin>>N;
		for (j=0;j<N;j++)
		{
			fin>>bot[j].color;
			fin>>bot[j].position;
		}
		totaltime=0;
		lastPositionO=0;
		lastPositionB=0;
		posB=0;
		posO=0;
		for (j=0;j<N;j++)
		{
			if (bot[j].color=='O')
			{
				int time=abs(bot[j].position-lastPositionO)-posO;
				if (time>0)
				{
					totaltime+=time;
					posB+=time;
					lastPositionO=bot[j].position;
					posB++;
					totaltime++;
				}
				else
				{
					totaltime+=0;
					posB+=0;
					lastPositionO=bot[j].position;
					posB++;
					totaltime++;
				}
				posO=0;
			}
			if (bot[j].color=='B')
			{
				int time=abs(bot[j].position-lastPositionB)-posB;
				if (time>0)
				{
					totaltime+=time;
					posO+=time;
					lastPositionB=bot[j].position;
					posO++;
					totaltime++;
				}
				else
				{
					totaltime+=0;
					posO+=0;
					lastPositionB=bot[j].position;
					posO++;
					totaltime++;
				}
				posB=0;
			}
		}
		fout<<"Case #"<<i+1<<": "<<totaltime-1<<endl;
	}

	return 0;
}