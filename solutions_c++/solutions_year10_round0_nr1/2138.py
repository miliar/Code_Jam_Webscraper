#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)


typedef long long int LL;

int main() {
   // freopen("A-small-attempt0.in","r",stdin);
  // freopen("i","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("A-large.o","w",stdout);

    int t,n,k,total;
    cin>>t;
    int cc=0;

    while (t--) {
        cc++;
        cin>>n>>k;

        cout<<"Case #"<<cc<<": ";

        total=k;
//cout<<total<<" "<<n<<" "<<(1<<n)<<" "<<total-(1<<n)<<endl;
      int coeff=total/(1<<n);
      total-=coeff*(1<<n);
       //while ((total-(1<<n))>=0) {
      //      total=total-(1<<n);
    //    }

        if (total==((1<<n)-1)) {
            cout<<"ON\n";
        } else
            cout<<"OFF\n";

    }

    return 0;
}
