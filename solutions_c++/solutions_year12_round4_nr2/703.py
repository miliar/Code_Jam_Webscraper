#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define MAXN 10010
#define MAXT 100
using namespace std;
long long  r[MAXN];
long long  nowx[MAXN],nowy[MAXN];
int n,l,w;
inline long long  sqr(long long  x)
{
    return x*x;
}
bool dfs(int idx)
{
    if(idx==n)
    {
        for(int i=0; i<n; ++i) cout <<' ' <<   nowx[i] << ' '<<  nowy[i];
        cout << endl;
        return true;
    }
    for(int i=0; i<MAXT; ++i)
    {
        long long  x=rand()*rand()%(w+1),y=rand()*rand()%(l+1);
        int w;
        for(w=0; w<idx; w++)
            if(sqr(x-nowx[w])+sqr(y-nowy[w])<sqr(r[w]+r[idx])) break;
        if(w==idx)
        {
            nowx[idx]=x,nowy[idx]=y;
            if(dfs(idx+1)) return true;
        }
    }
    dfs(idx-1);
}
void ini()
{
    cin >> n >> w >> l ;
    for(int i=0; i<n; ++i) cin >> r[i];
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    srand(time(NULL));
    int cas;
    scanf("%d",&cas);
    int ci;
    int i;
    for(ci=1; ci<=cas; ci++)
    {
        ini();
        printf("Case #%d:",ci);
        dfs(0);
    }
    return 0;
}
