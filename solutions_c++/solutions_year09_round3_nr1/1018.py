//Author : Pankaj Kumar
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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
#include <stack>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
using namespace std;

/*START OF TEMPLATE:BY_PANKAJ_CODEGAMBLER*/
#define INF 1e10//::INF
#define VAR(x,a) 	__typeof(a) x=(a)//::VAR(
#define FE(it,c) 	for(VAR(it,(c).begin());it!=(c).end();++it)//::FE(
#define FOR(i,a,b)  	for(int i=(int)(a),_b=(int)(b) ; i < _b;i++)//::FOR(
#define FORR(i,a,b) 	for(int i=(a),_b=(b);i>=_b;--i)//::FORR(
#define	REP(i,n)    	FOR(i,0,n)//::REP(
#define ALL(c) 		(c).begin(),(c).end()//::ALL(
#define SZ		size()//::SZ
#define PB		push_back//::PB
#define PF		push_front//::PF
#define V(x)    vector< x >//::V(
#define VI      V(int)//::VI
#define VII     V(VI)//::VII
#define VS      V(string)//::VS
#define PI      pair<int,int>//::PI
#define MP      make_pair//::MP

const double eps=1e-11;//::eps
const double pi=acos(-1.0);//::pi
typedef long long LL;//::LL
typedef unsigned long long ULL;//::ULL
typedef long double LD;//::LD

/* Bitmasking Common Operator Follows */
#define two(X) (1<<(X))//::two(
#define twoL(X) (((LL)1)<<(X))//::twoL(
#define setBit(S,X) (S|=two(X))//::setBit(
#define setBitL(S,X) (S|=twoL(X))//::setBit(
#define contain(S,X) ((S&two(X))>0)//::contain(
#define containL(S,X) ((S&twoL(X))>0)//::containL(
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//::lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//::countbit(

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//::checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//::checkmax(
template<class T> inline T sqr(T x){return x*x;}//::sqr

/* Numeric Function */
template<class T> inline T gcd(T a,T b)//::gcd(
    {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//::lcm(
    {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline bool isPrime(T n)//::isPrime(
    {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T euclide(T a,T b,T &x,T &y)//::euclide(
    {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
    if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
    if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<class T> inline vector<pair<T,int> > factorize(T n)//::factorize(
    {vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
    i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T eularFunction(T n)//::eularFunction(
    {vector<pair<T,int> > R=factorize(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}

/*Matrix Operations*/
const int MaxMatrixSize=40;//::MaxMatrixSize
template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//::showMatrix(
    {for(int i=0;i<n;i++){for(int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}
template<class T> inline T checkMod(T n,T m) {return (n%m+m)%m;}//::checkMod(
template<class T> inline void identityMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//::identityMatrix(
    {for(int i=0;i<n;i++)for(int j=0;j<n;j++) A[i][j]=(i==j)?1:0;}
template<class T> inline void addMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//::addMatrix(
    {for(int i=0;i<n;i++) for(int j=0;j<n;j++) C[i][j]=A[i][j]+B[i][j];}
template<class T> inline void subMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//::subMatrix(
    {for(int i=0;i<n;i++) for(int j=0;j<n;j++) C[i][j]=A[i][j]-B[i][j];}
template<class T> inline void mulMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//::mulMatrix(
    { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) C[i][j]+=A[i][k]*B[k][j];}
template<class T> inline void addModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//::addModMatrix(
    {for(int i=0;i<n;i++) for(int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]+B[i][j],m);}
template<class T> inline void subModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//::subModMatrix(
    {for(int i=0;i<n;i++) for(int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]-B[i][j],m);}
template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((LL)(a)*(LL)(b)%(LL)(m))+(LL)(m))%(LL)(m));}//::multiplyMod(
template<class T> inline void mulModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//::mulModMatrix(
    { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int k=0;k<n;k++) C[i][j]=(C[i][j]+multiplyMod(A[i][k],B[k][j],m))%m;}
template<class T> inline T powerMod(T p,int e,T m)//::powerMod(
    {if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}

/*Point&Line*/
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//::dist(
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//::distR(
template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}//::cross(
int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)//::crossOper(
    {double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)//::isIntersect(
    {return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}
bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}//::isMiddle(

/* Most Common Coversion */
template<class T> int toInt(T n){int r=0;istringstream ist(n);ist>>r;return r;}//::toInt(
template<class T> LL toLong(T n){istringstream ist(n);LL r;ist>>r;return r;}//::toLL(
template<class T> string toString(T n){stringstream ost;ost<<n;ost.flush();return ost.str();}//::toString(
template<class T> LD toDouble(T n){LD r=0;istringstream sin(n);sin>>r;return r;}//::toDouble(
template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}//::stoa(
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}//::atos(
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}//::atov(
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}//::vtoa(
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//::stov(
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}//::vtos(

/* Mathematics Fraction Class */
template<class T> struct Fraction{T a,b;Fraction(T a=0,T b=1);string toString();};//::Fraction
  template<class T> Fraction<T>::Fraction(T a,T b){T d=gcd(a,b);a/=d;b/=d;if (b<0) a=-a,b=-b;this->a=a;this->b=b;}
  template<class T> string Fraction<T>::toString(){ostringstream sout;sout<<a<<"/"<<b;return sout.str();}
  template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);}
  template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);}
  template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.a,p.b*q.b);}
  template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b,p.b*q.a);}

/* Input Output Function */
#define BUFSIZE (1<<10)
char BUF[BUFSIZE+1], *inp=BUF;
#define DIG(a) (((a)>='0')&&((a)<='9'))//::DIG(
#define GETCHAR(t){if(!*inp){BUF[fread(BUF,1,BUFSIZE,stdin)]=0;inp=BUF;}t=*inp++;}//::GETCHAR(
#define GETNUM(j){int t;do{GETCHAR(t);}while(!DIG(t));j=t-'0'; GETCHAR(t);while(DIG(t)){j=10*j+(t-'0');GETCHAR(t);}}//::GETNUM(

/* Only for Debugging */
#define out(__debug) cout << #__debug << " = " << __debug << endl;//::out(
template<class T> void outContainer(T A)//::outContainer
    {cout<<"{"; FE(it,A)cout << *it << " " ;cout<<"}"<<endl;}
template<class T> void outArray(T A[],int n)//::outArray
    { cout<<"{"; for (int i=0;i<n;i++) cout<<A[i]<<" "; cout<<"}"<<endl;}
template<class T> void outVector(vector<T> A,int n=-1)//::outVector
    { if (n<0) n=SIZE(A); cout<<"{"; for (int i=0;i<n;i++) cout<<A[i]<<" "; cout<<"}"<<endl;}
template<class T> static void split(const string &s, vector<T> &out)//::split
    {istringstream in(s);out.clear();copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));}
/*END TEMPLATE:BY_PANKAJ_CODEGAMBLER*/
//Don't Code Until You are sure of your Idea , God Bless You !

#define codegambler
int main()
{
    #ifdef codegambler
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int T;
    cin>>T;
    int abc=1;
    while(T--)
    {
        string s;
        cin>>s;
        int sz=s.SZ;
        size_t fnd;
        string c;
        int base=1;
        vector<unsigned long long> v;
        map<char,int>mp;
        int f=1;
        REP(i,sz)
        {
            c=s.substr(0,i);
            fnd=c.find(s[i]);
            if(fnd!=string::npos)
            {
                 v.PB(mp[s[i]]);
                 //cout<<int(fnd)<<"@";cout<<int(string::npos)<<"#";

            }
            else
            {
                if(f--==0)mp[s[i]]=0;
                else
                    mp[s[i]]=base++;
                v.PB(mp[s[i]]);
            }
               
                
        }
       // cout<<base<<endl;
       
        int size=v.SZ;
        int tmp=0;
        int x=0;//cout<<base<<"#";
        //FE(it,v)cout<<*it<<" ";cout<<endl;
        for(int i=size-1;i>=0;--i)
        {
               v[i]*=pow(double(base),double(x)); 
                x++;
                
        }
        VI tp;
        int y=0;
        unsigned long long res=0;
        REP(i,size)res+=v[i];
        cout<<"Case #"<<abc++<<": "<<res<<endl;
    }
 	return 0;
}
