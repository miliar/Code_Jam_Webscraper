#include <iostream>
#include<stdio.h>
#include<set>
#include<map>
#include<cstring>
using namespace std;


int main (int argc, char * const argv[]) {
  
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for(int caso=1;caso<=t;caso++)
	{
		set<pair<char,char> >S;
		map<pair<char,char>,char>M;
		int C,d,n;
		cin>>C;
		for(int i=0;i<C;i++)
		{
			char a,b,c;
			cin>>a;
			cin>>b;
			cin>>c;
			M[make_pair(a,b)]=c;
			M[make_pair(b,a)]=c;
		}
		cin>>d;
		
		for(int i=0;i<d;i++)
		{
			char a,b;
			cin>>a;
			cin>>b;
			S.insert(make_pair(a,b));
			S.insert(make_pair(b,a));
		}
		cin>>n;
		string res="";
		for(int i=0;i<n;i++)
		{
			char x;
			cin>>x;
			if(res.size()==0)
			{
				res+=x;
				continue;
			}
			char u=res[res.size()-1];
			if(M.count(make_pair(u,x))){
				res=res.substr(0,res.size()-1)+M[make_pair(u,x)];
				continue;
			}
			for(int j=0;j<res.size();j++)
				if(S.count(make_pair(x,res[j])))res="";
			if(res=="")continue;
			res+=x;
		}
		cout<<"Case #"<<caso<<": [";
		for(int i=0;i<res.size();i++)
		{
			cout<<res[i];
			if(res.size()!=i+1)cout<<", ";
		}
		cout<<"]"<<endl;
		
	}
    return 0;
}
