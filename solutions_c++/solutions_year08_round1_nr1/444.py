#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

int main() {
    
    int t;
    sf("%d",&t);
    int kase=1;
    while ( t--) {
          int n;
          sf("%d",&n);
          vector<int> x,y;
          x.clear();y.clear();
          int i;
          int num;
          for ( i=0;i<n;i++)
           sf("%d",&num), x.pb(num);
          for(i=0;i<n;i++)
           sf("%d",&num), y.pb(num);
          sort(x.begin(),x.end() );
          sort(y.begin(), y.end() );
          reverse(y.begin(),y.end());
          INT sum = 0;
          INT one=1;
          for(i=0;i<n;i++)
           sum += one*x[i]*y[i];
          pf("Case #%d: ",kase++);
          cout<<sum<<endl; 
    }
	return 0;
}
