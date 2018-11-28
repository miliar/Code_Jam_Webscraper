#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<fstream>

using namespace std;

char isCombine(string s,vector<string> &a)
{
	int i;
	for(i=0;i<a.size();++i)
		if( (s[s.size()-1]==a[i][0] && s[s.size()-2]==a[i][1]) || (s[s.size()-1]==a[i][1] && s[s.size()-2]==a[i][0]))
			return a[i][2];
	return '?';
}

bool isOppose(string s,vector<string> &b)
{
	int i,j,k;

	for(i=0;i<s.size()-1;++i)
	for(j=i+1;j<s.size();++j)
	for(k=0;k<b.size();++k)
		if((s[i]==b[k][0] && s[j]==b[k][1]) || (s[i]==b[k][1] && s[j]==b[k][0]))
			return true;
	return false;
}

string B(vector<string> a,vector<string> b,string s)
{
	int i,j;
	char c;
	string str,ret="[";

L:	for(i=2;i<=s.size() && s.size()>1;)
	{
		str=s.substr(0,i),s.erase(s.begin(),s.begin()+i);
		if((c=isCombine(str,a))!='?')
		{
			str.erase(str.begin()+str.size()-1);
			str.erase(str.begin()+str.size()-1);
			str+=c,s=str+s,--i;
			goto L;
		}
		else if(isOppose(str,b))
			goto L;
		else
			s=str+s,++i;
	}

	if(s.size()==0)
		return "[]";

	for(i=0;i<s.size()-1;++i)
	{
		c=s[i];
		ret=ret+s[i]+", ";
	}
	ret=ret+s[s.size()-1]+"]";	

	return ret;
}


void main()
{
	int i,j;
	int num,n1,n2;
	vector<string> a,b;
	string s,ret,str;
	vector<int> v;

	ifstream fin("D:\\gcj\\B-small\\B-large.in");
	ofstream fout("D:\\gcj\\B-small\\B-large.txt");

	fin>>s;
	num=atoi(s.c_str());
	
	for(i=1;i<=num;++i)
	{
		a.clear(),b.clear();

		fin>>s;
		n1=atoi(s.c_str());
		for(j=0;j<n1;++j)
			fin>>s,a.push_back(s);

		fin>>s;
		n2=atoi(s.c_str());
		for(j=0;j<n2;++j)
			fin>>s,b.push_back(s);

		fin>>s,fin>>s;
		str=s;
			
		char number[100];
		itoa(i,number,10);
		string nn(number);

		ret="Case #"+nn+": ";
		fout<<ret<<B(a,b,str)<<endl;
	}

/*	string sa[]={"QFT"};
	string sb[]={"QF"};

	vector<string> a(sa,sa+1);
//	vector<string> a;
	vector<string> b(sb,sb+1);
//	vector<string> b;

	string s="FAQFDFQ";

	string ret=B(a,b,s);
	cout<<ret<<endl;*/
}	
