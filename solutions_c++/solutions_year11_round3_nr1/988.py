/***    786
    Md. Saiful Islam Saif
    CSE - SUST.
***/

#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>

using namespace std;

#ifdef __GNUC__
typedef long long ll;typedef unsigned long long ull;
#else
typedef __int64 ll;  typedef unsigned __int64 ull;
#endif

#define inf (1<<30)-1
#define SIZE 100
#define pi (2*acos(0.0))
#define forn(i,n) for (i=0;i<n;i++)
#define forr(i,n) for (i=n-1;i>=0;i--)
#define forab(i,p,k) for (i=p; i<=k;i++)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)

#define bug(x)    cout<< "->" <<#x<<": "<<x<<endl
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define mp(a,b) make_pair(a,b)
#define zero(x,with) memset(x,with,sizeof(x))
#define copy(c,r)   memcpy(c,r,sizeof(r))
#define sz(x) (int)x.size()
#define length(x) (int)x.length()
#define all(x) x.begin(),x.end()
#define pb push_back
#define popcount(i) __builtin_popcount(i)
#define gcd(a,b)    __gcd(a,b)

#define fs first
#define sc second
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define maxi(v) *max_element(all(v))
#define mini(v) *min_element(all(v))
#define CS c_str()
#define clr clear()
#define err 1e-9
#define even(a) ((a)%2==0)
#define odd(a) ((a)%2==1)

typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<ll>vll;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef vector<vll>vvll;
typedef vector<vd>vvd;
typedef vector<pii>vpii;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef map<pii,int>mpi;

template<class T> inline T gcd(T a,T b) {if(!b) return a; else return gcd(b,a%b);}
template<class T> void b_sort(vector<T>& VT) {for(int i=VT.sz;i>0;i--)for(int j=1;j<i;j++)if(VT[j]<VT[j-1]) swap(VT[j],VT[j-1]);}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline bool isprime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T mod(T n,T m) {return (n%m+m)%m;} //For Positive Negative No.
template<class T> string tostring(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
int toint(string s){int r=0;istringstream sin(s);sin>>r;return r;}
ll toll(string s){ll r=0;istringstream sin(s); sin>>r; return r;}
template<class T> void debug(const T& e){cout<<e<<endl;}
template<class T1,class T2> void debug(const T1& e1,const T2& e2){cout<<e1<<"\t"<<e2<<endl;}
template<class T1,class T2,class T3> void debug(const T1& e1,const T2& e2,const T3& e3){cout<<e1<<"\t"<<e2<<"\t"<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void debug(const T1& e1,const T2& e2,const T3& e3,const T4& e4){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void debug(const T1& e1,const T2& e2,const T3& e3,const T4& e4,const T5& e5){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<"\t"<<e5<<endl;}
template<class T> void debug(vector<T>& e){int i;forn(i,sz(e)) cout<<e[i]<<" ";cout<<endl;}
template<class T> void debug(vector< basic_string<T> >& e){int i,j;forn(i,sz(e)) {forn(j,sz(e[i])) cout<<e[i][j];cout<<endl;} cout<<endl;}
template<class T> void debug(vector< vector<T> >& e,int row,int col){int i,j;forn(i,row) {forn(j,col) cout<<e[i][j]<<"\t";cout<<endl;} cout<<endl;}
template<class T> void debug(T e[SIZE][SIZE],int row,int col){int i,j;forn(i,row) {forn(j,col) cout<<e[i][j]<<" ";cout<<endl;}}
inline bool iseq(double x,double y){if(fabs(x-y)<err)return true;return false;}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}

ll Pow(ll B,ll P){  ll R=1;  while(P>0)  {if(P%2==1)  R=(R*B);P/=2;B=(B*B);}return R;} //compute b^p
//struct pq{    int cost,node;bool operator<(const pq &b)const{return cost>b.cost;}};// Min Priority Queue

//typedef struct {     int x,y; }st;
//st XX[100];
//bool comp(st a,st b){    return a.x > b.x;}   //Comp Sort

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("AA.out","w",stdout);

    int i,n,test,kase =1,re,rd,cnt,j,r,c;

    char a[100][100];

    scanf("%d",&test);
    while(test--)
    {
        rd = re = 0;
        cin >> r >> c;

        forn(i,r)
        {
            cnt = 0;
            forn(j,c)
            {
                cin >> a[i][j];
                if(a[i][j] == '#')cnt++;
            }
            if(cnt % 2)rd = 1;

            re += cnt;
        }

        printf("Case #%d:\n",kase++);

        if(rd == 1 || re % 4 != 0)
        {
            printf("Impossible\n");
            continue;
        }


        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(i+1 < r && j+1 < c)
                {
                    if(a[i][j] == '#' && a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
                    {
                        a[i][j] = '/';
                        a[i][j+1] = '\\';
                        a[i+1][j] = '\\';
                        a[i+1][j+1] = '/';
                    }
                }
            }
        }

        forn(i,r)
        {
            forn(j,c)
            {
                printf("%c",a[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}




