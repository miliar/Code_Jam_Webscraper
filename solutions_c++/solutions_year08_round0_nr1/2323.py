#include<iostream>
#include<vector>
#include<map>
using namespace std;
int main()
{
int n;
cin>>n;
int c=0;
while(n--)
	{
		int s,q;
		cin>>s;
		cin.ignore();
		map<string,int> eng;
		for(int i=0;i<s;i++)
		{
			string x;
			getline(cin,x);
			eng[x]=0;
		}
		map<string,int> temp;
		cin>>q;
		cin.ignore();
		int sw=0;
		while(q--)
		{
		
		string x;
		getline(cin,x);
			if(eng.count(x)!=0)
			{
			if(temp.count(x)==0)
			{
				temp[x]=1;
			}
			if(temp.size()==s)
			{
				sw++;
				temp.clear();
				temp[x]=1;
			}
			}
		}
		cout<<"Case #"<<++c<<": "<<sw<<"\n";
	}

}
