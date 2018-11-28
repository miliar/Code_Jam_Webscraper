#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

bool IsAllIn(vector<string> se,vector<string> qu,int s)
{
	if(s>=qu.size())
		return false;
	for(int i=0;i!=se.size();++i)
	{
		vector<string>::iterator result=find(qu.begin()+s,qu.end(),se[i]);
		if(result==qu.end())
			return false;
	}
	return true;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-small.out");
	int n;
	fin>>n;
	for(int i=0;i!=n;++i)
	{
		vector<string> se,qu;
		int sen,qun;
		fin>>sen;
		fin.ignore(1000,'\n');
		for(int i1=0;i1!=sen;++i1)
		{
			string temp;
			getline(fin,temp);
			se.push_back(temp);
		}
		fin>>qun;
		fin.ignore(1000,'\n');
		for(int i1=0;i1!=qun;++i1)
		{
			string temp;
			getline(fin,temp);
			qu.push_back(temp);
		}
		if(sen==0||qun==0)
		{
			fout<<"Case #"<<i+1<<": "<<"0"<<endl;
			continue;
		}
		int start=0,cnt=0;
		if(IsAllIn(se,qu,0)==false)
		{
			fout<<"Case #"<<i+1<<": "<<"0"<<endl;
		}
		else
		{
			while(IsAllIn(se,qu,start))
			{
				vector<int> vpos;
		    	for(int j=0;j!=se.size();++j)
					vpos.push_back(find(qu.begin()+start,qu.end(),se[j])-qu.begin());
				start=vpos[max_element(vpos.begin(),vpos.end())-vpos.begin()];
				cnt++;
			}
			fout<<"Case #"<<i+1<<": "<<cnt<<endl;
		}
		
	}
	return 0;
}