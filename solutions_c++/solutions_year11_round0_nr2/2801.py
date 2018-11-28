#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <map>
#include <set>
using namespace std;

#define MAX_BUF_SIZE 4096


int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "Usage:command.exe infile outfile" << endl;
		exit(1);
	}
	FILE* in = fopen(argv[1], "r");
	if (!in)
	{
		cout << "cannot open infile" << endl;
		exit(1);
	}
	FILE* out = fopen(argv[2], "w");
	if (!out)
	{
		cout << "cannot open outfile" << endl;
		exit(1);
	}
	char buf[MAX_BUF_SIZE];
	fgets(buf, MAX_BUF_SIZE, in);
	int count = 0;
	while (fgets(buf, MAX_BUF_SIZE, in))
	{
		count ++;
		printf("\r%d", count);
		map<string, string> comMap;
		set<string> oppSet;
		char* toke = strtok(buf, " \n");
		for (int i = 0; i < atoi(toke); i++)
		{
			toke = strtok(NULL, " \n");
			string str = toke;
			string key = str.substr(0,2);
			string value = str.substr(2);
			comMap.insert(make_pair(key, value));
			char covKey[4];
			covKey[0] = key[1];
			covKey[1] = key[0];
			covKey[2] = '\0';
			comMap.insert(make_pair(covKey, value));
		}
		toke = strtok(NULL, " \n");
		for (int i = 0; i < atoi(toke); i++)
		{
			toke = strtok(NULL, " \n");
			oppSet.insert(toke);
			char cov[4];
			cov[0] = toke[1];
			cov[1] = toke[0];
			cov[2] = '\0';
			oppSet.insert(cov);
		}
		toke = strtok(NULL, " \n");
		toke = strtok(NULL, " \n");
		string instr = toke;
		string outstr;
		outstr.push_back(instr[0]);
		for (int i = 1; i < instr.size(); i++)
		{
			if (outstr.empty())
			{
				outstr.push_back(instr[i]);
				continue;
			}
			char com[4];
			com[0] = outstr[outstr.size()-1];
			com[1] = instr[i];
			com[2] = '\0';
			if (comMap.find(com) != comMap.end())
			{
				outstr.replace(outstr.size()-1, 1, comMap[com]);
			}
			else
			{
				outstr.push_back(instr[i]);
				for (int j = 0; j < int(outstr.size()-1); j++)
				{
					com[0] = outstr[j];
					if (oppSet.find(com) != oppSet.end())
					{
						outstr.clear();
					}
				}
			}
			
		}
		fprintf(out, "Case #%d: [", count);
		printf(" %d\n", outstr.size());
		for (int i = 0; i < int(outstr.size()-1); i++)
		{
			fprintf(out, "%c, ", outstr[i]);
		}
		if (outstr.size() != 0)
		{
			fprintf(out, "%c", outstr[outstr.size()-1]);
		}
		fprintf(out, "]\n");
		//fprintf(out, "Case #%d: %d\n", count, totaltime);
	}
	fclose(in);
	fclose(out);
}