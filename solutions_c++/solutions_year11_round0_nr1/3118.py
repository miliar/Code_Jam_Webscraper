#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <ctype.h>
#include <cmath>

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

int doForOne(vector<pair<int,char> > X)
{
	int lo=1,lb=1;
	int teO=0,teB=0;
	int total=0;
	for(int i=0;i<X.size();i++)
	{
		if(X[i].second=='B')
		{
			total += max(0,abs(lb-X[i].first)-teB)+1;
			teO += max(0,abs(lb-X[i].first)-teB)+1;
			teB=0;
			lb = X[i].first;
		}
		else
		{
			total += max(0,abs(lo-X[i].first)-teO)+1;
			teB += max(0,abs(lo-X[i].first)-teO)+1;
			teO=0;
			lo = X[i].first;
		}
	}
	return total;
}

int main()
{
	string line;
	int T;
	stringstream ss;
	ifstream fp("A-large.in");
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
	FILE *fpout = fopen("temp.out","w");
	while (getline (fp, line)) 
	{
		caseCount++;
			
		vector<string> tokens;
		Tokenize(line,tokens," ");
		vector<pair<int,char> > X;
		for(int i=1;i<tokens.size();i+=2)
			X.push_back(make_pair(atoi(tokens[i+1].c_str()),tokens[i][0]));
				
		int out = doForOne(X);
		fprintf(fpout,"Case #%d: %d",caseCount,out);
		fprintf(fpout,"\n");
	}	
	fprintf(fpout,"\n");
	fclose(fpout);
}
