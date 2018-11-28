#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef  long long int lli;
typedef long double ld;

int mint(int *ar,int n)
{

    int m=0;
    m=ar[0];
    for(int i=0;i<n;i++)
    {
      if(ar[i]<m) m=ar[i];
    }
    return m;
}
int main() {

  freopen("C-large.in","r",stdin);
   freopen("C-large.out","w",stdout);
    int t,n,x=0;
    cin>>t;
    while(t--)
    {
        cin>>n;
        x++;
        int candies[1005]={0};
        long sum=0;
        int exor=0;
        for(int i=0;i<n;i++)
        {
            cin>>candies[i];
            exor^=candies[i];
            sum+=candies[i];
        }
        if(exor==0)  cout<<"Case #"<<x<<": "<<sum-mint(candies,n)<<endl;

        else cout<<"Case #"<<x<<": "<<"NO"<<endl;
    }

    return 0;
}



