#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int N;
string *strings;
int *results;
string pattern = "welcome to code jam";
int pattern_len;

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Welcome to Code Jam\\test.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Welcome to Code Jam\\out.txt";

void readfile();
void writefile();
void init();
int Analyze(string s, int string_start, int pattern_index);

void main()
{
	readfile();
	init();
	writefile();
	delete[] strings;
	delete[] results;
}

void readfile()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	infile>>N;
	strings = new string[N];

	string skip;
	getline(infile, skip, '\n');

	for(int i = 0; i < N; i++)
	{
		getline(infile, strings[i], '\n');
	}
	infile.close();

}

void writefile()
{
	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	for(int i = 0; i < N; i++)
	{
		outfile<<"Case #"<<i + 1<<": ";
		if(results[i] < 10)
		{
			outfile<<"000";
		}
		else if(results[i] < 100)
		{
			outfile<<"00";
		}
		else if(results[i] < 1000)
		{
			outfile<<"0";
		}
		outfile<<results[i] % 10000<<endl;
	}
	outfile.close();
}

void init()
{
	pattern_len = pattern.length();
	results = new int[N];
	for(int i = 0; i < N; i++)
	{
		results[i] = Analyze(strings[i], 0, 0);
	}
}

int Analyze(string s, int string_start, int pattern_index)
{
	int count = 0;
	if(pattern_index < pattern_len -1)
	{
		for(int i = string_start; i < s.length(); i++)
		{
			if(pattern[pattern_index] == s[i])
			{
				count += Analyze(s, i + 1,  pattern_index + 1);
			}
		}
	}
	else if(pattern_index == pattern_len -1)
	{
		for(int i = string_start; i < s.length(); i++)
		{
			if(pattern[pattern_index] == s[i])
			{
				count ++;
			}
		}	
	}
	return count;
}