// Was build with STL libraries of standard MS VisualStudio 2005 SP1
// Target application was console win 32 application with multibite character set setting. 
// Used software were licensed to Align Technology Inc

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <math.h>
#define M_PI       3.14159265358979323846

/////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	int numOfCases;
	std::cin >> numOfCases;
	for(int cn = 0; cn < numOfCases; cn++)
	{
		int stop;
		std::cin >> stop;
		int dirA, dirB;
		std::cin >> dirA >> dirB;
		std::map<int, int> events[2];
		for(int i = 0; i < dirA+dirB; i++)
		{
			int block = ((i >= dirA)?1:0);
			int happened[2];
			for(int j = 0; j < 2; j++) 
			{
				int hours;
				std::cin >> hours;
				char stub;
				std::cin.read(&stub, 1);
				int minutes;
				std::cin >> minutes;
				minutes += 60*hours;
				happened[j] = minutes;
			}
			happened[1]+=stop;
			if(events[block].find(happened[0])==events[block].end())
				events[block][happened[0]] = 0;
			events[block][happened[0]]=events[block][happened[0]]+1;
			if(events[1-block].find(happened[1])==events[1-block].end())
				events[1-block][happened[1]] = 0;
			events[1-block][happened[1]]=events[1-block][happened[1]]-1;
		}
		int amin[2]={0, 0};
		int cur[2] ={0,0};
		for(int j = 0; j <2; j++)
		{
			for(std::map<int, int>::const_iterator i=events[j].begin(); i!=events[j].end();++i)
			{
				cur[j]+=i->second;
				//std::cout << i->first << ":" << i->second << "\n";
				if(cur[j] > amin[j])
					amin[j] = cur[j];
			}
		}
		std::cout << "Case #" << (cn+1) << ": "<< amin[0] << " " << amin[1] <<"\n";
	}
	return 0;
}

