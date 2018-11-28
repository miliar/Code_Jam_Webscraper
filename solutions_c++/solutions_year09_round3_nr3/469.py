#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;
bool prison[102];



int func(int p,vector<int>v)
{
	for(int i=0;i<102;i++) prison[i]=true;
	prison[0]=false; prison[101]=false;
	int sz=v.size();
	int cnt=0;
	for(int i=0;i<sz;i++)
	{
		for(int j=v[i]-1;j>=0 && prison[j];j--)
		{
			cnt++;
		}
		for(int j=v[i]+1;j<=p && prison[j];j++)
		{
			cnt++;
		}
		prison[v[i]]=false;
	}
	return cnt;
}
int main()
{
	int p,q,test,r=1;
	cin>>test;
	while(test--)
	{
				cin>>p>>q;
				vector<int>v(q);
				for(int i=0;i<q;i++)
				{
					cin>>v[i];
				}
				prison[0]=false;
				prison[101]=false;
				int ret=9999999;
				
				sort(v.begin(),v.end());
				
				do
				{
					ret=min(ret,func(p,v));
				}while(next_permutation(v.begin(),v.end()));
				
				cout<<"Case #"<<r++<<": "<<ret<<endl;
	}					
	
	return 0;
}