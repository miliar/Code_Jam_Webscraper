//Program:A

#include<iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>


using namespace std;
typedef vector<long int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

#define pb push_back
#define REP(i,n) for(i=0;i<(n);i++)
#define FOR(i,a,b) for(i=(a),i<(b);i++)
#define FORD(i,a,b) for(i=(a);i>(b);i--)
#define ALL(c)  (c).begin(),(c).end()
#define OUT(c) cout<<(c)<<endl

#define INF 100000

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

//Global:



//

//Function DEF:

//

int main()
{
  freopen("C12321.in", "r", stdin);
  freopen("res.txt", "w", stdout);
long long int t,r,k,n,sum,a[100001],l,count,i,j,g,m;
long long int temp,c=0,cnt;
cin>>t;
while(t--)
{c++;
memset(a,0,sizeof(a));
  cin>>r>>k>>n;
  REP(i,n)
  {
   cin>>g;
    a[i]=g;      }
l=0;
      count=0;
for(m=0;m<r;m++)
{ sum=0;
temp=k;
cnt=0;
//cout<<m<<" ";
    while(1)
    {

    cnt++;

    if(cnt>n)
    break;

    if(a[l]<=temp)
    {
    sum+=a[l];
    temp-=a[l];
    count+=a[l];
    //cout<<l<<" "<<n<<endl;
    l++;
   if(l>=n)
   l=0;
   }
    else
    break;
    }

     //cout<<sum<<" "<<m<<endl;
}
    cout<<"Case #"<<c<<": "<<count<<endl;
    }
return 0;
}
