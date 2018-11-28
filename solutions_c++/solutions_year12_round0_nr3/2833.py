/*
ID:   cs_diab1
TASK: 
LANG: C++
*/

#include<algorithm>
#include<iostream>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<sstream>
#include<vector>
#include<cstdio>
#include<string>
#include<cmath>
#include<queue>
#include<set>

#define stop exit(0)
#define nc -1
#define eps 1e-10
#define inf 1000000000
#define mp make_pair

#define fill(array,value) memset(array,value,sizeof(array))
#define f(i,beg,end) for(int i=beg; i<=end; i++)
#define F(i,beg,end) for(int i=beg; i>=end; i--)
#define Max(a,b) ( (a>b)?a:b )
#define Min(a,b) ( (a<b)?a:b )
#define pi 3.1415926535897932384626433832
#define iread(var) scanf("%d",&var)
#define dread(var) scanf("%f",&var)
#define lread(var) scanf("%lld",&var)
#define input(name) freopen(name,"r",stdin)
#define output(name) freopen(name,"w",stdout)
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;

using namespace std;

int p[7]={1,10,100,1000,10000,100000,1000000};
set < pair <int,int> > s;

inline int solve(int a, int b)
{
    int sol=0;  s.clear();
    
    int m, n, cnt=(int)(1+log10(a));
    f(i,a,b)
    {
        int n=i;
        f(j,1,cnt-1)
        {
            m=(n%p[cnt-j])*p[j]+n/p[cnt-j];
            if (m>n && m<=b) 
            {
                s.insert(mp(n,m));
            }
        }
    }
    return s.size();
}

void init()
{
    int t, a, b; iread(t);
    
    f(i,1,t)
    {
        cin>>a>>b;
        cout<<"Case #"<<i<<": "<<solve(a,b)<<endl;
    }
}

int main()
{
    //redirect();
    //input("test.txt");
    input("c.in");
    output("sol.txt");
    init();

    return 0;
}