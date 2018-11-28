
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define fi(n,i)         for(int i=0;i<n;i++)
#define fab(a,b,i)      for(int i=a;i<=b;i++)
#define max(a,b)        (a>b?a:b)
#define min(a,b)        (a<b?a:b)
#define _abs(x)         (x<0?(-1)*x:x)
#define all(c)          (c).begin(),(c).end()
#define contains(c,x)	(find(all(c),(x))!=(c).end())

#define fs              first
#define sc              second
#define pb              push_back
#define mp              make_pair
#define D(x)		cout << #x << " -> "<<x << endl;

typedef long long int64;
typedef unsigned long long uint64;
#define two(x)		(1<<(x))
#define twoL(x)		(((uint64)(1))<<(x))


const double oo = (1<<30);
const double PI = acos(-1);
const double eps = 1e-9;

using namespace std;

template<class T>
ostream& operator<<(ostream& out,vector<T> v)
{
    int sz = v.size();
    out <<"[";
    for(int i=0;i<sz;i++)
    {
	out<<v[i];
	if(i+1<sz)cout << ", ";
    }
    out<<"]";
    return out;
}


long long best=-1;
int N;
vector<int> candy;

void f(long long a, long long b ,long long reala , long long realb, int i)
{
//    cout << "calling with: "<<a<<","<<b<<","<<reala<<","<<realb<<","<<i<<endl;
    if(i>=N)
    {
	if(a != b || !reala || !realb)
	   return;
	best = max(best,max(reala,realb));
//	cout << "[reala , realb] = ["<<reala<<", "<<realb<<"]"<<endl;
	return;
    }
    f(a^candy[i] ,b,reala+candy[i],realb,i+1);
    f(a,b^candy[i],reala,realb+candy[i],i+1);
    return;
}

int main()
{
   ios_base::sync_with_stdio(0);
   freopen("2011/C.in","r",stdin);
   freopen("2011/C.out","w",stdout);
   int T,C;
   cin>>T;
   fi(T,c)
   {
       best = -1;
       candy.clear();
       cin>>N;
       fi(N,i)
       {
	   cin>>C;
	   candy.pb(C);
       }
//       cout << "candy: "<<endl<<candy<<endl;
       f(0LL,0LL,0LL,0LL,0);
       cout <<"Case #"<<c+1<<": ";
       if(best!=-1)cout << best;
       else cout<<"NO";
       cout <<endl;
   }
   return 0;
}



















