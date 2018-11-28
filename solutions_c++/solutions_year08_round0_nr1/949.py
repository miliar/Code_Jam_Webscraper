#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<sstream>
#include<fstream>
using namespace std;
vector<string> se,sq;
int se_sz,sq_sz;
int calc()
{
	int mx=0,i,j,k,ret=0,c=0;
	for(i=0;i<sq_sz;i+=mx)
	{
		for(j=0,mx=0;j<se_sz;j++)
		{
			for(k=i,c=0;k<sq.size()&&se[j]!=sq[k];k++,c++);
				mx=max(c,mx);
		}
		if(i+mx<sq_sz) ++ret;
	}
	return ret;
}
int main()
{
	char str[1000];
	string t="";
	int n,se_n,sq_n;
	stringstream ss;
	fstream f1,f2;
	f1.open("c:\\gcj\\A-large.in",ios::in);
	f2.open("c:\\gcj\\A-large.out",ios::out);
	f1.getline(str,1000);
	ss<<str;
	ss>>n;
	ss.clear();
	for(int i=0;i<n;i++)
	{
		f1.getline(str,1000);
		ss<<str;
		ss>>se_n;
		ss.clear();
		for(t="",se_sz=se_n;se_n>0;se_n--)
		{
			f1.getline(str,1000);
			t=str;
			se.push_back(t);
		}
		f1.getline(str,1000);
		ss<<str;
		ss>>sq_n;
		ss.clear();
		for(t="",sq_sz=sq_n;sq_n>0;sq_n--)
		{
			f1.getline(str,1000);
			t=str;
			sq.push_back(t);
		}
		int ret=calc();
		f2<<"Case #"<<i+1<<":"<<" "<<ret<<endl;
		se.clear();
		sq.clear();
	}
	f1.close();
	f2.close();
	system("pause");
	return 0;
}
