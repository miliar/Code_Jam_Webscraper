#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

#define AND &&
#define OR ||




vector<LL> first,second;



LL compare1 (const void * a, const void * b)
{
  return ( *(LL*)a - *(LL*)b );
}

LL compare2 (const void * a, const void * b)
{
  return ( *(LL*)b - *(LL*)a );
}


int main()
{
    LL T;
    cin>>T;
    LL cost;
    LL n;
    LL vecA;
    LL counter =0;
    while(T--)
    {         
              counter++;
                     cin>>n;
              first.clear();
              second.clear();
              REP(i,n)
              {
                      cin>>vecA;
                      //cout<<vecA;
                      first.push_back(vecA);
              }
              sort(first.begin() , first.end());

              REP(i,n)
              {
                      cin>>vecA;
                      //cout<<vecA;
                      second.push_back(vecA);
              }
              sort(second.begin() , second.end());
              
              cost = 0;

              REP(i,n){
              cost+=first[i]*second[n-i-1];
              }
             cout<<"Case #"<<counter<<": "<<cost<<endl;
    }
    
    //system("pause");
    
}

