#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct _Chick
{
    int x,v,t,c;        
}chicken;

bool cmp1(chicken a, chicken b)
{
    return a.t<b.t;     
}

bool cmp2(chicken a, chicken b)
{
    return a.c<b.c;     
}

int solve()
{
    int res=0;
    int i,j;
    int n,k,b,t;
    chicken ch[90];
    vector<chicken> vec;
    chicken chick;
    cin >> n >> k >> b >> t;
    for(i=0; i<n; ++i) cin >> ch[i].x;
    for(i=0; i<n; ++i) cin >> ch[i].v;
    for(i=0; i<n; ++i)
        ch[i].t=(b-ch[i].x+ch[i].v-1)/ch[i].v;         
    sort(&ch[0], &ch[n], cmp1);
    
    for(i=0; i<n; ++i) if(ch[i].t>t) break;
    if(i>=n) return 0;
    else if(i<k) return -1;
    t=i;
    for(; i<n; ++i) ch[i].c=b;
    for(i=0; i<t; ++i)
    {
        b=0;
        for(j=t; j<n; ++j)
        {
            if (ch[i].x<ch[j].x) ++b;        
        }         
        ch[i].c=b;
    }     
    sort(&ch[0], &ch[n], cmp2);
    
    for(i=0; i<k; ++i) res+=ch[i].c;
    
    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cnum,res; 
    cin >> cnum;
    
    for(int cid=1; cid<=cnum; ++cid)
    {
        res=solve();
        cout << "Case #" << cid << ": " ;
        if(-1==res) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
       
    return 0;    
}
