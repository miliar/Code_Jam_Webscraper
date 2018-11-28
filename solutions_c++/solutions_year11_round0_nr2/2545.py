// GJam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <assert.h>
using namespace std;

const int abc_size = ('Z' - 'A') + 1;

int main(int argc, char* argv[])
{

	assert(argc > 1);
	FILE * output =  0; 
	if (argc > 2)
	{
#ifndef _DEBUG
		output = freopen(argv[2], "w", stdout);
#endif
	}
	FILE * input = fopen(argv[1], "r");

	char combines[abc_size][abc_size];
	multimap<char, char> eliminates;
	int count;
	fscanf(input, "%d", &count);
	//cerr << count << endl;

	for (int i=0; i< count; ++i)
	{
		memset(combines, 0, sizeof(combines));
		eliminates.clear();
		int comb_count;
		fscanf(input, "\n%d ", &comb_count);
		for (int j = 0; j < comb_count; ++j)
		{
			char c[4];
			fscanf(input, "\n%s ", &c);
			combines[c[0]-'A'][c[1]-'A']=c[2]-'A';
			combines[c[1]-'A'][c[0]-'A']=c[2]-'A';
			//cerr << c[0] << "&" << c[1] << "->" << c[2] << " ";
		}
		int elim_count;
		//cerr << " | ";
		fscanf(input, "%d ", &elim_count);
		for (int j = 0; j < elim_count; ++j)
		{
			char c[3];
			fscanf(input, "\n%s ", &c);
			eliminates.insert(make_pair(c[0]-'A',c[1]-'A'));
			eliminates.insert(make_pair(c[1]-'A',c[0]-'A'));
			//cerr << c[0] << "/" << c[1] << " ::\n";
		}
		int str_ln;
		fscanf(input, "%d ", &str_ln);
		char * inp_str = new char[str_ln + 1];
		inp_str[str_ln]=0;
		fread(inp_str, 1, str_ln, input);
		//cerr << inp_str << endl;

		map<char, int> counters;

		vector<char> result;
		result.reserve(str_ln);
		for (int j = 0; j < str_ln; j++)
		{
			result.push_back(inp_str[j]-'A');
			counters[inp_str[j]-'A']++;


			while(result.size() > 1 &&
				combines[result.back()][result[result.size()-2]])
			{
				--counters[result.back()];
				--counters[result[result.size()-2]];
				result[result.size()-2] = combines[result.back()][result[result.size()-2]];
				result.pop_back();
				counters[result.back()]++;
			}
			for (
				multimap<char, char>::iterator it = eliminates.find(result.back());
			    it != eliminates.end()  && it->first == result.back(); it++)
			{
				if (counters[it->second])
				{
					result.clear();
					counters.clear();
					break;
				}
			}

			//if (result.empty()) continue;

			//cerr << " " << char(result[0] + 'A');
			//for (int k = 1; k<result.size();k++)
			//{
			//	cerr << char(result[k] + 'A');
			//}
			//cerr << " ";

		}
		delete[]inp_str;
#ifndef _DEBUG
		cout << "Case #" << (int)(i+1) << ": [";
		//cerr << " \n[";
		if (!result.empty())
		{
			//cerr << (char)(result[0] + 'A');
			cout << (char)(result[0] + 'A');
			for (int j = 1;j<result.size();j++)
			{
				//cerr << ", " << (char)(result[j] + 'A');
				cout << ", " << (char)(result[j] + 'A');
			}
		}
		//cerr << "]" << endl;
		cout << "]\n";
#endif
	}

	if (output)
		fclose(output);
	if (input)
		fclose(input);
	return 0;
}

