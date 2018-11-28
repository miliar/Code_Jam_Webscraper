#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;

int main()
{
	freopen("a.in","r",stdin) ;
	freopen("a.out","w",stdout) ;
	int L,D,N;
	cin>>L>>D>>N;
	vector<vector<int> > Data;
	string s;
	for(int i=0;i<D;i++)
	{
		
		cin>>s;
		vector<int> eachVal;//(L,0);
		for(int j=0;j<L;j++)
		{
			int value =s[j]-'a';
			eachVal.push_back(1<<value);
		}
		Data.push_back(eachVal);
	}

	for(int i=0;i<N;i++)
	{
		cin>>s;
		vector<int> TestCase;
		for(int j=0;j<s.size();j++)
		{
			int eachValue=0;
			if(s[j]=='(')
			{
				j++;
				while(s[j]!=')')
				{
					eachValue|=(1<<(s[j]-'a'));
					j++;
				}
				TestCase.push_back(eachValue);
			}
			else
			{
				TestCase.push_back(1<<(s[j]-'a'));
			}
		}
		int count=0;
		for(int j=0;j<D;j++)
		{
			bool isTrue = true;
			for(int k=0;k<L;k++)
				isTrue &= ((Data[j][k]&TestCase[k])>0);
			if(isTrue)count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}

	return 0;
}