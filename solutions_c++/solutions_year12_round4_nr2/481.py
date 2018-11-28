#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <time.h>

using namespace std;
const int maxn=1010;
int so[maxn],a[maxn];
bool flag[maxn];
struct node{
    int x,y;
}ans[maxn];

bool cmp(const int &u,const int &v)
{
    return a[u]>a[v];
}

bool ok()
{
    return rand()%100!=0;
}

int main()
{
    int cas;
    int N,W,L;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    srand(time(0));
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
        scanf("%d %d %d",&N,&W,&L);
        for(int i=0;i<N;i++) scanf("%d",&a[i]);
        for(int i=0;i<N;i++) so[i]=i;
        sort(so,so+N,cmp);
        int usex=0;
        while(1)
        {
        memset(flag,0,sizeof(flag));
        int idx=0;
        while(1)
        {
            while(idx<N&&flag[idx]) idx++;
            if (idx==N) break;
            int p=so[idx];
            ans[p].x=usex+a[p];
            ans[p].y=0;
            if (usex==0) ans[p].x=0;
            flag[idx]=1;
            int usey=a[p];
            int upx=ans[p].x+a[p];
            bool finds=1;
            while(finds)
            {
                finds=0;
                for(int j=idx;j<N;j++)
                 if (!flag[j]&&2*a[so[j]]+usey<=L)
                 {
                     finds=1;
                     flag[j]=1;
                     int p=so[j];
                     ans[p].x=usex+a[p];
                     if (usex==0) ans[p].x=0;
                     ans[p].y=usey+a[p];
                     int lenx=ans[p].x+a[p];
                     for(int k=j;k<N;k++)
                      if (!flag[k]&&lenx+2*a[so[k]]<=upx)
                      {
                          if (!ok()) continue;
                          int p=so[k];
                          flag[k]=1;
                          ans[p].x=lenx+a[p];
                          ans[p].y=usey+a[p];
                          lenx+=2*a[p];
                      }
                    usey+=2*a[p];
                    break;
                 }
            }
            usex=upx;
        }
            bool ansflag=1;
            for(int i=0;i<N;i++)
            if (ans[i].x>=W) ansflag=0;
            if (ansflag) break;
        }
        //for(int i=0;i<N;i++) printf("%d ",flag[i]);puts("");
        printf("Case #%d:",ii);
        for(int i=0;i<N;i++) printf(" %d %d",ans[i].x,ans[i].y);
        //for(int i=0;i<N;i++)
        // if (ans[i].x>=W) puts("bad");
        puts("");
    }
    return 0;
}



