#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

void main()
{	
    ifstream ifile("A-large.in.txt");
	ofstream ofile("output.txt");
	int caseNum,seNum,qureNum;
	ifile>>caseNum;
	int i,j,k;
    for(i=0;i<caseNum;++i)
	{
		int res =0;
		string temp;
		vector<string> se,qure;
	
		ifile>>seNum;
		getline(ifile,temp);
		for(j=0;j<seNum;++j)
		{
			getline(ifile,temp);
			se.push_back(temp);
		}
		ifile>>qureNum;
		getline(ifile,temp);
		for(j=0;j<qureNum;++j)
		{
			getline(ifile,temp);
			qure.push_back(temp);
		}
			
		typedef vector<string>::iterator iter;
		iter max ,flog= qure.begin();		
		while (flog!= qure.end()) 
		{
			max = flog;
			for(int n=0;n<seNum;n++)
			{
				if (max < find(flog,qure.end(),se[n])) 
					max = find(flog,qure.end(),se[n]);
			} 
			flog=max;
			if (flog!=qure.end()) res++;
		}
		cout<<"Case #"<<i+1<<":"<<res<<endl;
		string output("Case #");
		ostringstream s,s1;
		s<<i+1;
		output+=s.str();
		output+=": ";
		s1<<res;
		output+=s1.str();
		ofile<<output<<endl;
		se.clear();
		qure.clear();
	}
}