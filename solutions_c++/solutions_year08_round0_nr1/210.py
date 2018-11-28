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
		int engCount;
		std::cin >> engCount;
		std::vector<std::string> engines;
		char dropline[1024];
		std::cin.getline(dropline, 1023);
		for(int i = 0; i < engCount; i++)
		{
			char line[1024];
			std::cin.getline(line, 1023);
			engines.push_back(line);
		}
		std::sort(engines.begin(), engines.end());
		int queCount;
		std::cin >> queCount;
		std::cin.getline(dropline, 1023);
		std::vector<int> minSwitches(engCount, 0);
		for(int i = 0; i < queCount; i++)
		{
			char line[1024];
			std::cin.getline(line, 1023);
			std::string key = line;
			int index = std::lower_bound(engines.begin(), engines.end(), key) - engines.begin();
			int minimal = queCount+1;
			for(int i = 0; i < engCount; i++)
			{
				if(i != index && minSwitches[i]<minimal)
					minimal = minSwitches[i];
			}
			minSwitches[index] = minimal+1;
		}
		int minimal = queCount+1;
		for(int i = 0; i < engCount; i++)
		{
			if(minSwitches[i]<minimal)
				minimal = minSwitches[i];
		}
		std::cout << "Case #" << (cn+1) << ": "<< minimal <<"\n";
	}
	return 0;
}

