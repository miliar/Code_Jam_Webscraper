#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define fi(n) for (int i=0;i<(n);++i)
#define gsort(a,b) sort(a,b,greater<typeof(*a)>());
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef __int64 LL;
typedef pair<int,int> PII;
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream ss;
typedef istringstream iss;
typedef ostringstream oss;
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclide(T a,T b,T &x,T &y)//NOTES:euclide(
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<class T> inline vector<pair<T,int> > factorize(T n)//NOTES:factorize(
  {vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
   i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T eularFunction(T n)//NOTES:eularFunction(
  {vector<pair<T,int> > R=factorize(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}
double sqr(double x){return x*x;}
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//NOTES:dist(
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//NOTES:distR(
template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}//NOTES:stoa(
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}//NOTES:atos(
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}//NOTES:atov(
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}//NOTES:vtoa(
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//NOTES:stov(
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}
template<typename T> inline string str(const T &t){oss s;s<<t;return s.str();}
template<typename T> inline LL Int(const T &t){stringstream s;s<<t;LL r;s>>r;return r;}
template<typename T> inline double Double(const T &t){stringstream s;s<<t;double r;s>>r;return r;}
template<typename T> inline int size(const T &t) {return t.size();}
template<class T,class U> T cast(U x){ostringstream os; os<<x; T res; istringstream is(os.str()); is>>res; return res;}
inline string tolower(string s){fi(size(s)) s[i]=tolower(s[i]);return s;}
inline string toupper(string s){fi(size(s)) s[i]=toupper(s[i]);return s;}
#define M 10005
#define eps 0.00000001
int T,pd,pg;
LL n;
int main()
{
    int i,j;
    freopen("D:\\A-large.in","r",stdin);
    freopen("D:\\A-large.out","w",stdout);
    scanf("%d",&T);
    for (int ca=1;ca<=T;ca++)
    {
        scanf("%I64d%d%d",&n,&pd,&pg);
        if (pg==100 && pd<100)
        {
            printf("Case #%d: Broken\n",ca);
            continue;
        }
        else if (pg==0 && pd>0)
        {
            printf("Case #%d: Broken\n",ca);
            continue;
        }
        int PD=100/gcd(100,pd);
        bool ck=0;
        if (PD<=n)
            ck=1;
        if (ck) printf("Case #%d: Possible\n",ca);
        else printf("Case #%d: Broken\n",ca);
    }
    return 0;
}
