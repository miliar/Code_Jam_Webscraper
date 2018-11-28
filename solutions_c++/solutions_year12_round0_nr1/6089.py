#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <limits>
#include <cstring>
#include <fstream>
#include <string>
using namespace std;

int pel(string s){string t;t=s;reverse(t.begin(),t.end());if(s==t)return 1;return 0;}
string toString(int n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
bool isprime(int m){if(m<2) return 0;for( int i=2; i*i<=m ; i++)if(m%i==0)return 0; return 1;return 0;}

# define eps 1e-8
# define inf (1<<30)
# define pi (2*acos(0.0))
# define __(array,w)   memset(array,w,sizeof array)
# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)
# define all(c) (c).begin(), (c).end()
# define sz(x) x.size()
# define pb push_back
# define UNQ(s) {sort(all(s));(s).erase(unique(all(s)),s.end());}
# define rive(s) reverse(s.begin(),s.end())
# define out(a) cout<<#a<<" #"<<a<<endl;
# define caout(a) cout<<#a<<" "<<++a<<": ";
# define X first
# define Y second
# define MP make_pair
typedef long long LL;
//typedef __int64   LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
typedef map<string,int>msi;
typedef map<vector<int>,int>mvi;
inline bool iseq(double x,double y){if(fabs(x-y)<eps)return true;return false;}
template<typename T>inline double hpt(T x1,T y1,T x2,T y2){return hypot(x1-x2,y1-y2);}
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}
#define PS 5
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}
map<char,char>mp;

int main()
{
mp['a']='y';
mp['b']='h';
mp['c']='e';
mp['d']='s';
mp['e']='o';
mp['f']='c';
mp['g']='v';
mp['h']='x';
mp['i']='d';
mp['j']='u';
mp['k']='i';
mp['l']='g';
mp['m']='l';
mp['n']='b';
mp['o']='k';
mp['p']='r';
mp['q']='z';
mp['r']='t';
mp['s']='n';
mp['t']='w';
mp['u']='j';
mp['v']='p';
mp['w']='f';
mp['x']='m';
mp['y']='a';
mp['z']='q';
mp[' ']=' ';

#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
#endif
    int test,Ctest=0;
    cin>>test;
    getchar();


    while(test--)
    {
        string s,t;
        getline(cin,s);
        cout<<"Case #"<<++Ctest<<": ";
        REP(i,sz(s))
        cout<<mp[s[i]];

        cout<<endl;
    }

    return 0;
}
