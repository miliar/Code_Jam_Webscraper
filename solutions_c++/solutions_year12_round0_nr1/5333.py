/*
uva :
author : rafsan
algo :
*/

#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<queue>
#include<fstream>
#include<sstream>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<utility>
#include<climits>
#include<iomanip>
#include<ctime>
#include<complex>
using namespace std;


#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n) for (int i=0;i<(n);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)

#define inf INT_MAX/3
#define pb push_back
#define MP make_pair
#define all(a) (a).begin(),(a).end()
#define SET(a,c) memset(a,c,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define pii pair<int,int>
#define pcc pair<char,char>
#define pic pair<int,char>
#define pci pair<char,int>
#define VS vector<string>
#define VI vector<int>
#define debug(x) cout<<#x<<": "<<x<<endl
#define MIN(a,b) (a>b?b:a)
#define MAX(a,b) (a>b?a:b)
#define pi 2*acos(0.0)
#define INFILE() freopen("in0.txt","r",stdin)
#define OUTFILE()freopen("out0.txt","w",stdout)
#define in scanf
#define out printf
#define ll long long
#define ull unsigned long long
#define eps 1e-9
#define mod 1000000007
template<typename T>inline T  S(T a){return a*a;}
template<typename T>inline string tostring(T a){ostringstream os("");os << a;return os.str();}
template<typename T>inline ll tolong(T a){ll res;istringstream os(a);os>>res;return res;}
template<typename T>inline T gcd(T a, T b){if (b == 0)return a;else return gcd(b, a % b);}
template<typename T>inline ull bigmod(T a, T b, T m){if (b == 0)return 1;else if (b % 2 == 0)return S(bigmod(a, b / 2, m)) % m;else return (a % m*bigmod(a, b - 1, m)) % m;}
template<typename T>inline VS parse(T str){VS res;string s;istringstream os(str);while(os>>s)res.pb(s);return res;}
template<typename T>inline ull  dist(T A,T B){ull res=(A.x-B.x)*(A.x-B.x)+(A.y-B.y)*(A.y-B.y);return res;}
template<typename T>inline T power(T base,int po){T res=1;if(base==0)return 0; FOR(i,0,po)res*=base;return res;}
int main()
{
    string s="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string s1="our language is impossible to understand";
    string s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string s3="there are twenty six factorial possibilities";
    string s4="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string s5="so it is okay if you want to just give up";
    map<char,char>mp;
    map<char,char>::iterator it;
    int l=s.size();
    FOR(i,0,l)mp[s[i]]=s1[i];
     l=s2.size();
    FOR(i,0,l)mp[s2[i]]=s3[i];
     l=s4.size();
    FOR(i,0,l)mp[s4[i]]=s5[i];
    mp['q']='z';
    mp['z']='q';
    mp[' ']=' ';
    //for(it=mp.begin();it!=mp.end();it++)cout<<it->first<<" "<<it->second<<endl;
int ks;
freopen("Speaking in Tongues.out","w",stdout);
freopen("A-small-attempt0.in","r",stdin);
in("%d",&ks);
getline(cin,s);
FOR(cas,1,ks+1)
{
    getline(cin,s);
    l=s.size();
    cout<<"Case #"<<cas<<": ";
    FOR(i,0,l)cout<<mp[s[i]];
    cout<<endl;
}

}
