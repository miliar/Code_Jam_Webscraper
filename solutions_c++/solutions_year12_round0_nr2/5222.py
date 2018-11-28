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
#include <ctime>

using namespace std;

#ifdef __GNUC__
typedef long long ll;typedef unsigned long long ull;
#else
typedef __int64 ll;  typedef unsigned __int64 ull;
#pragma warn -csu
#endif

//Type Definition
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<ll>vll;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef map<string,ll> msl;
typedef map<ll,ll>mll;
typedef map<pll,ll>mpl;


#define REP(i,n)      for(i=0;i<n;i++)
#define REV(i,n)      for(i=n;i>=0;i--)
#define FOR(i,p,k)    for(i=p; i<k;i++)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define Sort(x)       sort(x.begin(),x.end())
#define Reverse(x)    reverse(x.begin(),x.end())
#define inf           99999999
#define SZ            100010
#define LD            long double
#define pb            push_back
#define pi            3.141592653589793
#define sz            size()
#define mem(a,b)      memset(a,b,sizeof(a))
#define two(i)        ((ll)1<<i)
#define clr           clear()
#define mkp           make_pair
using namespace std;

//Important Functions
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template<class T> T Abs(T x) {return x > 0 ? x : -x;}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}


//int,double is converted to string
template<class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
//string is converted to int
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
//string is converted to Long long
ll toLl(string s){ll r=0;istringstream sin(s); sin>>r; return r;}
//string is coverted to Double
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble
//check character is vowel
bool IsVowel(char ch){ch=tolower(ch);if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')return true;return false;}
//isUpperCase
bool isUpperCase(char c){return c>='A' && c<='Z';}
//isLowerCase
bool isLowerCase(char c){return c>='a' && c<='z';}
//compute b^p
ll Pow(ll B,ll P){	ll R=1;	while(P>0)	{if(P%2==1)	R=(R*B);P/=2;B=(B*B);}return R;}
//compute b^p%m
int BigMod(ll B,ll P,ll M){	ll R=1;	while(P>0)	{if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;}	return (int)R;}
/*calculates (a*b)%c taking into account that a*b might overflow */
ll mulmod(ll a,ll b,ll c){ ll x = 0,y=a%c; while(b>0){ if(b%2 == 1){x=(x+y)%c;} y=(y*2)%c;b/= 2;}return x%c;}

//ASCII Chart
void ASCII_Chart(){int i,j,k;printf("ASCII Chart:(30-129)\n");FOR(i,30,50){REP(j,5){k=i+j*20;printf("%3d---> '%c'   ",k,k);}printf("\n");}}
//Degree to Radian
double deg2rad(double x){ return (pi*x)/180.0; }
//Radian to Degree
double rad2deg(double x){ return (180.0*x)/pi; }


//ll month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
//string monthName[]={"","JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"};
//string dayName[]={"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};
//ll ax[]={1,0,-1,0};ll ay[]={0,1,0,-1}; //4 Direction
//ll ax[]={1,1,0,-1,-1,-1,0,1};int ay[]={0,1,1,1,0,-1,-1,-1};//8 direction
//ll ax[]={2,1,-1,-2,-2,-1,1,2};int ay[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//ll ax[]={2,1,-1,-2,-1,1};int ay[]={0,1,1,0,-1,-1}; //Hexagonal Direction
//ll month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

int ar[1000];

ll kase,test,cnt,i,j,k,p,s,n,mx,sum;
string str;

vector<pair<ll,pair<ll,ll> > > arr,arr1,arr2;

bool isSurprising(pair<ll,pair<ll,ll> > arr)
{
    ll ii = abs(arr.first-arr.second.first);
    ll jj = abs(arr.first-arr.second.second);
    ll kk = abs(arr.second.first-arr.second.second);
    return (ii>1 || jj>1 || kk>1);
}
void count_max(pair<ll,pair<ll,ll> > arr,pair<ll,pair<ll,ll> > arr1,pair<ll,pair<ll,ll> > arr2)
{
    ll cnt=0;
    if(arr.first>=p || arr.second.first>=p || arr.second.second>=p)cnt++;
    if(arr1.first>=p || arr1.second.first>=p || arr1.second.second>=p)cnt++;
    if(arr2.first>=p || arr2.second.first>=p || arr2.second.second>=p)cnt++;
    setmax(mx,cnt);
}
void count_max1(pair<ll,pair<ll,ll> > arr,pair<ll,pair<ll,ll> > arr1)
{
    ll cnt=0;
    if(arr.first>=p || arr.second.first>=p || arr.second.second>=p)cnt++;
    if(arr1.first>=p || arr1.second.first>=p || arr1.second.second>=p)cnt++;
    setmax(mx,cnt);
}
void count_max2(pair<ll,pair<ll,ll> > arr)
{
    ll cnt=0;
    if(arr.first>=p || arr.second.first>=p || arr.second.second>=p)cnt++;
    setmax(mx,cnt);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>n>>s>>p;
        arr.clr;
        arr1.clr;
        arr2.clr;
        mx=0;
        REP(i,n)
        {
            cin>>ar[i];
        }

        REP(i,11)
            REP(j,11)
                REP(k,11)
                {
                    sum = i+j+k;
                    ll ii = abs(i-j);
                    ll jj = abs(i-k);
                    ll kk = abs(j-k);

                    if(sum==ar[0] && ii<=2 && jj<=2 && kk<=2)arr.pb(mkp(i,mkp(j,k)));
                    if(n>1)
                        if(sum==ar[1] && ii<=2 && jj<=2 && kk<=2)arr1.pb(mkp(i,mkp(j,k)));
                    if(n>2)
                        if(sum==ar[2] && ii<=2 && jj<=2 && kk<=2)arr2.pb(mkp(i,mkp(j,k)));
                }
        if(n==3)
        REP(i,arr.sz)
        {
            REP(j,arr1.sz)
            {
                REP(k,arr2.sz)
                {
                    cnt=0;
                    if(isSurprising(arr[i]))cnt++;
                    if(isSurprising(arr1[j]))cnt++;
                    if(isSurprising(arr2[k]))cnt++;
                    if(s==cnt)count_max(arr[i],arr1[j],arr2[k]);
                }
            }
        }
        if(n==2)
        REP(i,arr.sz)
        {
            REP(j,arr1.sz)
            {
                cnt=0;
                if(isSurprising(arr[i]))cnt++;
                if(isSurprising(arr1[j]))cnt++;
                if(s==cnt)count_max1(arr[i],arr1[j]);

            }
        }
        if(n==1)
        REP(i,arr.sz)
        {
            cnt=0;
            if(isSurprising(arr[i]))cnt++;
            if(s==cnt)count_max2(arr[i]);
        }
        cout<<"Case #"<<++kase<<": "<<mx<<endl;
    }
    return 0;
}



