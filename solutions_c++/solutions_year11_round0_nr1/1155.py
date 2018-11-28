#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define oo 1000111222
#define pii pair<int,int>
using namespace std;
typedef long long ll;
const int dx[]={-1,0,1,0,-1,1,1,-1};
      int dy[]={0,1,0,-1,1,1,-1,-1};
      
vector < pii > a;

int main()
{
   freopen("A-large.in","r",stdin); freopen("gcj-qualA.out","w",stdout);
   int test,n,it,i,j,x,y,re,cur; 
   char c,cc;
   cin >> test; 
   fr(it,1,test)
   {
      cin >> n;
      a.clear();
      fr(i,1,n*2)
        if (i%2) cin >> c;
        else 
        {
           cin >> x;
           if (c=='B') a.pb(mp(x,0));
           else a.pb(mp(x,1));
        }
      fr(i,0,n-1)
        if (!a[i].second) break;
      fr(j,0,n-1)
        if (a[j].second) break;
      x=y=1; re=0; cur=0;
      while (i<n || j<n)
      {
         int ok=0;
         if (i<n)
         {
            if (x==a[i].first)
            {
              if (i==cur)
              {
                i++; cur++; ok=1;
                while (i<n && a[i].second) i++;
              }
            }
            else
              if (x<a[i].first) x++;
              else x--;
         }
         if (j<n)
         {
            if (y==a[j].first)
            {
              if (j==cur && !ok)
              {
                j++; cur++;
                while (j<n && !a[j].second) j++;
              }
            }
            else
              if (y<a[j].first) y++;
              else y--;
         }
         re++;
      }
      cout << "Case #" << it << ": " << re << endl;
  }
   return 0;
}
