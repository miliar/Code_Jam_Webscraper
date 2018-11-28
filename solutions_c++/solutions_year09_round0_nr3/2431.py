#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <numeric>
#include <iostream>
#include <fstream>
#include<iomanip>

using namespace std;

int cnt(string s,string s2)
{
	int res=0;
	if(s.size()<s2.size() || s2.size()==0)
		return 0;
	if(s2.size()==1)
		res+=count(s.begin(),s.end(),s2[0]);

	else
		for(int i=0;i<s.size();i++)
		{

			while(s[i]!=s2[0] && i<s.size()-1)
				i++;
			res+=cnt(s.substr(i+1),s2.substr(1));
			res%=10000;


		}
		return res%10000;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("C-small-attempt0.in");
	output.open("C-small-attempt0.out");
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
	int N;
	int round=1;
	input>>N;
	string s="welcome to code jam";
	string str;
	getline(input,str);
	while(round<=N)
	{
		int res;
		getline(input,str);


		res=cnt(str,s);
		output<<"Case #"<<round<<": ";
		if(res<1000)output<<"0";
		if(res<100)output<<"0";
		if(res<10)output<<"0";
		output<<res<<endl;
		round++;
	}
	input.close();
	output.close();
	return 0;
}