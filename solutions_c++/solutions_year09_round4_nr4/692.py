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

ld x[1200],y[1200],r[1200];
int n;

ld dist(int i,int j)
{
    return sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
}

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(10);
    int t;
    cin>>t;
    
        srand(12345);    
    for(int T=1;T<=t;T++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        cin>>x[i]>>y[i]>>r[i];
        ld R=10e10;
        if (n==3)
        {
            R<?=max(dist(0,1)+r[0]+r[1],r[2]*2);
            R<?=max(dist(0,2)+r[0]+r[2],r[1]*2);  
            R<?=max(dist(2,1)+r[2]+r[1],r[0]*2);
            R/=2;
        }
        if (n==2)
        {
            R<?=max(r[0],r[1]);
        }
        if (n==1)
        {
            R=r[0];
        }
        printf("Case #%d: ",T);
        cout<<R<<endl;
    }
    return 0;
}
