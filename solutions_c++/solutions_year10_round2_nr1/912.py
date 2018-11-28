#include <fstream>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>

std::vector<std::string> StringSplit(const std::string &string, const std::string &delim, int pos = 0)
{
	int lastPos = 0;
	std::vector<std::string> splitted;
	do
	{
		pos = string.find(delim, pos+1);
		std::string section(string, lastPos, pos-lastPos);
		lastPos = pos+1;
		splitted.push_back(section);
	}while(pos != -1);
	return splitted;
}

int main()
{
	std::fstream file("file.in");
	if (!file.is_open()){
		std::cout<<"Could not find file";
		return -1;
	}
	std::string num, exist, needed, output;
	std::vector<std::string> vneed, vexist;
	file >> num;
	int numTrials = atoi(num.c_str()), numExist = 0, numNeeded = 0;
	for (int i = 0; i < numTrials; ++i){
		int ans=0;
		file >> exist;
		numExist = atoi(exist.c_str());
		file >> needed;
		numNeeded = atoi(needed.c_str());
		for(int c = 0; c < numExist; ++c){
			file >> exist;
			//exist.erase(exist.begin());
			vexist.push_back(exist);
		}
		for(int c = 0; c < numNeeded; ++c){
			file >> exist;
			exist.erase(exist.begin());
			vneed.push_back(exist);
		}
		int casea = 0;
		bool found = false;
		while (vneed.size()){
			
			std::vector<std::string> split = StringSplit(vneed[0],"/");
			for(int x = 0; x < split.size(); ++x){
				std::string curr;
				for (int y = 0;y<=x;++y){
					curr+="/";
					curr+=split[y];
				}
				for (int c = 0; c < vexist.size(); ++c){

					if(curr==vexist[c]){
						found = true;
						break;
					}

				}
				if(!found){
					ans++;
					vexist.push_back(curr);
				}
				found = false;
			}
			vneed.erase(vneed.begin());
		}
		vneed.clear();
		vexist.clear();
		std::stringstream ss;
		ss << "Case #";
		ss << i+1;
		ss << ": ";
		ss << ans;
		ss << "\n";
		output+=ss.str();
	}
	file.close();
	std::fstream file2("file.out", std::ios::out);
	file2 << output;
	file2.close();
	return 0;
}