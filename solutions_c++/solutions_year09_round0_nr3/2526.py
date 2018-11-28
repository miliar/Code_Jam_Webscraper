#include<vector>
#include<iostream>
#include<string>
#include<cstdio>
#include<cmath>
#include<map>
#include<set>
#include<fstream>
#include<cstring>
#include<sstream>
using namespace std;
#define REP(i,n) for(int i=0;i<n;++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
string pat("welcome to code jam");
long long  res;
void  rec(string inp,string  str,int inp_index,int pat_index)
{
	if(str.compare(pat)==0)
		res = (res+1)%10000;
	else
	{
		for(int i=inp_index;i<(int)inp.size();++i)
		{
			if(inp[i]==pat[pat_index])
			{
				char c = pat[pat_index];
				rec(inp,str+c,i+1,pat_index+1);
			}
		
		}
	}
	
}
int main()
{
	ifstream file1("/home/npm/small.in");
	ofstream out("/home/npm/small.out");
 	string inp;
	char temp[100];
	file1.getline(temp,100);
	int test=0;
	for(int i=0;temp[i];++i)
		test = test*10+temp[i]-'0';	
	for(int c=0;c<test;++c)
	{
		file1.getline(temp,100);
		for(int i=0;i<temp[i];++i)
			inp+=temp[i];
//		cout<<"******** "<<inp<<" *******"<<endl;
		for(int i=0;i<inp.size();++i)
		{
			if(inp[i]=='w')
			{
				rec(inp,"w",i+1,1);
			}
		}
		string ans="";
		std::stringstream con;
		con<<res;
		ans=con.str();
		if(ans.size()<4)
		while((int)ans.size()<4)
		{
			ans = "0"+ans;
		}
		out<<"Case #"<<c+1<<": "<<ans<<endl;
		res=0;
		inp="";
	}
	file1.close();
	out.close();
	return 0;
}
