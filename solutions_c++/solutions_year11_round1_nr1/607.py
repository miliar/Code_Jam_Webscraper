#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>
#include<iterator>
#include<sstream>
#include<set>
using namespace std;

typedef unsigned long long uint64;
typedef long long int64;
typedef long double ld128;

int gcd(int x, int y)
{
	if(y==0)return x;
	return gcd(y,x%y);
}

void printVec(vector<int> &A)
{
	for(int i=0;i<A.size();i++)
		cout<<A[i]<<' ';
	cout<<endl;
}

int main(int argc, char *argv[])
{
//readin file
	string file;
	if(argc!=2){cerr<<"0,1 or 2!"<<endl;exit(1);}
	switch(atoi(argv[1]))
	{
		case 0: file="test"; break;
		case 1: file="A-small"; break;
		case 2: file="A-large"; break;
		default: cerr<<"choose the correct file, 0(test),1(small),2(large)"<<endl;exit(1); break;
	}
	string ifilename=file+".in"; string ofilename=file+".out";
	ifstream input(ifilename.c_str());ofstream output(ofilename.c_str());

//read in number of events
	int T;
	input>>T;
	int64 N;
	int PD,PG;

//main loop start
	for(int t=0;t<T;t++)
	{
		input>>N>>PD>>PG;
		cout<<"case : "<<t+1<<endl;

		if(PD<100 && PG==100){output<<"Case #"<<t+1<<": Broken"<<endl;continue;}
		if(PD>0 && PG==0){output<<"Case #"<<t+1<<": Broken"<<endl;continue;}
		int y=gcd(PD,100);
		if((int64)100/y>N){output<<"Case #"<<t+1<<": Broken"<<endl;continue;}

		output<<"Case #"<<t+1<<": Possible"<<endl;;
	}

	input.close();
	output.close();
	return 0;
}
