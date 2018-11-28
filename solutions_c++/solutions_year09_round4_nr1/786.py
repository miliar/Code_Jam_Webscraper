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

int n,z[50];
char a[50][50];

int main()
{
    freopen("q.in", "rt", stdin);
    freopen("q.out", "wt", stdout);
    cout.flags(ios::fixed);
    cout.precision(2);
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        {
            scanf("%c",&a[i][0]);
            z[i]=0;
            for(int j=0;j<n;j++)
            {
                scanf("%c",&a[i][j]);
                if (a[i][j]=='1') z[i]=j+1;
            }
        }
        int ans=0;
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n;j++)
            if (z[j]<=i+1)
            {
                while(j-1>=i)
                {
                    swap(z[j],z[j-1]);
                    j--;
                    ans++;
                }
                break;
            }
        }
//        for(int i=0;i<n;i++)
//        cout<<z[i]<<endl;
        printf("Case #%d: ",T);
        cout<<ans<<endl;
    }
    return 0;
}
