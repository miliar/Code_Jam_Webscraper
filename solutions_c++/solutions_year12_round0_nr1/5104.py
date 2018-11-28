#include <fstream>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
	char map[26];
	map['a' - 'a'] = 'y';
	map['o' - 'a'] = 'e';
	map['z' - 'a'] = 'q';
	map['q' - 'a'] = 'z';
	
	ifstream readSampleIn("sampleIn.txt");
	ifstream readSampleOut("sampleOut.txt");
	string lineSampleIn, lineSampleOut;
	int linesSampleCount;
	readSampleIn >> linesSampleCount; 
	getline(readSampleIn, lineSampleIn);
	for (int i = 0; i < linesSampleCount; i++)
	{
		lineSampleIn.clear();
		lineSampleOut.clear();
		getline(readSampleIn, lineSampleIn);
		getline(readSampleOut, lineSampleOut);
		int startIndex = i >= 10 ? 10:9; 	//"Case #i: "
		for (int j = 0; j < lineSampleIn.length(); j++)
		{
			char c = lineSampleIn[j];
			if (c >= 'a' && c <= 'z')
			{
				map[c - 'a'] = lineSampleOut[startIndex + j]; 
			}
		}
	}
	readSampleIn.close();
	readSampleOut.close();
	
	ifstream read("input.txt");
	ofstream write("output.txt");
	string line;
	int linesCount;
	read >> linesCount;
	getline(read, line);
	for (int i = 0; i < linesCount; i++)
	{
		line.clear();
		getline(read, line);
		for (int j = 0; j < line.length(); j++)
		{
			char c = line[j];
			if (c >= 'a' && c <= 'z')
			{
				line[j] = map[c - 'a'];
			}
		}
		write << "Case #" << i + 1 << ": " << line << endl;
	}
	read.close();
	write.close();
	
	return 0;
}