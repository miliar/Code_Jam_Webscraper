#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

char *filenameIn;
char *filenameOut;
int caseNumbers;
int *N;
int *K;
string *inLine;
bool *isPower;
bool *isOn;
int democase = 0;

void readFile(const char* fileIn)
{
    ifstream infile;
	infile.open(fileIn,ios::in);

	char buff[300];
	infile.getline(buff,300);
	caseNumbers = atoi(buff);
	N = new int[caseNumbers];
	K = new int[caseNumbers];
	inLine = new string[caseNumbers];

	for(int i = 0; i < caseNumbers; i++)
    {
        infile.getline(buff,300);
        inLine[i] = buff;
		string tempStr = "";
		int count = 0;
		for(string::size_type index = 0; index != inLine[i].size()+1; index++)
		{
			if(isalnum(inLine[i][index]))
			{
				tempStr += inLine[i][index];
			}
			else
			{
				if(count == 0)
				{
					N[i] = atoi(tempStr.c_str());
					tempStr = "";
				}
				else
				{
					K[i] = atoi(tempStr.c_str());
				}
				count++;
			}
		}
    }
}

void go(int index)
{
	int cN = N[index] +1;
	int cK = K[index];
	isPower = new bool[cN];
	isOn = new bool[cN];
	isPower[0] = true;
	isOn[0] = false;
	for(int i = 1; i < cN; i++)
	{
		isPower[i] = false;
		isOn[i] = false;
	}

	for(int j = 0; j < cK; j++)			//cK为一共按的次数
	{
		for(int n = 0; n < cN; n++)
		{
			if(isPower[n])
			{
				isOn[n] = !isOn[n];
			}
		}
		for(int n = 0; n < cN; n++)
		{
				if(isPower[n] && isOn[n])
				{
					isPower[n+1] = true;
				}
				else
				{
					isPower[n+1] = false;
				}
		}
	}
}

bool writeFile(const char *fileOut)
{
	ofstream outfile;
	outfile.open(fileOut,ios::out);

	while(democase < caseNumbers)
	{
		go(democase);
		if(isPower[N[democase]])
			outfile<<"Case #"<<democase+1<<": "<<"ON"<<endl;
		else
			outfile<<"Case #"<<democase+1<<": "<<"OFF"<<endl;
		democase++;
	}
	return 0;
}

int main()
{
	filenameIn = "A-small-attempt2.in";
	filenameOut = "A-small.out";
	readFile(filenameIn);
	writeFile(filenameOut);
	return 0;
}