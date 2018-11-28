#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

int n,q;
int arr[105];
int best[105][105];
int solve(int s,int e)
{
    if (arr[s]+1>arr[e]-1)return 0;
    if (best[s][e]!=-1)return best[s][e];
    int ret=1<<30;
    int c,c2;
    bool f=0;
    for (c=s+1;c<e;c++)
    {
        f=1;
        int m=arr[e]-arr[s]-2;
        ret=min(ret,m+solve(s,c)+solve(c,e));
    }
    return best[s][e]=f*ret;
}

int main()
{
    FILE *in=fopen("prs.in","r");
    freopen("prs.out","w",stdout);
    int c,c2;
    int tests;
    fscanf(in,"%d",&tests);
    for (int test=1;test<=tests;test++)
    {
        printf("Case #%d: ",test);
        fscanf(in,"%d%d",&n,&q);
        for (c=0;c<q;c++)
        fscanf(in,"%d",&arr[c]);
        q+=2;
        arr[q-1]=0;
        arr[q-2]=n+1;
        sort(arr,arr+q);
        memset(best,-1,sizeof(best));
        int ret=solve(0,q-1);
        printf("%d\n",ret);
    }
//    system("pause");
    return 0;
}
