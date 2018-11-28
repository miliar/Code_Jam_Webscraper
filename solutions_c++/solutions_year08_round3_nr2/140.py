#include <algorithm> 
#include <cctype> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <deque> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <string> 
#include <vector> 

using namespace std; 

template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

#define bublic public
#define TynKogep TOPCODER 
#define clr(a); memset(a,0,sizeof(a));
#define pb push_back
#define sz size()  
#define ld long double
#define istr istringstream

long long c=0,ans=0;
int t;
string s;

/*void tst(long long now)
{
    long long w=abs(c+now);
//    cout<<w<<endl;
    if (w%2==0) {ans++; return;}
    if (w%3==0) {ans++; return;}
    if (w%5==0) {ans++; return;}
    if (w%7==0) {ans++; return;}
}

void tst2(long long now)
{
    long long w=abs(c-now);
//    cout<<w<<endl;
    if (w%2==0) {ans++; return;}
    if (w%3==0) {ans++; return;}
    if (w%5==0) {ans++; return;}
    if (w%7==0) {ans++; return;}
}

void rec(int x,long long now,bool fst)
{
    if (x==s.sz) {tst(now); if (!fst) tst2(now); return;}
    rec(x+1,now*10+s[x]-'0',false);
    c+=now;
    rec(x+1,s[x]-'0',fst);
    c-=now;
    if (!fst)
    {
    c-=now;
    rec(x+1,-s[x]+'0',fst);
    c+=now;
    }
}*/

void tst(string now)
{
     long long q=0,w=0,t=1;
    for(int i=0;i<now.sz;i++)
    {
         if (now[i]=='+') {q+=w*t; t=1; w=0; continue;}
         if (now[i]=='-') {q+=w*t; t=-1; w=0; continue;}
         w*=10;
         w+=now[i]-'0';
    }
    q+=w*t;
//    cout<<q<<endl;
    w=abs(q);
    if (w%2==0) {ans++; return;}
    if (w%3==0) {ans++; return;}
    if (w%5==0) {ans++; return;}
    if (w%7==0) {ans++; return;}
//    cout<<now<<endl;
}

void rec(int x,string now)
{
    if (x==s.sz) {tst(now); return;}
    rec(x+1,now+"+"+s[x]);
    rec(x+1,now+s[x]);
    rec(x+1,now+"-"+s[x]);
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout); 
    cin>>t;
    for(int q=0;q<t;q++)
    {
        cin>>s;
        string z="";
        z+=s[0];
        ans=0;
        rec(1,z);
/*        ans=0;
        c=0;
        rec(0,0,true);*/
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
    return 0;
}
