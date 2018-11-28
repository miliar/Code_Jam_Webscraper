#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^=a;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
int main(){
//	freopen("B-small-attempt4.in","r",stdin);freopen("B-small-attempt4.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
   int i,j,k,l,cnt;
   int T;
   int pt;
   string x;
   cin >> T;
   for (j = 1; j <= T; j ++ ) {
       cin >> x;
       pt = -1;
       for (i = SZ(x) - 1; i >=1 ; i --){
           if (x[i] > x[i - 1]){
              pt = i - 1;
              break;
           } 
       }
       if (pt == -1){
          sort(x.begin(),x.end());
          for (l = 0; l < SZ(x); l ++ ) {
              if (x[l] != '0') break;
          }
          x.erase(0,l);
          x.insert(1,l+1,'0');
       }else if (pt == SZ(x) - 2){
           swap(x[pt],x[SZ(x)-1]);
       }else if (x[pt] < x[SZ(x) - 1]){
           swap(x[pt],x[SZ(x)-1]);
           swap(x[pt+1],x[SZ(x)-1]);
           sort(x.begin()+pt+1,x.end()-1);
       }else{
           for (k = SZ(x) - 1; k > pt; k --){
               if (x[k] > x[pt]) break;
           }
           swap(x[k],x[pt]);
           sort(x.begin()+pt+1,x.end());
       }
       cout << "Case #" << j << ": " << x << endl;
   }
//   system("pause");
   return 0;
}
