#include <iostream>
#include <string>
#include <memory>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>

using namespace std;
typedef long long int LL;

#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define BR cout<<endl
#define PB push_back

#define PP pair<int,int>
#define LP list< PP >
#define VL vector< LP >

#define MAXI 805

/*////////////////////////////////////////////////////////////*/
int main(){
   int T,n,x,y,cas,sum;
   vector<int> v1;
   vector<int> v2;
   
   cin>>T;
   REP(cas,T){
      cout<<"Case #"<<cas+1<<": ";
      cin>>n;
      REP(j,n){cin>>x; v1.PB(x);}
      REP(j,n){cin>>y; v2.PB(y);}
      sort(v1.begin(),v1.end());
      sort(v2.begin(),v2.end());
      sum=0;
      REP(i,n){
         sum+=v1[i]*v2[n-i-1];
      }
      cout<<sum<<endl;
      v1.clear();v2.clear();    
   }
   
   return 0;
}
