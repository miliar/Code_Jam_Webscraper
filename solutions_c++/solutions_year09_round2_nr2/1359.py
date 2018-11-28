#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <numeric>

using namespace std;

int main()
{
	unsigned long long a;
	ifstream input;
	ofstream output;
	input.open("B-small-attempt0.in");
	output.open("B-small-attempt0.out");
	if(!input)
	{
		cout<<"input error"<<endl;
		return 0;
	}
	if(!output)
	{
		cout<<"output error"<<endl;
		return 0;
	}
	int round=1;
	int T;
	input>>T;
	while(round<=T)
	{
		input>>a;
		string s;
		vector<int> v;

		while(a)
		{
			 int d=a%10;
			 a/=10;
			 v.push_back(d);
		}
		output<<"Case #"<<round<<": ";
		reverse(v.begin(),v.end());
		if(next_permutation(v.begin(),v.end()) )
			for(vector<int>::iterator it=v.begin();it!=v.end();++it)
				output<<*it;
		else
		{
			sort(v.begin(),v.end());
			vector<int>::iterator it=v.begin();
			while(*it==0)
				++it;
			int j = *it;
			v.erase(it);
			output<<j<<"0";
			for(vector<int>::iterator it=v.begin();it!=v.end();++it)
				output<<*it;
		}
		output<<endl;
		round++;
	}
	return 0;
}