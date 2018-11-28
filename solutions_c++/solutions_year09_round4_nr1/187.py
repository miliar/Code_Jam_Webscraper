#include <iostream>
#include <map>
#include <set>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int N = 45,INF = 1<<29;
const double eps = 1e-10;
const double pi = acos(1.);
int n,m;
char s[N][N];
//int swap[N][N];
int L[N],P[N];
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int i,j,k;
    int T,K=1;
    scanf("%d",&T);
    while(T--)
    {
    //    memset(swap,0,sizeof(swap));
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",s[i]);
            L[i]=-1;
            for(j=0;j<n;j++)
                if(s[i][j]=='1')L[i]=j;

            P[i]=L[i];
        }
        sort(P,P+n);
        for(i=0;i<n;i++)
            if(P[i]>i)break;
        printf("Case #%d: ",K++);
        if(i<n){puts("X");continue;}
        int ans = 0;
        for(i=0;i<n;i++)
        {
            if(L[i]<=i)continue;
            for(j=i+1;j<n;j++)
                if(L[j]<=i)break;
            int tmp = L[j];
            for(k=j;k>i;k--)
                L[k]=L[k-1],ans++;
            L[i]=tmp;
        }
        printf("%d\n",ans);
    }
    return 0;
}
