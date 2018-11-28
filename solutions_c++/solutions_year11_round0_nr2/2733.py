/*
 * B.cpp
 *
 *  Created on: ??þ/??þ/????
 *      Author: B2lawa
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ext/numeric>
#include <memory.h>
#include <valarray>
using namespace std;
map <string,char> M;
set <string> S;
string sc,sd,s;
int C,D,N,len;
string tem,tt;
int main()
{
	freopen("B.in","rt",stdin);
	freopen("B.out","wt",stdout);
	int t;
	cin>>t;
	for(int x=1;x<=t;++x)
	{
		M.clear();
		S.clear();
		cin>>C;
		while(C--)
		{
			cin>>sc;
			tem=(sc[0]);
			tem+=(sc[1]);
			M[tem]=sc[2];
			reverse(tem.begin(),tem.end());
			M[tem]=sc[2];
		}
		cin>>D;
		while(D--)
		{
			cin>>sd;
			S.insert(sd);
			reverse(sd.begin(),sd.end());
			S.insert(sd);
		}
		cin>>N;
		cin>>s;
		tem="";
		bool f,r;
		for(int i=0;i<s.size();++i)
		{
			f=true;
			r=true;
			if(tem.size())
			{
				tt="";
				tt+=(tem[tem.size()-1]);
				tt+=s[i];
				if(M.find(tt)!=M.end())tem[tem.size()-1]=M[tt],f=false;
				if(f)
				{
					for(int j=0;j<tem.size();++j)
					{
						tt="";
						tt+=(tem[j]);
						tt+=(s[i]);
					//	cout<<tt<<endl;
						if(S.find(tt)!=S.end()){tem="";r=false;break;}
					}
				}
			}
			if(r&&f)tem+=s[i];
		}
		cout<<"Case #"<<x<<": [";
		for(int i=0;i<tem.size();++i)
		{
			if(i)cout<<", ";
			cout<<tem[i];
		}
		cout<<"]"<<endl;
	}
}
