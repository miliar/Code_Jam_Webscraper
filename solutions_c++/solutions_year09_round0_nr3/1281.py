// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
#include <string>
#include <vector>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>
#include <iomanip>

using namespace std;

//other functions may go here!

//main function!

typedef struct data_{
	int pos;
	__int64 count;
} data;

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("clargein.txt");
    ofstream outputFile("clargeout.txt", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
    {
      //error openning input/output file!
      return 0;
    }

	int numIterations;
	inputFile >> numIterations;
	inputFile.ignore();
	string word = "welcome to code jam";
	string letters = " welcotdjam";
	vector<int> positions[11];
	vector<data> answer[19];
	for(int numCases = 1; numCases<=numIterations; numCases++)
	{
		//parsing code goes here
		string text;
		getline(inputFile, text);
		for(int x=0; x<letters.size(); x++)
		{
			int pos = -1;
			positions[x].clear();
			while((pos = text.find(letters[x], pos+1))>=0)
				positions[x].push_back(pos);
		}
		//problem code goes here
		answer[18].clear();
		data d;
		d.count=1;
		for(int x=0; x<positions[10].size(); x++)
		{
			d.pos = positions[10][x];
			answer[18].push_back(d);
		}
		for(int x=17; x>-1; x--)
		{
			answer[x].clear();
			int pos = 0;
			while(letters[pos] != word[x]) pos++;
			for(int y=0; y<positions[pos].size(); y++)
			{
				d.count = 0;
				for(int z=0; z<answer[x+1].size(); z++)
				{
					if(answer[x+1][z].pos > positions[pos][y])
						d.count += answer[x+1][z].count;
				}
				if(d.count>0)
				{
					d.pos = positions[pos][y];
					d.count %= 10000;
					answer[x].push_back(d);
				}
			}
		}
		__int64 count=0;
		for(int x=0; x<answer[0].size(); x++)
		{
			count += answer[0][x].count;
			count %= 10000;
		}
		outputFile << "Case #" << numCases << ": " << setfill('0') << setw(4) << count << endl;
	}
	return 0;
}