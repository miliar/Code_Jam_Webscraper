#include <fstream>
#include <string>
#include <iostream>
#include <sstream>

int main()
{
	std::fstream file("file.in");
	if (!file.is_open()){
		std::cout<<"Could not find file";
		return -1;
	}
	std::string num, snap, flips, output;
	file >> num;
	int numTrials = atoi(num.c_str()), numSnaps = 0, numFlips = 0;
	for (int i = 0; i < numTrials; ++i){
		file >> snap;
		file >> flips;
		numSnaps = atoi(snap.c_str());
		numFlips = atoi(flips.c_str());

		int max = 1 << numSnaps;
		while (numFlips > max)
			numFlips -= max;
		std::stringstream ss;
		ss << "Case #";
		ss << (i+1);
		ss << ": ";
		if (numFlips == max-1){
			ss << "ON";
		}else{
			ss << "OFF";
		}
		ss << "\n";
		output += ss.str();

	}
	file.close();
	std::fstream file2("file.out", std::ios::out);
	file2 << output;
	file2.close();
	return 0;
}