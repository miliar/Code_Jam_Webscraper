// BEGIN CUT HERE

// END CUT HERE
#line 5 "ImportantSequence.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define SZ(v) (int)((v).size())

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("in.in");
	outfile.open("out.in");
	int T;
	infile>>T;
	string azline;
	for(int i=97;i<=122;i++)
		azline.push_back(char(i));
	//cout<<azline<<endl;
	string bline="yhesocvxduiglbkrztnwjpfmaq",line;
	getline(infile,line);
	for(int j=1;j<=T;j++)
	{
		getline(infile,line);
		istringstream str(line);
		
		outfile<<"Case #"<<j<<':';
		string a;
		while(str>>a)
		{
			outfile<<' ';
			string b(a);
			int len=a.size();
			for(int i=0;i<len;i++)
				b.at(i)=bline.at((int)(a[i])-97);
			outfile<<b;
		}
		outfile<<'\n';
	}
	infile.close();
	outfile.close();
	//system("pause");
	return 0;
}
