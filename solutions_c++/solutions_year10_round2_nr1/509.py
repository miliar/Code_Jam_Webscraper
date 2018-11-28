#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;


vector<string> split(string x)
{
	x+="/";
	vector<string> res;
	for(int i=0;i<x.size()-1;++i)
	{
		string tmp;
		if(x[i]=='/')
		{
			while(i<x.size()-1  && x[i+1]!='/')
			{
				tmp+=x[i+1];
				//cout<<i<<" "<<tmp<<"\n";
				i+=1;
			}
		}
		res.push_back(tmp);
		//cout<<tmp<<"frf\n";
	}
	return res;
}



int main()
{
	int T;
	cin>>T;
	for(int i1=1;i1<=T;++i1)
	{
		map<string,int> store;
		int M,N;
		cin>>M>>N;
		for(int i=0;i<M;++i)
		{
			string s;
			cin>>s;
			//return 0;
			vector<string> X= split(s);
			string tmp;
			for(int i=0;i<X.size();++i)
			{
				tmp+="/"+X[i];
				store[tmp]=1;
			}
		}
		int count=0;
		for(int i=0;i<N;++i)
		{
			string s;
			cin>>s;
			vector<string> X= split(s);
			string tmp;
			for(int i=0;i<X.size();++i)
			{
				tmp+="/"+X[i];
				if(store[tmp]!=1)
				{
					count+=1;
					store[tmp]=1;
				}
			}
		
		}
		cout<<"Case #"<<i1<<": "<<count<<"\n";;
	}
}