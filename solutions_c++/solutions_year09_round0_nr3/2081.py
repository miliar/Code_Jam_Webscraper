#include <string>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <winsock2.h>
#include <vector>
unsigned int recurseOverString(std::string toSearch, std::string toFind);
std::string PadToFourCharacters(unsigned int value);
int main(int argc, char* parm[])
{
	std::string fileName = parm[1];
	HANDLE hInputFile = CreateFile(const_cast<char*>(fileName.c_str()), 
									GENERIC_READ, 
									FILE_SHARE_READ, 
									(LPSECURITY_ATTRIBUTES)	NULL, 
									OPEN_EXISTING, 
									FILE_ATTRIBUTE_READONLY, 
									(HANDLE) NULL);
	char msg[825000];
	DWORD bytesRead = 0;
	ReadFile(hInputFile, &msg, 825000, &bytesRead, NULL);
	msg[bytesRead] = 0x00;
	std::string input = msg;
	int numOfCases = atoi(input.c_str());
	input = input.substr(input.find('\n'));
	input = input.substr(input.find_first_not_of('\n'));
	std::vector<std::string> listOfInputs;
	size_t index = 0;
	size_t index2 = 0;
	while(input.length() > 0)
	{
		index2 = input.find('\n');
		if(index2 != std::string::npos)
		{
			index = input.find_first_not_of('\n', index2);
			if(index != std::string::npos)
			{
				std::string temp = input.substr(0, index2);
				listOfInputs.push_back(temp);
				input = input.substr(index);
			}
			else
			{
				std::string temp = input.substr(0, index2);
				listOfInputs.push_back(temp);
				break;
			}
		}
		else
		{
			listOfInputs.push_back(input);
			break;
		}
	}
	for(int i = 0; i < numOfCases; ++i)
	{
		std::cout<<"Case #"<<i+1<<": ";

		std::cout<<PadToFourCharacters(recurseOverString(listOfInputs.at(i), "welcome to code jam"))<<std::endl;
	}
	return 0;
}
//int findFirstCharacter(std::string toSearch, std::string toFind)
//{
//	for(size_t i = 0; i <= toSearch.length(); ++i)
//	{
//
//	}
//}

unsigned int recurseOverString(std::string toSearch, std::string toFind)
{
	if(toFind.length() == 0)
	{
		return 1;
	}
	unsigned int count = 0;
	for(size_t i = 0; i < toSearch.length(); ++i)
	{
		if(toSearch.at(i) == toFind.at(0))
		{
			count += recurseOverString(toSearch.substr(i+1), toFind.substr(1));
		}
	}

	return count;
}


std::string PadToFourCharacters(unsigned int value)
{
	std::string retVal;
	char strVal[500];
	_itoa(value, strVal, 10);
	retVal = strVal;
	if(retVal.length() > 4)
	{
		retVal = retVal.substr(retVal.size()-4, 4);
	}
	else
	{
		size_t length = retVal.length();
		retVal.clear();
		switch(length)
		{
			case 0:
				retVal += "0";
			case 1:
				retVal += "0";
			case 2:
				retVal += "0";
			case 3:
				retVal += "0";
		}
		retVal += strVal;
	}

	return retVal;
}