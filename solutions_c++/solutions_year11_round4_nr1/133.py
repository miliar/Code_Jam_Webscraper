#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <set>
#include <queue>
#include <sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define mp make_pair
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define oo 1000111222
#define lloo 1LL << 60
using namespace std;

int n;
vector < pair<int,double> > a;

int main()
{
    freopen("alarge.in","r",stdin); freopen("a.out","w",stdout);
    int test,it,i,j,run,walk,len,free,x,y,v;
    double re,t;
    cin >> test;
    fr(it,1,test)
    {
       cout << "Case #" << it << ": ";
       cin >> len >> walk >> run >> t >> n;
       re=0;
       a.clear();
       free=len;
       fr(i,1,n)
       {
          scanf("%d%d%d",&x,&y,&v);
          y-=x;
          free-=y;
          a.pb(mp(v,1.0*y));
       }
       a.pb(mp(0,1.0*free));
       sort(a.begin(),a.end());
       fr(i,0,n)
       {
//          cout << a[i].first << " " << a[i].second << " ";
          if (a[i].second==0) continue;
          double need=a[i].second/(a[i].first+run);
//          cout << need << " ";
          if (t<=need)
          {
             re+=t;
             a[i].second-=t*(run+a[i].first);
             t=0;
             re+=a[i].second/(walk+a[i].first);
          }
          else 
          {
             re+=need;
             t-=need;  
          }
//          cout << t << endl;
       }
       printf("%.9lf\n",re);
       //cerr << it << endl;
    }
    //while (1);
    return 0;
}
