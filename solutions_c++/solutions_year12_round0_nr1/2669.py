#include<iostream>
#include<cstdio>
#include<vector>
#include<sstream>
#include<set>

#define REP(i,n) for(int i=0;i<n;++i)
#define PRINT(n) {REP(i,n.size()) cout<<n[i]<<"|";cout<<endl;}
#define PB(n) push_back(n)

using namespace std;

char letters[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

 int readInt()
{
	int ret;
	string s;
	getline(cin,s);
	istringstream is(s);
	is>>ret;
	return ret;
}

void solve(int testNumber)
{

	string ret="";
	
	string local ;
	getline(cin,local);
	for(int i=0;i<local.size();++i)
	{

	
		if(local[i]>='a'&&local[i]<='z') ret+=letters[ ((int)(local[i]-'a'))%26];
		else ret+=local[i];
	}

	cout<<"Case #"<<testNumber<<": "<<ret<<endl;

	
}

int main()
{
	int t;
	t=readInt();
	REP(i,t) solve(i+1);
}

 
