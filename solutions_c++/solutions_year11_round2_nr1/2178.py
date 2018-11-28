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
#include <string.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define zero(a) memset(a, 0, sizeof(a))
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64

const double pi=acos(-1.0);//NOTES:pi
const double eps=1e-11;//NOTES:eps
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr

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


typedef vector<int> vint;

typedef struct _nodo{
  vint adjs;
  int color;
  _nodo(){color=0;}
} nodo;


#define p(a) cout << a << endl

int main()
{
        int _n;
        cin >> _n;
        forn(_i,_n){
                int tam;
                cin >> tam;
                cin.ignore();
                vector < vector<char> > mat(tam, vector<char>(tam) );
                string s;
                forn(i,tam){
                        getline(cin,s);
                        forn(j,tam)
                                mat[i][j] = s[j];
                }
                
                vector<double> WP,OWP,OOWP,vjugados,vganados,vperdidos;

                forn(i,tam){
                        double jugados=0.0,ganados=0.0,perdidos=0.0;
                        forn(j,tam){
                                if(mat[i][j]=='1'){jugados++;ganados++;}
                                if(mat[i][j]=='0'){jugados++;perdidos++;}
                        }
                        WP.pb( (ganados/jugados));
                        vjugados.pb(jugados);
                        vganados.pb(ganados);
                        vperdidos.pb(perdidos);
                }

                forn(i,tam){
                        double temp=0.0;
                        double cont=0.0;
                        forn(j,tam){

                             if(mat[i][j] !='.'){
                                     cont++;
                                     if(mat[i][j] == '0'){
                                        temp += ((vganados[j]-1)/(vjugados[j]-1));}
                                     else
                                        temp += ((vganados[j])/(vjugados[j]-1));
                             }
                        }
                        
                        OWP.pb(temp/cont);
                }

                forn(i,tam){
                        double temp=0.0;
                        double cont=0.0;
                        forn(j,tam){

                             if(mat[i][j] !='.'){
                                     cont++;
                                     temp += OWP[j];
                             }
                        }
                        
                        OOWP.pb(temp/cont);
                }

                p("Case #"<<_i+1<<":");
                cout.precision(12);
                forn(i,tam) p(0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);




        }
}
