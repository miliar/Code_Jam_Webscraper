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
      
#define MINI(a,b)  ((a<b)?(a):(b))

using namespace std;

int calc(int P,vector<int> v)
{
vector<int> A,B;
A.pb(1);
B.pb(P);
int z=v.sz;
int r=0;
for(int a=0;a<z;a++)
      {
      //cout<<"R is "<<r<<endl;
      bool todo1=1;
      for(int x=0;(todo1) &&x<A.sz;x++) 
			{ 
			if(A[x]<=v[a]&&B[x]>=v[a])
				  {
				  todo1=false;
				  r+=((B[x])-(A[x]));    
				 // cout<<" Added from : "<<B[x]<<" - "<<A[x]<<endl;
			if(v[a]==A[x])
						    {
						    A[x]=((A[x])+1);
						    }
				  else if(v[a]==B[x])
						    {
						    B[x]=((B[x])-1);
						    }
				else {
				      A.pb(v[a]+1);
				      B.pb(B[x]);
				      //m1[v[a]+1]=i1->second;
				      B[x]=v[a]-1;
				      }
						    
						    
				  }
			}
       }
//cout<<"R is "<<r<<endl;

return r;
}

int main()
{
  /*
  int P=20;
  vector<int> v1;
  v1.pb(14);
  v1.pb(3);
  v1.pb(6);
  calc(P,v1);
  */
  
int T,P,Q;  
  cin>>T;
  vector<int> v,bv;
  int temp;
  for(int a=0;a<T;a++)
	      {
	      cin>>P>>Q;
	      v.clear();
		for(int b=0;b<Q;b++)
		   {  cin>>temp; v.pb(temp); }
	      sort(all(v));
	      int best=calc(P,v);
	      bv=v;
	      while(next_permutation(v.begin(),v.end()))
			{
			//best=MINI(best,calc(P,v));
			//cout<<"Best is "<<best<<endl;
			//for(int s=0;s<v.sz;s++) cout<<v[s]<<" "; cout<<endl;
			if(calc(P,v)<best) {
					    best=calc(P,v);
					    bv=v;
					    }
			}
	      	//cout<<"Best is "<<best<<endl;
		//for(int s=0;s<bv.sz;s++) cout<<bv[s]<<" "; cout<<endl;
		
	      cout<<"Case #"<<a+1<<": "<<best<<endl;
	      }
	    
return 0;
}
