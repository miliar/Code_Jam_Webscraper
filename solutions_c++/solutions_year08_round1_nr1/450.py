#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define SZ size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

int n,T;
long long tmp;
 
int main(){
   cin>>T;
   FORN(c,T){
      vector<long long> A,B;
      cin>>n;
      FORN(i,n){
	 cin>>tmp;
	 A.PB(tmp);
      }
      FORN(i,n){
	 cin>>tmp;
	 B.PB(tmp);
      }
      sort(ALL(A));
      sort(ALL(B));
      reverse(ALL(B));
      long long res=0;
      FORN(i,n)
      res+=((long long)(A[i]*B[i]));
      
      cout<<"Case #"<<c+1<<": "<<res<<endl;
   }

    return 0;
}
