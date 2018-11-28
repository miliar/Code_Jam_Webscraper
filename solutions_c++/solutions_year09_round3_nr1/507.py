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
 
//my MACROS
 
#define VF vector<float>     
#define VVF vector<vf>        
#define VD vector<double>       
#define VVD vector<vd>       
#define VI vector<int>  
#define VVI vector<vi>  
#define VS vector<string>  
#define VVS vector<vs>     
 
#define LL long long     
#define LD long double     
#define LI long int  
#define INF (int)1e9+1  
 
#define FOR(i,a,b) for(int i=a;i<b ;i++)     
#define REP(i,n) for(int i=0;i<n ;i++)
#define pb push_back  
#define itr iterator     
 
#define sz size()     
#define all(x) x.begin(),x.end()     
#define PEEK(x) {cout<<#x<<"="<<x;}  
#define MOD 1234567891 
      
using namespace std;

int main()
{
  int T;
  cin>>T;
  string s;
  for(int i=0;i<T;i++)
	    {
  cin>>s;
  map<char,int> m1;
  int pos=0;
  for(int j=0;j<s.length();j++) { 
				  if(m1.find(s[j])==m1.end()) {
							      m1[s[j]]=pos;
							      pos++;
							      }
                                 }
  for(map<char,int>::iterator i1=m1.begin();i1!=m1.end();i1++)
	      {
	      if((i1->second)==0) i1->second=1;
	      else if((i1->second)==1) i1->second=0;
	//      cout<<i1->first<<" "<<i1->second<<endl;
	      }
  if(pos==1) pos++;
  //cout<<"Pos is "<<pos<<endl;
  unsigned long long val=0;
  for(int j=0;j<s.length();j++)
		      {
		      val*=pos;
		      val+=m1[s[j]];
		      }
       cout<<"Case #"<<i+1<<": "<<val<<endl;
		 	    }

  return 0;
}

