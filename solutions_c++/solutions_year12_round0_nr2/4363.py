
#include<stack>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<iomanip>
#include<utility>
#include<map>
#include<cmath>
#include<vector>
#include<queue>
#include<string>
#include<algorithm>
#include<fstream>

using namespace std;

bool compare( pair< int,int > p1, pair<int ,int > p2)
{
	if(p1.first > p2.first )
		return true;
	if(p1.first == p2.first && p1.second > p2.second)
		return true;
	return false;
}

int main()
{
	int t;
	cin >> t;
	for(int z = 1;z<=t;z++)
	{
	int n,s,p;
	cin >> n>>s>>p;
	vector< pair < int, int > > v;
	for(int i=0;i<n;i++)
	{
           int r ;
	   cin >>r;
	   v.push_back(make_pair(r/3 , r%3));
	}
	sort(v.begin(),v.end(),compare);
	int count = 0;
	for(int i=0;i<n;i++)
	{
		if(v[i].first >= p)
		{
			count ++;
		}
                 else
		 {
                     if(v[i].second == 0)
		     {
			    if(s>0 && v[i].first == p-1 && v[i].first > 0)
			    {
				    count++;
				    s--;
			    }
		     }
		     else
		     {
			     if( v[i].second == 1)
			     {
				     if(v[i].first == p-1)
				     {
                                          count++;
				     }
			     }
			     else
			     {
				     if(v[i].second ==2)
				     {
                                           if(v[i].first == p-1)
					   {
                                                count++;
					   }
					   else
					   {
						   if(s>0 && v[i].first == p-2)
						   {
							   s--;
							   count++;
						   }
					   }
				     }
			     }
                         
		     }
		 }
	}
		 cout<<"Case #"<<z<<": "<<count<<endl;
		 v.clear();
	}
	return 0;
}
