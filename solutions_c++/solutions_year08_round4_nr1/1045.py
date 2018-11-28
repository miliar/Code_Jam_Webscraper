#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <queue>
using namespace std;
 
#define all(c)         (c).begin(),(c).end()
#define fori(c,i)     for(typeof(c).begin() i = (c).begin(); i != (c).end(); i++)
 
typedef long long     LL;
typedef vector<int>   vi; 
typedef vector< vi >   vvi; 
#define PB push_back
#define ST first
#define ND second
#define MP make_pair

    int n,v;

struct node
{
  bool zm;
  int an;
  bool wart;
};
    vector <node> T;

bool przel(int c)
{
   if(T[c].an == 3) return T[c].wart;
   
   bool tmp;
   
   if(T[c].an == 1) tmp = przel(2*c) && przel(2*c+1);
   else tmp = przel(2*c) || przel(2*c+1);
   
   T[c].wart = tmp;
   return T[c].wart;
}

LL cnt = 0;

bool rob(int c, int & zm)
{
   if(T[c].an == 3) return T[c].wart;
   if( T[c].wart == v) return T[c].wart;
   if(T[c].zm)
   {
      if(T[c].an == v)        // zmieniamy bramke
      {
        zm++;
        T[c].an = !T[c].an;
        if( T[c].an )     // and
        {
           if( T[2*c].wart && T[2*c+1].wart == v)
           {
             T[c].wart = v;
             return v;
           }

        }
        else
        {   
          if( T[2*c].wart || T[2*c+1].wart == v)
           {
             T[c].wart = v;
             return v;
           }
        }
      }
   }  // zmiana dokonala sie , ale nie mamy tego co chcemy

   if( v == 0 )
   {
     int zm1=0,zm2=0;
     if( T[c].an == 1)
     {
        T[c].wart = rob( 2*c,zm1) && rob(2*c+1,zm2);
        if(T[c].wart == v)
        {
          int zm3 = 99999999;
          if( T[2*c].wart == v) zm3 = min(zm3,zm1);
          if( T[2*c+1].wart == v) zm3 = min(zm3,zm2);
          zm+=zm3;
        }
     }
     else
     {
        T[c].wart = rob( 2*c,zm1) || rob(2*c+1,zm2);
        if(T[c].wart == v) zm+=zm1+zm2;

     }

   }
   
   
   else // v == 1
   {
        int zm1=0,zm2=0;
     if( T[c].an == 0)
     {
        T[c].wart = rob( 2*c,zm1) || rob(2*c+1,zm2);
        if(T[c].wart == v)
        {
          int zm3 = 99999999;
          if( T[2*c].wart == v) zm3 = min(zm3,zm1);
          if( T[2*c+1].wart == v) zm3 = min(zm3,zm2);
          zm+=zm3;
        }
     }
     else
     {
        T[c].wart = rob( 2*c,zm1) && rob(2*c+1,zm2);
        if(T[c].wart == v) zm+=zm1+zm2;

     }

   }

   return T[c].wart;
}

int main()
{
  int tst;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {

    cin >> n >> v;
    T.resize(n+1);
    int zmian = 0;
    vector <bool> Z(n+1);
    for(int i=1;i<=(n-1)/2;i++)
    {
      cin >> T[i].an >> T[i].zm;
      T[i].wart = 0;
      if( T[i].zm == 1) zmian++;
      Z[i] = T[i].an;
    }
    for(int i=((n-1)/2) +1;i<=n;i++)
    {
      cin >> T[i].wart;
      T[i].an = 3;
      T[i].zm = 0;
    }
    przel(1);

    if( T[1].wart == v)
    {
     cout << "Case #" << num <<": " << 0 <<   endl;
     continue;
    }

    int p = 1 << zmian;
  //  cout << p << endl;
    int wszy = 99999;
    for(int w=0;w<p;w++)
    {
   //   cout << "=" << endl;
      int h = w;
      int ile = 0;
        for(int i=1;i<=(n-1)/2;i++)
        {

          if( T[i].zm)
          {
             if(h%2) { T[i].an = !Z[i]; ile++; }
             else T[i].an = Z[i];
             h/=2;
          }
        }
        przel(1);
        if( T[1].wart == v && wszy > ile) wszy = ile;
    }

  //  int zm = 0;
  //  rob(1,zm);
  //  cout << "v" << v << " " << T[1].wart << endl;
 /*   if( T[1].wart != v)
    {
     cout << "Case #" << num <<": " << "IMPOSSIBLE" <<   endl;
     continue;
    }   */

    if( wszy == 99999)
    {
     cout << "Case #" << num <<": " << "IMPOSSIBLE" <<   endl;
     continue;
    }

    cout << "Case #" << num <<": " << wszy <<   endl;

  }

  return 0;
}
