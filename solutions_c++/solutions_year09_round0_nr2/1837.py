/*
	Siyao
 	2009.08
*/
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int pa[20001];
int g[20001];
int ans[20001];
int h,w;
void build()
{
      for(int i=0;i<h;++i)
      {
            for(int j=0;j<w;++j)
            {
                    int tmp=g[i*w+j];
                    pa[i*w+j]=i*w+j;
                    if(i!=0&&g[i*w+j-w]<tmp) tmp=g[i*w+j-w],pa[i*w+j]=i*w+j-w;
                    if(j!=0&&g[i*w+j-1]<tmp) tmp=g[i*w+j-1],pa[i*w+j]=i*w+j-1;
                    if(j!=w-1&&g[i*w+j+1]<tmp) tmp=g[i*w+j+1],pa[i*w+j]=i*w+j+1;
                    if(i!=h-1&&g[i*w+j+w]<tmp) tmp=g[i*w+j+w],pa[i*w+j]=i*w+j+w;
            }
      }
}
int q[21000];
void col(int num,int tt)
{
          while(pa[num]!=num) num=pa[num];
          int r1=0,r2=0;
          q[0]=num;
          while(r1<=r2)
          {
                  int t=q[r1++];
                  ans[t]=tt;
                  int i=t/w,j=t%w;
                  if(i!=0&&pa[i*w+j-w]==t) ans[i*w+j-w]=tt,q[++r2]=t-w;
                  if(j!=0&&pa[i*w+j-1]==t) ans[i*w+j-1]=tt,q[++r2]=t-1;
                  if(j!=w-1&&pa[i*w+j+1]==t) ans[i*w+j+1]=tt,q[++r2]=t+1;
                  if(i!=h-1&&pa[i*w+j+w]==t) ans[i*w+j+w]=tt,q[++r2]=t+w;
          }

}
int main()
{
    freopen("in.txt","r",stdin);
        freopen("smallout.txt","w",stdout);
    int t,tt;
    scanf("%d",&t);
    for(int i=0;i<t;++i)
    {
            printf("Case #%d:\n",i+1);
            scanf("%d%d",&h,&w);
            for(int j=0;j<h;++j)
            {
                    for(int k=0;k<w;++k)
                    {
                        scanf("%d",&g[j*w+k]);
                    }
            }
            build();
            memset(ans,-1,sizeof(ans));
            tt=0;
            for(int j=0;j<h;++j)
            {
                    for(int k=0;k<w;++k)
                    {
                            if(ans[j*w+k]==-1) col(j*w+k,tt++);
                    }
            }
            for(int j=0;j<h;++j)
            {
                    for(int k=0;k<w;++k)
                    {
                           if(k)printf(" ");
                           printf("%c",ans[j*w+k]+'a');
                    }
                    printf("\n");
            }
    }
	return 0;
}
