/* Author   : FameofLight */
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stdexcept>
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long int64;
typedef pair<int,int> ii;
typedef vector<string> vs;
#define size(x) (int)((x).size())
#define all(v) (v).begin(), (v).end()
#define For(i,x) for(int i=0;i<x;i++)
#define Forr(i,y,x) for(int i=y;i>=x;i--)
#define Forn(i,y,x) for(int i=y;i<=x;i++)
#define Fill(a, v) memset(a, v, sizeof(a))
#define inRange(x,l,u) ((x)>=(l) && (x)<=(u))
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define Unique(c) sort(all(c)), (c).resize(unique(all(c)) - (c).begin());
#define Foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

const int inf=INT_MAX;
const double eps=1e-8;
const double pi=acos(-1.0);

/* Bitmasking Common Operator Follows */
#define two(X) (1<<(X))
#define setBit(S,X) (S|=two(X))
#define contain(S,X) ((S&two(X))>0)
#define resetBit(S,X) (S&=(~two(X)))

#define twoL(X) (((ll)1)<<(X))
#define setBitL(S,X) (S|=twoL(X))
#define containL(S,X) ((S&twoL(X))>0)
#define resetBitL(S,X) (S&=(~twoL(X)))

template<class T> T lowbit(const T &n) { return (n^(n-1))&n; }
template<class T> int countbit(const T &n) { return (n==0)?0:(countbit(n&(n-1))+1); }

template<class T> inline T sqr(T x){return x*x;}
template<class T> inline T abs(T x){return x<0 ? -x : x;}
template<class T> inline void checkmin(T &a,const T &b) { if (b<a) a=b; }
template<class T> inline void checkmax(T &a,const T &b) { if (b>a) a=b; }
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}
int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)
  {double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)
  {return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}



/* Numeric Function */
bool isMiddle(ll m,ll l,ll h){if(m>=l && m<h)return true; return false;}//Exclusive
bool isMiddlei(ll m,ll l,ll h){if(m>=l && m<=h)return true; return false;}//Inclusive
bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}
template<class T> inline T gcd(T a,T b){if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclide(T a,T b,T &x,T &y){if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}if(b<0){T d=euclide(a,-b,x,y);
y=-y;return d;}if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<class T> inline vector<pair<T,int> > factorize(T n){vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0)
{int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T checkMod(T n,T m) {return (n%m+m)%m;}
template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((ll)(a)*(ll)(b)%(ll)(m))+(ll)(m))%(ll)(m));}
template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T powerMod(T p,int e,T m){if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}
/* End of Numeric Function */

/* Matrix Class */
const int MaxMatrixSize=40;//NOTES:MaxMatrixSize
template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:showMatrix(
  {for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}
template<class T> inline void identityMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:identityMatrix(
  {for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=(i==j)?1:0;}
template<class T> inline void addMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:addMatrix(
  {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=A[i][j]+B[i][j];}
template<class T> inline void subMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:subMatrix(
  {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=A[i][j]-B[i][j];}
template<class T> inline void mulMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//NOTES:mulMatrix(
  { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) for (int k=0;k<n;k++) C[i][j]+=A[i][k]*B[k][j];}
template<class T> inline void addModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:addModMatrix(
  {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]+B[i][j],m);}
template<class T> inline void subModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:subModMatrix(
  {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]-B[i][j],m);}
template<class T> inline void mulModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//NOTES:mulModMatrix(
  { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) for (int k=0;k<n;k++) C[i][j]=(C[i][j]+multiplyMod(A[i][k],B[k][j],m))%m;}
/* End of Matrix Class */

/*Fraction Class */
template<class T> struct Fraction{T a,b;Fraction(T a=0,T b=1);string toString();};
template<class T> bool operator<(Fraction<T> p,Fraction<T> q){return p.a*q.b < p.b*q.a;}
template<class T> bool operator==(Fraction<T> p,Fraction<T> q){return p.a*q.b == p.b*q.a;}
template<class T> string Fraction<T>::toString(){ostringstream sout;sout<<a<<"/"<<b;return sout.str();}
template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.a,p.b*q.b);}
template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b,p.b*q.a);}
template<class T> Fraction<T>::Fraction(T a,T b){T d=gcd(a,b);a/=d;b/=d;if (b<0) a=-a,b=-b;this->a=a;this->b=b;}
template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);}
template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);}
/* End of Fraction Class */

/* Common Coversion */
template<class T> int toInt(T n){stringstream ost;ost<<n;int ret;ost>>ret;return ret;}
template<class T> ll toInt64(T n){stringstream ost;ost<<n;ll ret;ost>>ret;return ret;}
template<class T> string toString(T n){stringstream ost;ost<<n;ost.flush();return ost.str();}
template<class T> double toDouble(T n){stringstream ost;ost<<n;double ret;ost>>ret;return ret;}
template<class T> static void split(const string &s, vector<T> &out){istringstream in(s);out.clear();copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));}
/* End of Common Converstion */

/* Input Output Function (Warning : Only during TLE) */
#define BUFSIZE (1<<20)
char BUF[BUFSIZE+1], *inp=BUF;
#define SPACE(a) (isspace(a))
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define getChar(t){if(!*inp){BUF[fread(BUF,1,BUFSIZE,stdin)]=0;inp=BUF;}t=*inp++;}
#define getInt(j){int t;do{getChar(t);}while(!DIG(t));j=t-'0'; getChar(t);while(DIG(t)){j=10*j+(t-'0');getChar(t);}}
inline void getString(char *j){int t;do{getChar(t);}while(SPACE(t));*(j++)=t;getChar(t);while(!SPACE(t)){*(j++)=t;getChar(t);}*j='\0';}
/* End of Input Output Functions */

/*Debugging */
#define out(x) cout << #x << " = " << x << endl;
#define outArray(x,n) cout<<"{";For(i,n)cout<<x[i]<<", ";cout<<"}"<<endl;
#define outAny(x) cout<<"{";Foreach(it,x)cout << *it << ", " ;cout<<"}"<<endl;
template<typename T,typename TT>ostream &operator<<(ostream &s,pair<T,TT> t){return s<<"("<<t.first<<","<<t.second<<")";}
/* End of Debugging */


/* Don't Code Until You are sure of your Idea , God Bless You ! */

int n;
int X[501][3];
int V[501][3];
double avg[3];
double avgv[3];
double pos[501][3];

double dist(double t)
{
       For(i,n)
       {
               For(j,3)
               {
                       pos[i][j]=(double(X[i][j]) + double(V[i][j])*t);
               }
       }
       double ret=0;
       For(j,3)
       {
               double sum =0;
               For(i,n)sum += pos[i][j];
               sum /= double(n);
               ret += sqr(sum);
       }
       return sqrt(ret);
}
       
                       
               

int main()
{
    #ifdef FAMEOFLIGHT_HOME
     //   freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
		freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    #endif
    int t;
    cin >> t;
    
    For(kase,t)
    {
               
               cin >> n;
               For(i,n)
               {
                       For(j,3)cin >> X[i][j];
                       For(j,3)cin >> V[i][j];
               }
              
               For(i,3)avg[i]=avgv[i]=0.0;
               For(j,3)
               {
                       For(i,n)
                       {
                               avg[j]+=X[i][j];
                               avgv[j]+=V[i][j];
                       }
                       avg[j]/= double(n);
                       avgv[j] /= double(n);
               }
               double num=0.0 , den=0.0;
               For(j,3)
               {
                       num += sqr(avgv[j]);
                       den += (avg[j]*avgv[j]);
               }
               //out(num);
               //out(den);
               double t=.0;
               if(num!=0)t=-(den/num);
               if(t < 0) t = 0.0;
               printf("Case #%d: %.7f %.7f\n",kase+1 , dist(t) , t);
    }
    return 0;
}
