

#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 

using namespace std; 

map<set<pair<int,int> >,int > mp;

map<set<pair<int,int> >,int > mp2;

#define N (6)
#define CAN (11)

bool cck(set<pair<int,int> > &l)
{
	int p[N];
	memset(p,0,sizeof(p));
	for(set<pair<int,int> >::iterator it=l.begin();it!=l.end();it++)
	{
		p[it->first]=p[it->second]=1;
	}
	for(int i=0;i<N-1;i++)
	{
		if(p[i]==0&&p[i+1]==1)
			return false;
	}
	return true;
}

bool ck(vector<int> &v,set<pair<int,int> > &l)
{
	for(set<pair<int,int> >::iterator it=l.begin();it!=l.end();it++)
	{
		if(v[it->first]>v[it->second])
			return false;
	}
	return true;
}

int count(set<pair<int,int> > &l)
{
	if(mp.find(l)!=mp.end())return mp[l];
	vector<int > v;
	for(int i=0;i<N;i++)
		v.push_back(i);
	int c=0;
	do
	{
		if(ck(v,l))c++;
	}while(next_permutation(v.begin(),v.end()));
	return mp[l]=c;
}

int js(set<pair<int,int> > &l)
{
	if(mp2.find(l)!=mp2.end())return mp2[l];
	if(count(l)==1)return mp2[l]=0;
	if(count(l)==0)return mp2[l]=999999;

	if((l.size()>CAN)||count(l)>(1<<(CAN-l.size())))return mp2[l]=99999;
	//if(l.size()>=11)return 999999;
	int &res=mp2[l];
	cout<<mp2.size()<<endl;
	res=999999;
	for(int i=0;i<N;i++)
		for(int j=i+1;j<N;j++)
		{
			if(l.find(make_pair(i,j))==l.end()&&l.find(make_pair(i,j))==l.end())
			{
				int x1,x2;
				l.insert(make_pair(i,j));
				/*if(!cck(l))
				{
					l.erase(make_pair(i,j));
					continue;
				}*/
				x1=js(l);
				l.erase(make_pair(i,j));
				l.insert(make_pair(j,i));
				x2=js(l);
				l.erase(make_pair(j,i));
				if(x1==999999)res=min(res,x2+1);
				else if(x2==999999)res=min(res,x1+1);
				else res=min(res,max(x1,x2)+1);
			}
		}
	return res;
}

int main()
{
	set<pair<int,int> > s;
	s.insert(make_pair(0,1));
	int c=js(s)+1;
	cout<<"ans="<<c<<endl;
	cin>>c;
}
