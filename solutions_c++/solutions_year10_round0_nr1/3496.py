#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int pw(int n)
{
	int p=1;
	for(int i=0;i<n;i++)
	p=p*2;
	return p;
}
int main()
{
	ifstream fin("A-small-attempt2.in");
	ofstream fout("A-small-attempt2.out");
	int t;
	fin>>t;
	int to=t;
	while(t--)
	{
		int n,k;
		fin>>n>>k;
		int s=pw(n)-1;
		//cout<<"s="<<s<<endl;
		if(k<s)
			fout<<"Case #"<<to-t<<":"<<" "<<"OFF"<<endl;
		else if(k==s)
			fout<<"Case #"<<to-t<<":"<<" "<<"ON"<<endl;
		else if(k>s)
			if((k-s)%(s+1)==0)
			fout<<"Case #"<<to-t<<":"<<" "<<"ON"<<endl;
			else
			fout<<"Case #"<<to-t<<":"<<" "<<"OFF"<<endl;
	}
	return 0;
}
