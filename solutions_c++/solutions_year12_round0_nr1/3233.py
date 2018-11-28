#include <iostream>
#include <fstream>
#include <string>

int main(void)
{
	std::ifstream ifs("input.txt");
	std::ofstream ofs("output.txt");
	std::string buffer;
	char stringBuffer[100];

	char convertTable[26] = {
		'y', 'h', 'e', 's', 'o', 'c', 'v', 'x',
		'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
		'z', 't', 'n', 'w', 'j', 'p', 'f', 'm',
		'a', 'q'
	};

	int caseNum;


	ifs >> caseNum;
	std::getline(ifs, buffer);
	for(int j=0; j<caseNum; j++)
	{
		std::getline(ifs, buffer);
		ofs << "Case #" << j+1 << ": ";
		std::strcpy(stringBuffer,buffer.c_str());
		for(int i=0; i<buffer.size(); i++)
		{
			if(stringBuffer[i] == ' '){
				ofs << stringBuffer[i]; 
				continue;
			}
			stringBuffer[i] = convertTable[ stringBuffer[i] - 'a' ];
			ofs << stringBuffer[i];
		}
		ofs << std::endl;
	}

	return 0;
}