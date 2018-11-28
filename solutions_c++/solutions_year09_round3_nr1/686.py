/*
Language:C++
*/

#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<iostream>
#include<algorithm>
#include<hash_map>

using namespace std;
using namespace stdext;
//typedef  pair<char,int> digit;

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");
	
	int t;
	fin>>t;
	for(int i=0;i!=t;i++)
	{
		string s;
		fin>>s;
		
		hash_map<char, int> hm,hm2;
		for(int j=0;j!=s.length();j++)
		{
			hm[s[j]]++;
		}
		
		int d=hm.size();
		if(d==1) d=2;
		
		int digit=1;
		
		hm2[s[0]]=2;
		for(int j=1;j!=s.length();j++)
		{
			if(hm2[s[j]]==0)
			{
				hm2[s[j]]=digit;
				if(digit==1) digit++;
				digit++;
			}
		}

		unsigned long long result=0;
		
		for(int j=0;j!=s.length();j++)
		{
			unsigned long long dig=hm2[s[j]]-1;
			
			int p=s.length()-j-1;
			
			while(p>0)
			{
				dig*=d;
				p--;
			}
			result+=dig;
		}
		

		
		fout<<"Case #"<<(i+1)<<": "<<result<<endl;
	}
	
	return 0;
}