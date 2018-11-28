#pragma comment(linker, "/STACK:16777216")
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
#define ll long long
#define istr istringstream

int t,u[12];
string s;

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    cin>>t;
        getline(cin,s);    
    for(int T=1;T<=t;T++)
    {
        getline(cin,s);
        int q;
        bool yes=false;
        clr(u);
        for(int i=s.sz-1;i>=0;i--)
        {
            u[s[i]-'0']++;
            for(int j=s[i]-'0'+1;j<10;j++)
            if (u[j])
            {
                u[j]--;
                q=i+1;
                yes=true;
                s[i]=(char)j+'0';
                break;
            }
            if (yes) break;
        }
        if (yes)
        {
            for(int i=q;i<s.sz;i++)
            {
                for(int j=0;j<10;j++)
                if (u[j])
                {
                    u[j]--;
                    s[i]=(char)j+'0';
                    break;
                }
            }
        }
        else
        {
            s+="0";
            sort(s.begin(),s.end());
            string ss="";
            for(int i=0;i<s.sz;i++)
            if (s[i]>'0')
            {
                ss+=s[i];
                s[i]=0;
                break;
            }
            for(int i=0;i<s.sz;i++)
            if (s[i]>0)
            {
                ss+=s[i];
            }            
            s=ss;
        }
        printf("Case #%d: ",T);
        cout<<s<<endl;
    }
    return 0;
}
