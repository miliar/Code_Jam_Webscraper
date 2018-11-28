#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_ACRUSH_TOPCODER
#define fori(i,n) for(int i=0; i<n; i++)
#define rep(i, a, b) for(int i=a;i<=b;i++)
#define forv(i, a) for(size_t i=0; i<a.size(); i++)

#define PB push_back
#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define two(X) (1<<(X))//NOTES:two(
#define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
#define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
#define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(
const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
int compare(double a,double b){return(fabs(a-b)<=eps)?0:((a<b)?-1:1);}
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
typedef pair<int,int> ipair;//NOTES:ipair
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
//Numberic Functions
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
//Matrix Operations
const int MaxMatrixSize=40;//NOTES:MaxMatrixSize
template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:showMatrix(
{for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}
template<class T> inline T checkMod(T n,T m) {return (n%m+m)%m;}//NOTES:checkMod(
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
template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((int64)(a)*(int64)(b)%(int64)(m))+(int64)(m))%(int64)(m));}//NOTES:multiplyMod(
template<class T> inline void mulModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//NOTES:mulModMatrix(
{ T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
  for (int i=0;i<n;i++) for (int j=0;j<n;j++) for (int k=0;k<n;k++) C[i][j]=(C[i][j]+multiplyMod(A[i][k],B[k][j],m))%m;}
template<class T> inline T powerMod(T p,int e,T m)//NOTES:powerMod(
{if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}
//Point&Line
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//NOTES:dist(
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//NOTES:distR(
template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}//NOTES:cross(
int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)//NOTES:crossOper(
{double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)//NOTES:isIntersect(
{return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}
bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}//NOTES:isMiddle(
//Translator
bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase(
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase(
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter(
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase(
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase(
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(
template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}//NOTES:stoa(
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}//NOTES:atos(
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}//NOTES:atov(
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}//NOTES:vtoa(
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//NOTES:stov(
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}//NOTES:vtos(
//Fraction
template<class T> struct Fraction{T a,b;Fraction(T a=0,T b=1);string toString();};//NOTES:Fraction
template<class T> Fraction<T>::Fraction(T a,T b){T d=gcd(a,b);a/=d;b/=d;if (b<0) a=-a,b=-b;this->a=a;this->b=b;}
template<class T> string Fraction<T>::toString(){ostringstream sout;sout<<a<<"/"<<b;return sout.str();}
template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);}
template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);}
template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.a,p.b*q.b);}
template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b,p.b*q.a);}
//ENDTEMPLATE_BY_ACRUSH_TOPCODER
struct Point
{
  double x,y;
  Point(double _x=0,double _y=0)
  {
    x=_x;
    y=_y;
  }
  int compareTo(const Point &other)
  {
    int c=compare(x,other.x);
    if (c!=0) return c;
    return compare(y,other.y);
  }
};
struct Circle
{
  double x,y,r;
  Circle(double _x=0,double _y=0,double _r=0)
  {
    x=_x;
    y=_y;
    r=_r;
  }
  int compareTo(const Circle &other)
  {
    int c1=compare(x,other.x);
    if (c1!=0) return c1;
    int c2=compare(y,other.y);
    if (c2!=0) return c2;
    return compare(r,other.r);
  }
};

double ppDistance(const Point &a,const Point &b)
{
  return dist(a.x,a.y,b.x,b.y);
}
int getIntersect(const Circle &A,const Circle &B,Point &P,Point &Q)
{
  double X1=A.x,Y1=A.y,X2=B.x,Y2=B.y;
  double R1=A.r,R2=B.r;
  double dst=dist(X1,Y1,X2,Y2);
  if (dst>R1+R2+eps || dst<fabs(R1-R2)-eps) return 0;
  //(x-X1)^2+(y-Y1)^2=sqr(R1)=x^2-2*X1*x+X1^2+y^2-2*Y1*y+Y1^2 (1)
  //(x-X2)^2+(y-Y2)^2=sqr(R2)=x^2-2*X2*x+X2^2+y^2-2*Y2*y+Y2^2 (2)
  //(2)-(1):  sqr(R2)-sqr(R1)=2*(X1-X2)*x+2*(Y1-Y2)*y+sqr(X2)-sqr(X1)+sqr(Y2)-sqr(Y1)
  //	 :  (X1-X2)*x+(Y1-Y2)*y-(sqr(X1)-sqr(X2)+sqr(Y1)-sqr(Y2)-sqr(R1)+sqr(R2))/2.0;
  double a=X1-X2;
  double b=Y1-Y2;
  double c=-(a*(X1+X2)+b*(Y1+Y2)-sqr(R1)+sqr(R2))/2.0;
  double CX=X1,CY=Y1;
  //ax+by+c=0
  //(+by+c+aCX)^2+(ay-aCY)^2=(aR)^2
  double x1,y1,x2,y2;
  if (fabs(a)>fabs(b))
  {
    double A=sqr(a)+sqr(b);
    double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
    double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
    double delta=sqr(B)-4*A*C;
    if (delta<-eps) return 0;
    if (delta<0) delta=0;
    delta=sqrt(delta);
    y1=(-B+delta)/(2*A);x1=(-c-b*y1)/a;
    y2=(-B-delta)/(2*A);x2=(-c-b*y2)/a;
    P.x=x1;P.y=y1;
    Q.x=x2;Q.y=y2;
  }
  else
  {
    swap(a,b);swap(CX,CY);
    double A=sqr(a)+sqr(b);
    double B=2.0*b*(c+a*CX)-2.0*sqr(a)*CY;
    double C=sqr(c+a*CX)+sqr(a)*(sqr(CY)-sqr(R1));
    double delta=sqr(B)-4*A*C;
    if (delta<-eps) return 0;
    if (delta<0) delta=0;
    delta=sqrt(delta);
    y1=(-B+delta)/(2*A);x1=(-c-b*y1)/a;
    y2=(-B-delta)/(2*A);x2=(-c-b*y2)/a;
    swap(x1,y1);swap(x2,y2);
    swap(a,b);swap(CX,CY);
    P.x=x1;P.y=y1;
    Q.x=x2;Q.y=y2;
  }
  return 2;
}

int stest, n;
char a[103][103];
double wp[103], owp[103], oowp[103], res[103];
int W[103],T[103];

int main() {
  //freopen("input.txt", "r", stdin);
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  scanf("%d", &stest);
  rep(test, 1, stest) {
    scanf("%d", &n);
    fori(i,n)scanf("%s", a[i]);
    fori(i,n) {
      int tol = 0;
      int w = 0;
      fori(j,n)tol+=a[i][j]!='.', w+=a[i][j]=='1';

      if(tol == 0) wp[i] = 0.;
      else wp[i] = (w+0.)/tol;

      W[i] = w;
      T[i] = tol;
    }

    fori(i,n) {
      int tol = 0;
      double sum = 0;
      fori(j,n)if(a[i][j] != '.') {
        if(a[j][i] == '1')
          sum += (W[j]-1.)/(T[j]-1.);
        else sum += (W[j]+0.)/(T[j]-1.);
        tol++;
      }

      if(tol == 0) owp[i] =0.;
      else owp[i] = sum / tol;
    }

    fori(i,n) {
      int tol = 0;
      double sum = 0;
      fori(j,n)if(a[i][j] != '.') {
        sum += owp[j];
        tol++;
      }

      if(tol == 0) oowp[i] =0.;
      else oowp[i] = sum / tol;
    }

    fori(i,n) res[i] = 0.25 * wp[i] + 0.5*owp[i] + 0.25 * oowp[i];
    //sort(res, res + n);
    printf("Case #%d:\n", test);
    //for(int i = n-1; i>=0; i--) printf("%.6lf\n", res[i]);
    fori(i,n) printf("%.8lf\n", res[i]);
  }
  return 0;
}
