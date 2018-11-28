#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

#define MAXN 10000

class VINE
{
    public:
        int x;
        int len;
}arr[MAXN+5];
int n;

//int best[MAXN+5][MAXN+5];
/*
bool solve(int ind,int lasti)
{
    if (ind == n)return 1;
    if (best[ind][lasti+1]!=-1)return best[ind][lasti+1];
    int c,c2;
    bool ret=0;
    int alpha = arr[ind].len;
    if (lasti==-1)alpha=arr[ind].x;
    else alpha=min(alpha,arr[ind].x-arr[lasti].x);
    for (c=ind+1;c<=n;c++){
        if (arr[c].x>arr[ind].x+alpha)continue;
        ret|= solve(c,ind);
    }
    return best[ind][lasti+1]=ret;
    
}*/

int best[MAXN+5];

bool solve()
{
    int c,c2;
    best[0]=arr[0].x;
    for (c=1;c<=n;c++)
    {
        best[c]=-1;
        for (c2=0;c2<c;c2++){
            if (best[c2]+arr[c2].x<arr[c].x)continue;
            best[c] = max(best[c],min(arr[c].x-arr[c2].x,arr[c].len));
        }
    }
    if (best[n]==-1)return 0;
    return 1;
}

int main()
{
    FILE *in=fopen("swing.in","r");
    freopen("swing.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d",&tests);
    for (int test=1;test<=tests;test++)
    {
        fscanf(in,"%d",&n);
        for (c=0;c<n;c++)
            fscanf(in,"%d%d",&arr[c].x,&arr[c].len);
        fscanf(in,"%d",&arr[n].x);
        arr[n].len = 1000000000;
        bool can = 1;
//        memset(best,-1,sizeof(best));
//        bool ret = solve(0,-1);
        bool ret = solve();
        printf("Case #%d: ",test);
        if (!ret)printf("NO\n");
        else printf("YES\n");
    }
    
    
    
//    system("pause");
    return 0;
}
