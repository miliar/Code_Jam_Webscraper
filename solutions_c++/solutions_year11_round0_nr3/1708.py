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

bool isExist(vector<int> v)
{
	int i,j,k,maxLen=0,num;
	char c[100];
	vector<string> vs;

	for(i=0;i<v.size();++i)
	{
		itoa(v[i],c,2);
		string s(c);

		if(maxLen<=s.size())
			maxLen=s.size();

		vs.push_back(s);
	}

	for(i=0;i<vs.size();++i)
	for(j=1,k=vs[i].size();j<=maxLen-k;++j)
		vs[i]='0'+vs[i];
	
	for(i=0;i<vs[0].size();++i)
	{
		for(j=0,num=0;j<vs.size();++j)
			if(vs[j][i]=='1')
				++num;

		if(num%2!=0)
			return false;
	}

	return true;
}

int C(vector<int> v)
{
	int i;
	int ret=0;

	sort(v.begin(),v.end());

	if(!isExist(v))
		return -1;

	for(i=1;i<v.size();++i)
		ret+=v[i];

	return ret;
}

void main()
{
	int i,j;
	int num,gr,r,k;
	string s,ret;
	vector<int> v;

	ifstream fin("D:\\gcj\\C-large\\C-large.in");
	ofstream fout("D:\\gcj\\C-large\\C-large.txt");

	fin>>s;
	num=atoi(s.c_str());
	
	for(i=1;i<=num;++i)
	{
		v.clear();

		fin>>s;
		r=atoi(s.c_str());
		
		for(j=1;j<=r;++j)
			fin>>s , v.push_back(atoi(s.c_str()));
			
		char number[100];
		itoa(i,number,10);
		string nn(number);

		ret="Case #"+nn+": ";
		k=C(v);

		if(k>=0)
			fout<<ret<<C(v)<<endl;
		else
			fout<<ret<<"NO"<<endl;
	}

/*	int a[]={159818 ,884689 ,987035};
	vector<int> v(a,a+3);

	int ret=C(v);
	cout<<ret<<endl;*/

}
