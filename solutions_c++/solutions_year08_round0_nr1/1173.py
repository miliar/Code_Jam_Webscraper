#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
using namespace std;

vector<string> se;
vector<string> queries;

int solve()
{
	int i,j,k;


	vector<int> cnt;
	int nNumSwitch=0;
	bool bSwitch=true;
	for (i=0;i<se.size();i++) cnt.push_back(0);
	int last=-1;
	queries.push_back("");
	for (i=0;i<queries.size();i++)
	{
		int nCntZero=0;

		if (bSwitch) {for (j=0;j<cnt.size();j++) if (j!=last) cnt[j]=0;bSwitch=false;}
		string s=queries[i];

		for (j=0;j<se.size();j++)
		{
			string sej=se[j];
			if (sej.compare(s)==0)
			{cnt[j]++;last=j;break;}
		}
		for (j=0;j<cnt.size();j++)
			if (cnt[j]==0) {nCntZero++;}
		if (nCntZero<=0 && i<queries.size()-1) {
			nNumSwitch++; bSwitch=true;

			}
/*		for (j=0;j<se.size();j++)
		{
			string sej=se[j];
			if (sej.compare(s)==0)
				cnt[j]++;
		}*/


	}
	return nNumSwitch;
}
int main()
{
	int i,j,k;
	int num_cases;
	fstream fin,fout;
	fin.open ("A-large.in", fstream::in);
	fout.open("A-large.out",fstream::out);

	fin >>num_cases;


	for (i=0;i<num_cases;i++)
	{
		se.clear();
		queries.clear();

		int num_se,num_q;
		fin >>num_se;
		for (j=0;j<num_se;j++)
		{
			char sSE[128];
			do {fin.getline(sSE,128);} while (*sSE==0);
			se.push_back(sSE);
		}
		fin >>num_q;
		for (j=0;j<num_q;j++)
		{
			char sQ[128];
			do {fin.getline(sQ,128);} while (*sQ==0);
			queries.push_back(sQ);
		}
		fout << "Case #"<<i+1<<": "<<solve()<<endl;
	}
}