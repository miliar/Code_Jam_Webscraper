#ifndef HEADER
#define HEADER
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <string>
#include <sstream>
#include <set>
#include <vector>
using namespace std;

#ifdef _MSC_VER
#include <hash_map>
#include <hash_set>
using namespace stdext;
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif

extern size_t fread (void *__restrict __ptr, size_t __size,
                     size_t __n, FILE *__restrict __stream);

#define FIN(file) freopend(file, "r", stdin)

#define CLR(x) memset(x,0,sizeof(x))
#define SET(x,v) memset(x,v,sizeof(x))

#define PREC(n) cout.setf(ios::fixed);cout.precision(n);

#define VAR(a,b) __typeof(b) a=(b)
#define EH(i,m) for (VAR(i,(m).begin());i!=(m).end();++(i))
#define EHD(i,m) for (VAR(i,(m).rbegin());i!=(m).rend();++(i))
#define IN(x,s) ((s).find(x)!=(s).end())
#define ALL(x) (x).begin(),(x).end()
#define REP(i,s,n) for(int i=(s),_i=(n);i<_i;++i)
#define REPD(i,s,n) for(int i=(s),__i=(n);i>=__i;--i)

#define INF 0x7FFFFFFF
#define EPS 1e-3
#define GT(a,b) ((a)>(b)+EPS)
#define GTE(a,b) ((a)>(b)-EPS)
#define EQ(a,b) ((a)>(b)-EPS && (a)<(b)+EPS)
#define LS(a,b) ((a)<(b)-EPS)
#define LSE(a,b) ((a)<(b)+EPS)
#define SQR(x) ((x)*(x))
#define NORM(x,y) (sqrt(SQR(x)+SQR(y)))

#define MAX(x,y) ((x)>(y)?(x):(y))
#define MIN(x,y) ((x)<(y)?(x):(y))
#define ABS(x) ((x)<0?(-(x)):(x))
#define FABS(x) (LS(x,0.0)?(-(x)):(x))

inline bool _alpha(char c){return isalpha(c);}
inline bool _digit(char c){return isdigit(c);}
inline bool _space(char c){return c<=' ';}
inline bool _notsp(char c){return c>' ';}
inline bool _upper(char c){return isupper(c);}
inline bool _lower(char c){return islower(c);}
inline bool _alnum(char c){return isalnum(c);}
inline bool _notan(char c){return !isalnum(c);}

template<class X, class Y>
X to(Y value){
    stringstream ss(value);
    X res;
    ss>>res;
    return res;
}

istream& in=cin;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
#define V(x) vector<x >
#define VI V(int)
#define VL V(ll)

const double PI=acos(-1.0);
const double E=exp(1.0);
#endif

#ifndef READER
#define READER
#define I_SIZE 81920

char I_buff[I_SIZE];
size_t I_pos,I_len,I_in;
bool I_all;
void I_read(){
    if(I_len>I_pos)memcpy(I_buff,I_buff+I_pos,I_len-I_pos);
    I_len-=I_pos;I_pos=0;
    I_in = fread(I_buff+I_len,1,I_SIZE-I_len,stdin);
    if (I_in != I_SIZE-I_len){I_all=true;}
    I_len+=I_in;I_buff[I_len]=0;
}
inline char I_next(){return I_buff[I_pos++];}
char I_chk_next(){if (!I_all && I_pos+20>I_len)I_read();return I_next();}

void I_init(){I_all=false;I_len=0;I_pos=0;I_read();}
int I_sign(){
    int sign=1;char ch;
    while(((ch=I_chk_next())<'0'||ch>'9')&&ch!='-');
    if (ch=='-')sign=-1;else --I_pos;
    return sign;
}
template <class T> 
size_t I_t(char* p,T f){
    size_t i=1;while(!f(p[0]=I_chk_next()));while(f(p[i]=I_chk_next())){++i;}p[i]=0;--I_pos;return i;
}
char I_c(){char ch;while(_space(ch=I_chk_next()));return ch;}
size_t I_s(char *p){return I_t(p,_notsp);}
size_t I_l(char* p){size_t i=0;while((p[i]=I_chk_next())!='\n'){++i;}p[i]=0;return i;}
size_t I_lt(char *p){size_t i=I_l(p);while(i&&p[i-1]<15)--i;p[i]=0;return i;}
template <class T>
T I(){
    T res=0;char ch;
    while((ch=I_chk_next())<'0' || ch>'9');res=ch-'0';
    while((ch=I_next())>='0' && ch<='9'){res*=10;res+=ch-'0';}
    --I_pos;return res;
}
template <> double I<double>(){
    double res=0.0,p=1;char ch;
    while((ch=I_next())>='0' && ch<='9'){res*=10;res+=ch-'0';}
    if(ch=='.')while((ch=I_next())>='0' && ch<='9'){p*=10;res+=(ch-'0')/p;};
    --I_pos;return res;
}
template <class T> inline T Is(){int s=I_sign();T v=I<T>();return s*v;}
inline bool I_e(){return I_all && I_pos>=I_len;}
#define II (I<int>())
#define IL (I<ll>())
#define IS(x) (I_s(x))
#define IC (I_c())
#define ID (I<double>())
#define IIS (Is<int>())
#define ILs (Is<ll>())
#define IDS (Is<double>())
#endif

int n,m,a;
bool w;

int area(int x1,int y1,int x2,int y2,int x3,int y3){
    return abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3));
}

void debug(int x1,int y1,int x2,int y2,int x3,int y3){
    cout<<"Exp: " << a << " Act: " << area(x1,y1,x2,y2,x3,y3);
    if (a != area(x1,y1,x2,y2,x3,y3)){cout<<"!!!!!!";w=true;}
    if (x1>n || x2>n || x3>n)cout<<"N!!!";
    if (y1>m || y2>m || y3>m)cout<<"M!!!";
}

bool check(int a, int c, int b, int d){
    int x=MAX(a,d);
    int y=b+c;
    return ((x<=n && y<=m) || (x<=m && y<=n));
}

void output(int a, int c,int b,int d){
    int x1=d;
    int y1=c;
    int x2=d-a;
    int y2=b+c;
    if (x1>n || x2>n || y1>m || y2>m){
        swap(x1,y1);
        swap(x2,y2);
    }
    cout<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2;
    //debug(0,0,x1,y1,x2,y2);
}



void Run(){
    w=false;
    REP(cni,1,II+1){
        n=II;
        m=II;
        a=II;
        cout<<"Case #"<<cni<<": ";
        bool ok=false;
        int sqrta=((int)sqrt((double)a));
        REP(i,1,sqrta+1){
            if (a%i==0){
                int j=a/i;
                if ((i<=n && j<=m)){
                    cout<<"0 0 " << i << " 0 " << i<<" "<<j;
                    //debug(0,0,i,0,i,j);
                    ok=true;
                    goto L;
                }
                else if (i<=m && j<=n){
                    cout<<"0 0 " << j << " 0 " << j <<" "<<i;
                    //debug(0,0,j,0,j,i);
                    ok=true;
                    goto L;
                }
            }
        }
        REP(i,1,sqrta+1){
            REP(j,1,sqrta+1){
                int k=a-i*j;
                if (k==0)continue;
                int sqrtk=((int)sqrt((double)k));
                REP(ii,1,sqrtk+1){
                    if (k%ii==0){
                        int jj=k/ii;
                        if (jj>=i && check(i, j, ii, jj)){
                            output(i,j,ii,jj);
                            ok=true;
                            goto L;
                        }
                        if (ii>=i && check(i,j,jj,ii)){
                            output(i,j,jj,ii);
                            ok=true;
                            goto L;
                        }
                        if (jj>=j && check(j,i,ii,jj)){
                            output(j,i,ii,jj);
                            ok=true;
                            goto L;
                        }
                        if (ii>=j && check(j,i,jj,ii)){
                            output(j,i,jj,ii);
                            ok=true;
                            goto L;
                        }
                    }
                }
            }
        }
        L:
        if (!ok)cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    if (w)cout<<"!!!!"<<endl;
}

int main(){
    I_init();
    
    Run();
    
    return 0;
}

