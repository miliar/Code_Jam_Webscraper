#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;

const int MAXLENGTH = 1024;
char line[MAXLENGTH];

int main()
{
	string instr = "A-large.in";
	ifstream infile(instr.c_str());

	ofstream outfile("out.txt");

	infile.getline(line,MAXLENGTH);

	int caseNum = strtol(line,NULL,10);

	cout<<caseNum<<endl;

	vector< pair<int,__int64> > testCases;

	while( caseNum-- > 0 )
	{
		infile.getline(line,MAXLENGTH);
		char* NStr = strtok(line," ");
		char* KStr = strtok(NULL," ");
		testCases.push_back(std::make_pair(strtol(NStr,NULL,10),_atoi64(KStr)));
	}

	bool isLight;
	for(int i = 0; i < testCases.size(); i++)
	{
		isLight = false;
		pair<int,__int64> testcase = testCases[i];
		int N = testcase.first;
		__int64 K = testcase.second;

		int minTime = pow(2,N)-1;

		if((K-minTime)%(minTime+1) == 0)
			isLight = true;

		outfile<<"Case #"<<i+1<<": "<<(isLight?"ON":"OFF")<<"\n";
	}

	return 1;
}