#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <functional>

using namespace std;

int main( int argc, char*argv[])
{
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small.out");
    string str;
    getline(in,str);
    int iTasks = atoi(str.c_str());
    for( int iCount = 1; iCount <= iTasks; iCount++ )
    {
		getline(in, str);
		vector<string> vSTR;
		size_t iPos1 = 0;
		do
		{
			size_t iPos2 = str.find(' ',iPos1);
			if( iPos2 == string::npos )
				iPos2 = str.length();
			string str2;
			str2.assign(str.begin() + iPos1, str.begin() + iPos2);
			vSTR.push_back(str2);
			iPos1 = iPos2 + 1;
		}while(iPos1 < str.length());
		int numLet = atoi(vSTR[0].c_str());
		int numKey = atoi(vSTR[1].c_str());
		int numAlf = atoi(vSTR[2].c_str());
		getline(in, str);
		vector<int> vFreq;
		iPos1 = 0;
		do
		{
			size_t iPos2 = str.find(' ',iPos1);
			if( iPos2 == string::npos )
				iPos2 = str.length();
			string str2;
			str2.assign(str.begin() + iPos1, str.begin() + iPos2);
			vFreq.push_back(atoi(str2.c_str()));
			iPos1 = iPos2 + 1;
		}while(iPos1 < str.length());
		if( numKey * numLet < numAlf )
		{
			out<<"Case #"<< iCount <<": Impossible"<<'\n';
			continue;
		}
		sort(vFreq.begin(),vFreq.end());
		int mul = 1;
		int sum = 0;
		int itmp = 1;
		for( int i = vFreq.size() - 1; i >= 0; i-- )
		{
			sum += mul*vFreq[i];
			itmp++;
			if( itmp > numKey )
			{
				itmp = 1;
				mul++;
			}
		}
		out<<"Case #"<< iCount <<": "<<sum<<'\n';
	}
}