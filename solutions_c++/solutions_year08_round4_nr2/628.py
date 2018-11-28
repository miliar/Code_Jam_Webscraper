#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define forn(i,n) for (int i=0;i<n;++i)
#define all(a) a.begin(),a.end()
#define LL long long



void solve(){
     LL n,m,a;
     cin >> n >> m >> a;
     for (LL x1=0;x1<=n;x1++)
     for (LL y1=0;y1<=m;y1++)
     for (LL x2=0;x2<=n;x2++)
     for (LL y2=0;y2<=m;y2++){
     LL temp=x1*y2-x2*y1;
     if (temp<0) temp=-temp;
     if (temp==a)
     {
     	cout<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<endl;
        return;
     }
     }
     cout<<"IMPOSSIBLE";
     cout<<endl;
}

int main()
{
     freopen("B-small-attempt2.in", "r", stdin);
     freopen("B-small-attempt2.out", "w", stdout);
     int T;
     cin >> T;
     forn(t,T)
     {
          cout<<"Case #"<<t+1<<": ";
          solve();
     }

     return 0;
}
