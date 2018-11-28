#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

const int MAXLENGTH = 1024;
char line[MAXLENGTH];

__int64 gtwo(__int64 a, __int64 b)   
{   
	while(b>0)   
	{   
		int temp;   
		temp=b;   
		b=a%b;   
		a=temp;   
	}   
	return a;   
}   

__int64 gN(vector<__int64>& a)
{   
	vector<__int64> b;
	b.resize(a.size()-1);
	if(a.size()>2)   
	{   
		b[0]=gtwo(a[0],a[1]);   
		for(int i=1;i<a.size()-1;i++)   
			b[i]=a[i+1];   
		return gN(b);   
	}   
	else   
		return gtwo(a[0],a[1]);   
}  

int main()
{
	string instr = "B-small-attempt3.in";
	ifstream infile(instr.c_str());

	ofstream outfile("out.txt");

	infile.getline(line,MAXLENGTH);

	int caseNum = strtol(line,NULL,10);

	cout<<caseNum<<endl;

	vector< vector<__int64> > testCases;

	while( caseNum-- > 0 )
	{
		infile.getline(line,MAXLENGTH);
		char *NStr = strtok(line," ");
		int N = strtol(NStr,NULL,10);
		vector<__int64> testcase;
		while(N-->0)
		{
			char *event = strtok(NULL," ");
			testcase.push_back(_atoi64(event));	
		}
		testCases.push_back(testcase);
	}

	for(int i = 0; i < testCases.size(); i++)
	{
		vector<__int64> diff;
		vector<__int64> testcase = testCases[i];
		std::sort(testcase.begin(),testcase.end());
		for(int j = 1; j < testcase.size(); j++)
		{
			diff.push_back(testcase[j] - testcase[j-1]);
		}

		int result;
		int gcd;
		if(diff.size()>1)
		{
			gcd = gN(diff);
			
		}
		else
			gcd = diff[0];	

		if(testcase[0]%gcd == 0)
				result  = 0;
		else
		{
			result = gcd - (testcase[0]%gcd);
		}
			
		
		outfile<<"Case #"<<i+1<<": "<<result<<"\n";
	}

	return 1;
}
