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
#define REP(i,n) for (LL i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (LL var=pocz; var<=koniec; ++var)
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


/*
int compare(const void *a,const void *b) {
PII *x = (PII *) a;
PII *y = (PII *) b;
return x->second - y->second;
}
*/

vector <LL> arr;

bool compare(PII x, PII y)
{
     return (x.second - y.second);
}


LL licz(LL n)
{
           vector <LL> estimate(n,1);
           //REP(i,n)cout<<estimate[i];
           //cout<<endl;
           LL count=0;
          
           FOR(i,0,n-1){
                        FORD(j,i,0){
                                    estimate[i] += arr[i]>arr[j]?estimate[j]:0;
                                    }
                                    estimate[i] %= 1000000007;
                                    count += estimate[i];
                        }
                        return count%1000000007;
}


int main()
{
    LL T;
    cin>>T;
    LL counter =0;
    LL n,m,x,y,z;
    

    while(T--)
    {         
              counter++;
              cin>>n>>m>>x>>y>>z;
              LL abc;
                  vector <LL> nums;     
                  arr.clear();
                  
                  REP(i,m){
                           cin>>abc;
                  nums.push_back(abc);
                  //cout<<abc;
                  }
                  REP(i,n){
                          arr.push_back(nums[i%m]);
                          nums[i%m] = (x*nums[i%m] + y*(i+1))%z;
                          }
                  
                  /*REP(i,n)
                          cout<<arr[i]<<" ";
                  if(T==18)break;*/
             cout<<"Case #"<<counter<<": "<<licz(n)<<endl;
    }
    
    //system("pause");
    
}

