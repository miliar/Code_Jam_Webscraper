#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include<malloc.h>
#include<string>
using namespace std;

int main()
{
vector<string>v;
int l,d,n,i,j,ll,cas=0;
cin>>l>>d>>n;

string s;
	for(i=0;i<d;i++)
		{
		  cin>>s;
		  v.push_back(s);	 
		  
		}

map<char,int> mp[l];
map<char,int>::iterator it;
while(n--)
{
  cas++;
                cin>>s;
               ll=s.size();j=0;
 // cout<<s<<endl;
                   for(i=0;i<ll;)
                    {
	//cout<<i<<" "<<j<<endl;
     //if(s[i++]==' ')continue;
	 
                      if(isalpha(s[i]))
                        {
							mp[j][s[i]]=1;i++;j++;
					     	while(isalpha(s[i]))
			               {
			                 mp[j][s[i]]=1;i++;j++; 
			               }
	                    }	 
	                  else
	                    {
		//cout<<i<<" "<<j<<endl;
		                 i++;
	                    while(1)
	                    {
	                     if(s[i]==')')break;
	                     mp[j][s[i++]]=1;
	                    }
						i++;
						j++;
	   //cout<<i<<" "<<j<<endl;
					    }
	 	 
                    }
 
  int ans=0;
  for(i=0;i<d;i++)
  {
       
       for(j=0;j<l;j++)
	   {
	      if(mp[j][v[i][j]]!=1)
		  break;
	   }
	   if(j==l)ans++;
  }
  cout<<"Case #"<<cas<<": ";
  cout<<ans<<endl;
  for(i=0;i<l;i++)
  mp[i].clear();
  }
  return 0;
}
