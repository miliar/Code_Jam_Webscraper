#include <iostream>
#include <cmath>
#include <algorithm>


using namespace std;

typedef __int64  Int;
typedef struct _group
{
    Int m,p,f,s;        
}Group;
Group g[1004];

void See(int i){printf("%I64d %I64d %I64d %I64d\n", g[i].m, g[i].f, g[i].p, g[i].s);}

#define Large

Int solve()
{
    Int r, k, n;
    Int i,t,j,l,res=0LL;  
    
    scanf("%I64d %I64d %I64d", &r, &k, &n);
    for(i=0LL; i<n; ++i) scanf("%I64d", &g[i].m),g[i].p=g[i].f=0LL;
    for(i=t=0LL; i<n && t+g[i].m<=k; ++i) t+=g[i].m;
    if(i>=n) return t*r;
    
    g[0].p=i;
    g[0].s=t;
    for(j=1; j<n; ++j) 
    {
        t-=g[j-1].m;     
        while(t+g[i].m<=k) t+=g[i].m,++i,i%=n;
        g[j].p=i;g[j].s=t;         
    }
    
    //for(j=0; j<n; ++j) See(j);
     
    for(i=1,j=0; i<=r; ++i)
    {
        if( 0LL==g[j].f ) 
        {
            g[j].f=i;         
            res+=g[j].s;
            j=g[j].p;
        }   
        else break;
    }
    if(i>r) return res;
    r=r-i+1;t=g[j].s;l=g[j].p;
    while(l!=j) t+=g[l].s,l=g[l].p;
    
    res+=r/(i-g[j].f)*t;
    r%=(i-g[j].f);
    for(i=0; i<r; ++i) res+=g[j].s,j=g[j].p;
    
    return res;
}

int main()
{
    
#ifdef Large
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif
#ifdef Small
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
#endif

    int caseid, cases;
    
    scanf("%d", &cases);
    for(caseid=1; caseid<=cases; ++caseid)
        printf("Case #%d: %I64d\n", caseid, solve());

    
    return 0;    
}


