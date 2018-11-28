#include <string>
#include <vector>
#include <cmath>

#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream> 

using namespace std;

bool chk(char a,string b)
{
	for(int i=0;i<b.size();i++)
	{
		if(b[i]==a)return true;
	}
	return false;
}
int main()
{
	ofstream ofs; 
	ifstream ifs;
	ifs.open("d:\\Wraith\\A.in");
	ofs.open("d:\\Wraith\\a.out");
	int L,D,N;
	vector<string> a;
	string t,it;
	ifs>>L>>D>>N;
	for(int i=0;i<D;++i)
	{
		ifs>>t;
		a.push_back(t);
	}
	sort(a.begin(),a.end());
	int asw=0;
	for(int j=0;j<N;++j)
	{
		ofs<<"Case #"<<j+1<<": ";
		ifs>>it;
		int flag=0;
		string tep[15];
		int si=0;
		for(int k=0;k<it.size();)
		{
			if(it[k]=='(')
			{
				k++;
				flag=1;
			}
			else if(it[k]==')')
			{
				k++;si++;
				flag=0;

			}
			else if(flag==0)
			{
				tep[si++]+=it[k];
				k++;
			}
			else
			{
				tep[si]+=it[k];
				k++;
			}
		}
		for(int ii=0;ii<a.size();ii++)
		{
			int res=0;
			for(int jj=0;jj<L;jj++)
			{
				if(chk(a[ii][jj],tep[jj]))res++;
			}
			if(res==L){asw++;}
		}
		ofs<<asw<<endl;asw=0;
	}
	
	return 0;
}