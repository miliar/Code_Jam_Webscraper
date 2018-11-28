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

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

long long pw(int base,int pw)
{
     long long ans=1;
     for(int i=0;i<pw;i++)
     ans*=base;
     return ans;
}

int main()
{
  int t,x,i;
  S(t);
  FOR(x,t)
  {
          string s,ans;
          int a[65],j;
          map<char,int> mp;
          map<char,int> val;
          int base=0;
          cin>>s;
          //s=ans;
          FOR(i,s.size())
          {
              if(mp[s[i]]==0)
              {
                base++;
                mp[s[i]]=1;
              }           
          }
          
          if(base == 1 )base++;
         FOR(i,65)
         a[i]=i;
         
         a[0]=1;
         a[1]=0;
         
         j=0;
         
         FOR(i,s.size())
         val[s[i]]=-1;
         
         int k,p=s.size()-1;
         long long sum=0;
         FOR(k,s.size())
         {
      
              if(val[s[k]]==-1)
              {
                  val[s[k]] =  a[j++];           
              }
              sum+=(val[s[k]]*pw(base,p));
              p--;
              //cout<<val[s[k]];
                      
         }
         cout<<"Case #"<<x+1<<": "<<sum<<endl; 
          
  }
return 0;
}
