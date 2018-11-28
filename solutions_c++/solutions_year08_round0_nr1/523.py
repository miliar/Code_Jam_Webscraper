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

vector <string> Q;
vector <string> E;
int s;
int q;
int swps;
          /*
int solve(int swp, int act, string last)
{
   if( swp >= swps) return swps;
   if( act == q) return swp;
   if( last == Q[act] )
   {
     int wyn = 9999999;
     for(int i=0;i<s;i++)
     {
        if(last != E[i])
        {
          wyn = min(wyn, solve(swp+1,act+1, E[i]));

        }
     }
     return wyn;

   }
   else return solve(swp,act+1, last);
}
            */

int main()
{
  int tst;
  string cc;
  cin >> tst;
  int num = 0;
  while(++num <= tst)
  {
    cin >> s;
    swps = 999999;
    E.resize(s);
    getline(cin,cc);
    for(int i=0;i<s;i++)
    {
      getline(cin,E[i]);
 //   cout << E[i] << endl;
    }
    vector <bool> U(s,false);

    int used = 0;
    cin >> q;   getline(cin,cc);
    string L = "";
    Q.resize(q);
    vvi Z(s, vector<int>() );
    for(int i=0;i<q;i++)
    {
      string tmp;
      getline(cin,Q[i]);
      for(int j=0;j<s;j++)
      {
        if( Q[i] == E[j])
        {
          Z[j].push_back(i);
        }
      }
 //     cout << tmp << endl;

    }
    int act;
    swps = 0;
    int now = 0;
    // first
    for(int i=0;i<s;i++)
    {
       if( Z[i].size() == 0 ) { now = 9999999; break;}
       if( Z[i][0] > now) { now =  Z[i][0]; act = i; }
    }


 //   cout << now << " " << act << endl;

    while( now < q )
    {
   //   cout << now << endl;
   //   cout << swps << endl;
      swps++;
      int new_act = act;
      int new_now = now;
      for(int i=0;i<s;i++)
      {
        if( act == i ) continue;

         int j = 0;
         while( j < Z[i].size() && now >= Z[i][j])
         {

            j++;
         }
         if( j == Z[i].size() ) {  /*cout << "----";*/ new_now = 99999999;  break; }
         if( new_now < Z[i][j])
         {

           new_now =  Z[i][j];
           new_act = i;
         }
      }

      act = new_act;
      now = new_now;

    }



  /*  for(int i=0;i<s;i++)
      swps = min(swps,solve(0,0,E[i]));           */

    cout << "Case #" << num <<": " << swps << endl;
  }

  return 0;
}
