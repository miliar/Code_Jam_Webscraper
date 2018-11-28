#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>

using namespace std;

void Tokenize(const string& str,vector<string>& tokens, const string& delimiters = " ")
{
    
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    string::size_type pos = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {  
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}

string doForOne(vector<string> comb,vector<string> del, string seq)
{
	char combTable[26][26];
	bool delTable[26][26];
	for(int i=0;i<26;i++)
		for(int j=0;j<26;j++)
		{
			combTable[i][j] = char(0);
			delTable[i][j] = false;
		}
		
	for(int i=0;i<comb.size();i++)
	{
		combTable[comb[i][0]-'A'][comb[i][1]-'A'] = comb[i][2];
		combTable[comb[i][1]-'A'][comb[i][0]-'A'] = comb[i][2];
	}
	for(int i=0;i<del.size();i++)
	{
		delTable[del[i][0]-'A'][del[i][1]-'A'] = true;
		delTable[del[i][1]-'A'][del[i][0]-'A'] = true;
	}
	string final;
	for(int i=0;i<seq.length();i++)
	{
		if(final.length()==0)
		{
			final.push_back(seq[i]);
			continue;
		}
		char last = final[final.length()-1];
		if(combTable[last-'A'][seq[i]-'A']!=0)
		{
			final[final.length()-1] = (combTable[last-'A'][seq[i]-'A']);
			continue;
		}
		for(int j=0;j<final.length();j++)
			if(delTable[final[j]-'A'][seq[i]-'A'] == true)
			{
				final.clear();
				break;
			}
		if(final.length()!=0)
			final.push_back(seq[i]);
	}
	return final;
		
}
int main()
{
	string line;
	int T;
	stringstream ss;
	ifstream fp("B-large.in");
	if(!fp.is_open())
	{
		printf("\nCannot open file ... ");
		return 0;
	}
	getline(fp,line);
	
	ss.str("");
	ss<<line;
	ss>>T;
	
	int caseCount=0;
	while (getline (fp, line) && T>0) 
	{
		caseCount++;
		vector<string> comb,del;
		string seq;
		
		vector<string> tokens;
		Tokenize(line,tokens," ");
		
		int count=1;
;
		while(isalpha(tokens[count][0]))
			comb.push_back(tokens[count++]);
		
		count++;

		while(isalpha(tokens[count][0]))
			del.push_back(tokens[count++]);
		
		count++;
		seq = tokens[count];
		
		string output = doForOne(comb,del,seq);
		printf("Case #%d: [",caseCount);
		for(int i=0;i<output.length();i++)
			if(i<output.length()-1)
				printf("%c, ",output[i]);
			else
				printf("%c",output[i]);
		printf("]\n");
		
	}	
		
}
