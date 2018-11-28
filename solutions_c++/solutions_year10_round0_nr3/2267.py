#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>

int main()
{
	std::fstream file("file.in");
	if (!file.is_open()){
		std::cout<<"Could not find file";
		return -1;
	}
	std::string num, runs, holds, N, group, output;
	file >> num;
	int numTrials = atoi(num.c_str()), numRuns = 0, numHolds = 0, numGroups = 0;
	std::vector<int> groups;
	for (int i = 0; i < numTrials; ++i){
		file >> runs;
		file >> holds;
		file >> N;
		numRuns = atoi(runs.c_str());
		numHolds = atoi(holds.c_str());
		numGroups = atoi(N.c_str());
		for (int j = 0; j < numGroups; ++j){
			file >> group;
			groups.push_back(atoi(group.c_str()));
		}
		int moneyMade = 0;
		for (int j = 0; j < numRuns; ++j){
			int spaceLeft = numHolds;
			
			for (unsigned int k = 0; k < groups.size(); ++k){
				if (groups[0] <= spaceLeft){
					auto front = groups.begin();
					int frontValue = (*front);
					groups.erase(front);
					groups.push_back(frontValue);
					spaceLeft -= frontValue;
					moneyMade += frontValue;
				}else{
					break;
				}
			}
		}
		std::stringstream ss;
		ss << "Case #";
		ss << (i+1);
		ss << ": ";
		ss << moneyMade;
		ss << "\n";
		output += ss.str();
		groups.clear();
	}
	file.close();
	std::fstream file2("file.out", std::ios::out);
	file2 << output;
	file2.close();
	return 0;
}