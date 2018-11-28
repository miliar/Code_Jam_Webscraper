#include <iostream>
#include <fstream>
#include <string>
#include <clx/salgorithm.h>

#include <stdlib.h>

int main(int argc, char** argv)
{
	static unsigned char tableA[256] =
	{
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
		'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
		'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
		'y', 'z', ' ', 0
	};
	static unsigned char tableB[256] =
	{
		'y', 'h', 'e', 's', 'o', 'c', 'v', 'x',
		'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
		'z', 't', 'n', 'w', 'j', 'p', 'f', 'm',
		'a', 'q', ' ', 0
	};
	std::ifstream ifp(argv[1]);
	int testcases;
	std::string line;
	
	std::getline(ifp, line);
	testcases = atoi(line.c_str());
	for(int i = 0; i < testcases; i++)
	{
		std::getline(ifp, line);
		//std::cout << "line:" << line << std::endl;
		unsigned char* ch = (unsigned char*)malloc(strlen(line.c_str())+1);
		strcpy(ch, line.c_str());
		for(int k = 0; ch[k] != 0; k++)
		{
			for(int j = 0; tableA[j] != 0; j++)
			{
				if(ch[k] == tableA[j])
				{
					ch[k] = tableB[j];
					break;
				}
			}
		}
		std::cout << "Case #" << i+1 << ": " << ch << std::endl;
		free(ch);
	}
	return 0;
}