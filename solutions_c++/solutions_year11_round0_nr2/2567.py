// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <stdlib.h>
using namespace std;

#define LINE_SIZE 10000
#define STR_INT_SIZE 10

inline int ReadInt(char * line, int * oldptr)
{
	char str_int[STR_INT_SIZE];
	memset(str_int, 0, STR_INT_SIZE);
	int ptr = 0;
	while((line[ptr] != ' ') & (line[ptr] != '\0')) ptr++;
	if (ptr > 0)
	{
			memcpy(str_int, line, ptr);
			if (line[ptr] != 0)
				*oldptr += ptr+1;
			else
				*oldptr += ptr;
			return atoi(str_int);
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char line[LINE_SIZE], str_int[STR_INT_SIZE], last_read, to_add;
	int cur_case = 0, cases, total_places, ptr, nptr, tmp, x, num_right;
	int * the_array;

	ofstream outfile;
	ifstream infile;

	multimap<char,char> opposed;
	map<string, char> combine;
	map<string,char>::iterator find_combine;
	pair<multimap<char,char>::iterator,multimap<char,char>::iterator> ret;
	string elements;
	string a_combine, a_combine2;

	outfile.open("answer.txt");
	if (!outfile.is_open()){
		cout<<"Error opening output file\n";
		goto end;
	}

	infile.open("in.txt");
	if (!infile.is_open()){
		cout<<"Error opening input file\n";
		goto end;
	}

	memset(str_int, 0, STR_INT_SIZE);
	infile.getline(str_int, STR_INT_SIZE);
	cases = atoi(str_int);
	while(cur_case < cases)
	{
		//reset variables for each case
		elements.clear();
		combine.clear();
		opposed.clear();

		//read in the next string line
		memset(line, 0, LINE_SIZE);
		infile.getline(line, LINE_SIZE);
		ptr = 0;

		//read in the number of combines
		x = ReadInt(line, &ptr);
		if (x != 0)
		{
			tmp = 0;
			while(tmp < x)
			{
				a_combine.clear();
				a_combine.push_back(line[ptr]);
				a_combine.push_back(line[ptr+1]);
				a_combine2.clear();
				a_combine2.push_back(line[ptr+1]);
				a_combine2.push_back(line[ptr]);
				ptr += 2;
				combine[a_combine] = line[ptr];
				combine[a_combine2] = line[ptr];
				ptr += 2;
				tmp++;
			}
		}

		//read in the number of opposeds
		x = ReadInt(line+ptr, &ptr);
		if (x != 0)
		{
			tmp = 0;
			while(tmp < x)
			{
				opposed.insert(pair<char,char>(line[ptr],line[ptr+1]));
				opposed.insert(pair<char,char>(line[ptr+1],line[ptr]));
				ptr += 3;
				tmp++;
			}
		}

		//read in the number of elements
		x = ReadInt(line+ptr, &ptr);
		tmp = 0;
		while(tmp < x)
		{
			to_add = line[ptr];
			if (elements.length())
			{
				//check for combinations first
				string asdf;
				asdf.push_back(last_read);
				asdf.push_back(to_add);
				find_combine = combine.find(asdf);
				if (find_combine != combine.end())
				{
					elements.pop_back();
					to_add = find_combine->second;
				}
				else //now check for opposeds
				{
					multimap<char,char>::iterator it;
					ret = opposed.equal_range(line[ptr]);
					for (it=ret.first; it!=ret.second; ++it)
					{
						if (elements.find((*it).second) != string::npos)
						{
							elements.clear();
							to_add = 0;
							break;
						}
					}
				}

			}
			
			if (to_add != 0){
				elements.push_back(to_add);
				last_read = to_add;
			}
			ptr++;
			tmp++;
		}

		outfile<<"Case #"<<cur_case+1<<": [";
		if (elements.length())
		{
			outfile<<elements[0];
			for(x = 1; x < elements.length(); x++)
				outfile<<", "<<elements[x];
		}
		outfile<<"]\n";

		cur_case++;
	}


end:
	infile.close();
	outfile.flush();
	outfile.close();
	getchar();
	return 0;
}

