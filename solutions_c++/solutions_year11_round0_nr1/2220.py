#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int main()
{
  freopen("A-large.in.txt","r",stdin);
  freopen("A-large.out","w",stdout);
  int l,t,n,k,x,i;
  char c;
  char dump;
//  scanf("%d",&t);
  cin >> t;
  for (l=0;l<t;l++)
  {
    // scanf("%d", &n);
    cin >> n;
//    typedef pair<int, int> pi;
    vector<int> o,os,bs;
    vector<int> b;
    for (i = 0; i < n; i++)
    {
      // scanf("%c%d", &c, &x);
      cin >> c >> x;
      // cout << c << " " << x;
      if ( c== 'O')
      {
        o.push_back(x);
        os.push_back(i);
      }
      else
      {
        b.push_back(x);
        bs.push_back(i);
      }
    }
    if (o.size() == 0)
    {
      os.push_back(n+1);
      o.push_back(1);
    }
    if (b.size() == 0)
    {
      bs.push_back(n+1);
      b.push_back(1);
    }
    // cout << o[0] << o[1] << os[0] << os[1] << endl;
    // cout << b[0] << b[1] << bs[0] << bs[1] <<endl;
    int step = 0, opos = 1, bpos = 1;
    int oind = 0, bind = 0;
    for (i = 0; i < 10001; i++)
    {
      // cout << i << " " << step << " " << opos << " " << bpos << endl;
      if (step > n-1)
      {
        printf("Case #%d: ", l+1);
        printf("%d\n", i);
        break;
      }
      if (os[oind] == step) // o turn
      {
        if (opos == o[oind])
        {
          step++;
          oind = oind < o.size()-1 ? oind+1: oind;
          if (bpos == b[bind])
          ;
          else if (bpos > b[bind])
            bpos -- ;
          else
          {
            bpos ++;
          }
        }
        else if (opos > o[oind])
         {
           opos --;
           if (bpos == b[bind])
           {
             ;
           }
           else if (bpos > b[bind])
           {
             bpos--;
           }
           else
           {
             bpos++;
           }
         }
         else if (opos < o[oind])
         {
           opos++;
           if (bpos == b[bind])
           {
             ;
           }
           else if (bpos > b[bind])
           {
             bpos--;
           }
           else
           {
             bpos++;
           } 
         }
      }
      else if(bs[bind] == step)
      {
        if (bpos ==  b[bind])
        {
          step++;
          bind = bind < b.size()-1 ? bind+1: bind;
          if (opos == o[oind])
          {
            ;
          }
          else if (opos > o[oind])
          {
            opos--;
          }
          else
          {
            opos++;
          } 
        }
        else if( bpos > b[bind])
        {
          bpos --;
          if (opos == o[oind])
          {
            ;
          }
          else if (opos > o[oind])
          {
            opos--;
          }
          else
          {
            opos++;
          } 
        }
        else 
        {
          bpos ++;
          if (opos == o[oind])
          {
            ;
          }
          else if (opos > o[oind])
          {
            opos--;
          }
          else
          {
            opos++;
          } 
        }
      }
      
      
    }

  }
	return 0;
}

