
// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <math.h>


using namespace std;


class Converter
{
public:
	bool isOk(vector<int> v)
	{
		bool ret = true;
		for(int i = 1; i < (int)v.size(); i++)
			if(v[i-1] > v[i])
				return false;
		return true;
	}

	string process(vector<string> s, vector<string> q)
	{
		string ret = "";
		
		int index = 0;
		int sw = 0;


		int maxi = index;
		do
		{
			//jump
			for(int i = 0; i < s.size(); i++)
			{
				int j = index;
				while(j < q.size())
				{
					if(q[j] == s[i])
						break;
					j++;
				}

				maxi = max(maxi, j);
			}

			if(maxi < q.size())
			{
				index = maxi;
				sw++;
			}

		}while(maxi < q.size());

		char ch[1000];
		ret = itoa(sw, ch, 10);

		return ret;
	}

	vector<string> split(string line)
	{
		vector<string> ret;

		string tmp = "";
		for(int i = 0; i < line.size(); i++)
			if(line[i] != ' ')
				tmp += line[i];
			else
			{
				ret.push_back(tmp);
				tmp = "";
			}
			ret.push_back(tmp);

		return ret;
	}
	vector<int> splitInt(string line)
	{
		vector<int> ret;
		string tmp = "";
		for(int i = 0; i < line.size(); i++)
			if(line[i] != ' ')
				tmp += line[i];
			else
			{
				ret.push_back(atoi(tmp.c_str()));
				tmp = "";
			}
			ret.push_back(atoi(tmp.c_str()));

		return ret;
	}
};

string getLine(FILE * file)
{
	string line = "";
	char buff[2]; buff[0] = 'n';
	size_t read = 1;
	while(read == 1 && buff[0] != '\n')
	{
		read = fread(buff, 1, 1, file);
		if(read == 1 && buff[0] != '\n')
			line += buff[0];
	}
	return line;
}

int _tmain(int argc, _TCHAR* argv[])
{
	Converter cnv;	
	FILE * file = NULL, * out = NULL;

	//file = fopen("e:\\A-small.in", "r");
	//out = fopen("e:\\A-small.out", "w");
	file = fopen("e:\\A-large.in", "r");
	out = fopen("e:\\A-large.out", "w");
	int n = 0;
	if(file != NULL && out != NULL)
	{
		//get line
		string line = getLine(file);
		n = atoi(line.c_str());

		for(int i = 0; i < n; i++)
		{
			line = getLine(file);
			int sn = atoi(line.c_str());
			vector<string> s;
			for(int j = 0; j < sn; j++)
			{
				line = getLine(file);
				s.push_back(line);
			}

			line = getLine(file);
			int sq = atoi(line.c_str());
			vector<string> q;
			for(int j = 0; j < sq; j++)
			{
				line = getLine(file);
				q.push_back(line);
			}

			//process line
			string str = cnv.process(s, q);

			//write data to out file
			fprintf(out, "Case #%d: %s\n", i+1, str.c_str());
			fflush(out);
		}

		//close files
		fclose(file);
		fclose(out);

		printf("Press any key to exit.");
	}
	else
	{
		printf("Cannot open in/out file.");
	}

	getchar();

	return 0;
}

