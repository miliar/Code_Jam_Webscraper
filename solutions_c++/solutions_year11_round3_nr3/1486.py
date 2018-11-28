#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

using namespace std;

bool _cmp(ll a, ll b)
{
 return a<b;     
}
vector<ll> v[40];
int main()
{
 freopen("C-small-attempt1.in","r",stdin);
 freopen("a.out","w",stdout);
 long t;
 ull n,l,h,temp;
 ull count;
 bool err,res;
 cin>>t;
 for(long i = 0; i < t; i++)
 {
  printf("Case #%d: ",i+1);
  cin>>n>>l>>h;;
  for(int j = 0; j < n; j++)
  {
   cin>>temp;
   v[i].push_back(temp);
  }
  count = 1;
  sort(v[i].begin(),v[i].end(),_cmp);
  res = false;  
  for(int j = l; j <= h; j++)
  {
   err = false;
   for(ll h = 0; h < n; h++)
   {
    if(!(v[i][h] % j == 0 || j % v[i][h] == 0))
    {
     err = true;
    }
   }
   if(err == false)
   {
    res = true;
    cout<<j<<endl;
    break;      
   }
   /*count*=v[i][j];
   if(count >= l)
   {
    if(count > h)
    {
     printf("NO\n");
     break;
    }
    else
    {
     err = false;
     for(int h = j + 1; h < n; h++)
     {
      if(!(count&v[i][h] == 0 || v[i][h] % count == 0))
      {
       err = true;
       break;
      }
     }
     if(err == false)
     {
      cout<<count<<endl;
      break;     
     }
    }
   }*/
  }
  if(res == false)
   cout<<"NO"<<endl;
 } 
 return 0;
}
