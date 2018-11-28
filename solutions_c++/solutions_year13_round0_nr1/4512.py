#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
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
#include<stdio.h>



#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;

char a[4][4];

bool x()
{
        FOR(j,0,4)
        {
            int x=0,t=0;
           FOR(i,0,4) 
            {
              if(a[j][i]=='X') x++;
              if(a[j][i]=='T') t++;
            }
            if(x==4) return true;
            if(x==3&&t==1) return true;     
        }        
        
        FOR(j,0,4)
        {
            int x=0,t=0;
           FOR(i,0,4) 
            {
              if(a[i][j]=='X') x++;
              if(a[i][j]=='T') t++;
            }
            if(x==4) return true;
            if(x==3&&t==1) return true;     
        }        
            int t=0,x=0;
          FOR(i,0,4)
          {
              if(a[i][i]=='X') x++;
              if(a[i][i]=='T') t++;
          }    
          if(x==4) return true;
          if(x==3&&t==1) return true;
          
          x=0,t=0;
          FOR(i,0,4)
          {
              if(a[i][3-i]=='X') x++;
              if(a[i][3-i]=='T') t++;
          }
          if(x==4) return true;
          if(x==3&&t==1) return true;
    
    return false;
}

bool o()
{
        FOR(j,0,4)
        {
            int x=0,t=0;
           FOR(i,0,4) 
            {
              if(a[j][i]=='O') x++;
              if(a[j][i]=='T') t++;
            }
            if(x==4) return true;
            if(x==3&&t==1) return true;     
        }        
        
        FOR(j,0,4)
        {
            int x=0,t=0;
           FOR(i,0,4) 
            {
              if(a[i][j]=='O') x++;
              if(a[i][j]=='T') t++;
            }
            if(x==4) return true;
            if(x==3&&t==1) return true;     
        }        
            int t=0,x=0;
          FOR(i,0,4)
          {
              if(a[i][i]=='O') x++;
              if(a[i][i]=='T') t++;
          }    
          if(x==4) return true;
          if(x==3&&t==1) return true;
          
          x=0,t=0;
          FOR(i,0,4)
          {
              if(a[i][3-i]=='O') x++;
              if(a[i][3-i]=='T') t++;
          }
          if(x==4) return true;
          if(x==3&&t==1) return true;
    
    return false;
}

bool draw()
{
    int c=0;
    FOR(i,0,4)
    {
        FOR(j,0,4)
        if(a[i][j]=='X'||a[i][j]=='O'||a[i][j]=='T') c++;
    }
    if(c==16) return true;
    return false;
}
int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
  
  int t;
  cin>>t;

  FOR(k,1,t+1)
  {
      FOR(i,0,4)
      FOR(j,0,4) cin>>a[i][j];
      cout<<"Case #"<<k<<": ";
      if(x())  cout<<"X won\n";
      else if(o()) cout<<"O won\n";
      else if(draw()) cout<<"Draw\n";
      else cout<<"Game has not completed\n";
  }
  return 0;
  
}
