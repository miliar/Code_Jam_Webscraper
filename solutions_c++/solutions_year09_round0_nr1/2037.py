
#include <assert.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>

using namespace std;

const int nC='z'-'a'+1;
long L=0;
long D=0;
set<string> W;
set<char> combs[15];


string Process(string s)
{
	int res=0;

	if (s.length()==0) { return "0"; }
	
	int c=0;	
	for (size_t i=0;i<s.size();++i)
	{
		combs[c].clear();
		if (s[i]=='(')
		{
			while (s[++i]!=')')
			{
				combs[c].insert(s[i]);
			}
		}
		else
		{
			combs[c].insert(s[i]);
		}
		++c;
	}
	assert(c==L);
	
	for (set<string>::iterator it=W.begin();it!=W.end();++it)
	{
		string ss=*it;
		
		bool ok=true;
		for (int i=0;i<L&&ok;++i)
		{
			ok=(combs[i].find(ss[i])!=combs[i].end());		
		}
		if (ok)
		{ 
			++res;
		}
	}
	

	char sres[1024]={0};
	sprintf(sres,"%d",res);
	return string(sres);
}

void ProcessFile(ifstream &fIn,ofstream &fOut)
{	
	const int nLen=1;
	string params[nLen];
	
	string line;
	getline(fIn,line);
	long conf[3];
	int nPIndex=0;
	int nLastSPIndex=0;
	char *pParams=const_cast<char*>(line.c_str());
	do {
		int nSp=line.find(" ",nLastSPIndex);
		if (nSp==string::npos)
		{
			conf[nPIndex]=atoi(&pParams[nLastSPIndex]);
			break;
		}
		else
		{
			pParams[nSp]='\0';
			conf[nPIndex]=atoi(&pParams[nLastSPIndex]);
			nLastSPIndex=nSp+1;
		}
		++nPIndex;

	}while(true);
	L=conf[0];
	D=conf[1];
	long nN=conf[2];

	for (long i=0;i<D;++i)
	{
		getline(fIn,line);
		W.insert(line);
	}
	
	for (long i=0;i<nN;++i)
	{
		getline(fIn,line);
		fOut << "Case #" << (i+1) << ": " << Process(line)<<"\n";
		
	}
}



int main(int argc, char* args[])
{
	string fsIn(args[1]);
	string fsOut(fsIn+".out");
	ifstream fIn(fsIn.c_str());
	ofstream fOut(fsOut.c_str());
	ProcessFile(fIn,fOut);
	fIn.close();
	fOut.close();
}