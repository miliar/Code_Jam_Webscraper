#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>


using namespace std;
ifstream fin;
ofstream fout;

map<string,int> engine;
map<string,int>::iterator iter;

int main(void)
{
	int i,j,k,l,N,S,Q;
	fin.open("input.in");
	fout.open("output.out");
	fin>>N;
//	fin>>noskipws;
//	fin>>skipws;
	char c;
	string s;
	int change=0,neng=0;
	for(i=1;i<=N;i++)
	{
		change=0;
		fin>>S;
		fin>>noskipws;
		fin>>c;
		for(j=1;j<=S;j++)
		{
			s="";
			while(1)
			{
				fin>>c;
				if(c=='\n')
					break;
				else
					s+=c;
			}
			engine[s]=1;
		}
		neng=S;
		fin>>skipws;
		fin>>Q;
		fin>>noskipws;
		fin>>c;
		for(j=1;j<=Q;j++)
		{
			s="";
			while(1)
			{
				fin>>c;
				if(c=='\n'||fin.eof())
					break;
				else
					s+=c;
			}
			if(engine[s]==1)
			{
				neng--;
				engine[s]=0;
			}
			if(neng==0)
			{
				change++;
				for(iter=engine.begin();iter!=engine.end();iter++)
				{
					iter->second=1;
				}
				neng=S;
				engine[s]=0;neng--;
			}


		}
		fout<<"Case #"<<i<<": "<<change<<endl;
	}
	

    fin.close();
	fout.close();
	return 0;
}
