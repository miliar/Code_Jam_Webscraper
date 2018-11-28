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
	int N;
	int64 y;

//main loop start
	for(int t=0;t<T;t++)
	{
		input>>N;
		y=0;
		int posO,posB;
		posO=1;posB=1;
		int dtO=0;
		int dtB=0;
		for(int i=0;i<N;i++)
		{
			char c;int x;
			input>>c>>x;
//			cout<<c<<x<<endl;
			if(c=='O')
			{
				int dt=abs(x-posO);
				posO=x;
				if(dt>dtO){y+=(dt-dtO)+1;dtB+=(dt-dtO)+1;dtO=0;}
				else {y+=1;dtO=0;dtB+=1;}
			}
			else if(c=='B')
			{
				int dt=abs(x-posB);
				posB=x;
				if(dt>dtB){int del=dt-dtB+1;y+=del;dtB=0;dtO+=del;}
				else {y+=1;dtB=0;dtO+=1;}
			}
			else
			{
				cout<<"wrong!"<<endl;
			}
//			cout<<y<<' '<<dtO<<' '<<dtB<<endl;
		}
		cout<<endl;
		

		cout<<"case : "<<t+1<<endl;
		output<<"Case #"<<t+1<<": "<<y<<endl;
	}

	input.close();
	output.close();
	return 0;
}
