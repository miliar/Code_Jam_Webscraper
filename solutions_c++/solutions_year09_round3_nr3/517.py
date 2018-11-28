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
#include <fstream>
#define pb push_back
using namespace std;
int main()
 {
 
  int t;
  cin>>t;int ppp=1;
  while(t--)
    {
	  int size;
	  cin>>size;
	  int aa[size+2];
	  
	 
	  int num;
	  cin>>num;
	  vector<int>v;
      for(int i=0;i<num;i++)
        {
		  int k;cin>>k;v.pb(k);
         }
		 
		 vector<int>ans;
		 do 
		 {
		   int sum=0;
		   memset(aa,0,sizeof(aa));
		   
		  for(int i=0;i<v.size();i++)
		   {
		    aa[v[i]-1]=-1;
		     for(int j=v[i];j<size;j++)
			  {
			   if(aa[j]==-1)break;
			  else sum++;
			   }
			   for(int j=v[i]-2;j>=0;j--)
			    {
				 if(aa[j]==-1)
				  break;
				 else sum++;
				  }
				  }
				  ans.pb(sum);
	    }while(next_permutation(v.begin(),v.end()));
				  cout<<"Case #"<<ppp<<": "<<*min_element(ans.begin(),ans.end())<<endl;
				  ppp++;
				  }
				  
				   return 0;
		    
  
  }