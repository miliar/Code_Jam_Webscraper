#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

std::string int2str(int& N)
{
	std::stringstream ss;
	ss << N;
	return ss.str();
}

int main(void)
{
	std::ifstream ifs("input.txt");
	std::ofstream ofs("output.txt");

	int caseNum;
	ifs >> caseNum;

	for(int i=0; i<caseNum; i++)
	{
		int A, B, y;
		ifs >> A >> B;
		y = 0;
		
		for(int j=A; j<=B; j++)
		{
			std::string currentNumStr = int2str(j);
			for(int k=1; k < currentNumStr.size(); k++)
			{
				std::string recycled = currentNumStr.substr(currentNumStr.size() - k, k) + currentNumStr.substr(0, currentNumStr.size() - k);
				int recycledInt = atoi(recycled.c_str());

				//1212, 123123, etc.
				if(recycledInt == j)
					break;

				if(recycledInt > j && recycledInt <= B){
						y++;
				}
			}
		}
		
		ofs << "Case #" << i+1 << ": " << y << std::endl;
	}
	
	return 0;
}
