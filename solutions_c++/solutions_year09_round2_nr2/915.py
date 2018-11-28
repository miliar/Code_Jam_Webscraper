#include<iostream>
#include<string>
#include<vector>
#include<sstream>
using namespace std;
int NUM=0;
string itos(int a)
{
	stringstream z;
	z<<a;
	return z.str();
}

int  stoi(string h)
{
	int b;
	stringstream z(h);
	z>>b;
	return b;
}


string tar(string a)
{
	string j;
	for(int i=0;i<a.size();++i)
	{
		if(a[i]!='0')
			j+=a[i];
		else
			NUM+=1;
	}
	sort(j.begin(),j.end());
	return j;
}


int main()
{
	int test;
	string no;
	cin>>test;
	for(int i=0;i<test;++i)
	{
		NUM=0;
		cin>>no;
		printf("Case #%i: ",i+1);
		string s=no,res;
		string s1=s;
		next_permutation(s1.begin(),s1.end());
		string h=tar(s);
		res.push_back(h[0]);
		for(int i1=0;i1<=NUM;++i1)
			res+='0';
		for(int i1=1;i1<h.size();++i1)
			res+=h[i1];
		if(s1>no)
			cout<<s1<<"\n";
		else
			cout<<res<<"\n";
	}
}