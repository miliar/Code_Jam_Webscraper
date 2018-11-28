#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>

using namespace std;

const double pi = 2*acos(0.0);
const double eps = 1e-9;

int main(int argc,char* argv[])
{
	string inputfile,outputfile;
	if(argc==2)
		inputfile=argv[1];
	else
	{
		cout<<"Input: ";
		cin>>inputfile;
	}
	outputfile=inputfile;
	if(inputfile.find("in")!=inputfile.npos)
		outputfile.replace(outputfile.find("in"),2,"out");
	else
		outputfile.append(".out.txt");
	ifstream in(inputfile.c_str());
	ofstream out(outputfile.c_str());
	int N;
	in>>N;
	for(int i=0;i<N;i++)
	{
		int P,K,L;
		in>>P>>K>>L;
		vector<int> Frecs;
		for(int j=0;j<L;j++)
		{
			int Frec;
			in>>Frec;
			Frecs.push_back(Frec);
		}
		int Total=0,nP=1,nK=K,nL=0;
		bool imp=false;
		for(int j=0;j<L;j++)
		{
			vector<int>::iterator it=max_element(Frecs.begin(),Frecs.end());
			if(nK)
			{
				Total+=(*it)*nP;
				Frecs.erase(it);
				nK--;
			}
			else if(nP<=P)
			{
				nK=K;
				nP++;
				Total+=(*it)*nP;
				Frecs.erase(it);
				nK--;
			}
			else
			{
				imp=true;
			}
		}
		if(!imp)
			out<<"Case #"<<i+1<<": "<<Total<<endl;
		else
			out<<"Case #"<<i+1<<": "<<"Impossible"<<endl;
	}
	out.close();
	in.close();
}