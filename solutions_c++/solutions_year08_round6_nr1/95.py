#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>
#include<map>
#include<set>
#include<queue>
#include<algorithm>
using namespace std;

const int N=2000;
int bhmin,bhmax,bwmin,bwmax;
int nhmin,nhmax,nwmin,nwmax;
char ch[100];
int nw[1000],nh[1000],top,n,m;
int main()
{
    int i,j,k,ncase,w,test=1,h;
    freopen("Ain","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&ncase);
    while (test<=ncase)
    {
          scanf("%d",&n);
          top=0;
          bhmin=bhmax=bwmin=bwmax=-1;
          nwmin=nwmax=nhmin=nhmax=-1;
          for (i=0;i<n;i++)
          {
              scanf("%d%d%s",&w,&h,ch);
              if (ch[0]=='B')
              {
                 if (bwmin<0 || w<bwmin) bwmin=w;
                 if (bwmax<0 || w>bwmin) bwmax=w;
                 if (bhmin<0 || h<bhmin) bhmin=h;
                 if (bhmax<0 || h>bhmax) bhmax=h;
              }
              else
              {
                  scanf("%s",ch);
                  nw[top]=w;nh[top++]=h;
              }
          }
          for (i=0;i<top;i++)
          {
              if ((bwmin<0 || nw[i]>=bwmin) && (bwmax<0 || nw[i]<=bwmax))
              {
                  if (bhmax<0 || nh[i]>bhmax)
                  {
                     if (nhmin<0 || nh[i]<nhmin) nhmin=nh[i];
                  }
                  else
                  if (bhmin<0 || nh[i]<bhmin)
                  {
                     if (nhmax<0 || nh[i]>nhmax) nhmax=nh[i];
                  }
              }
              else
              if ((bhmin<0 || nh[i]>=bhmin) && (bhmax<0 || nh[i]<=bhmax))
              {
                  if (bwmax<0 || nw[i]>bwmax)
                  {
                     if (nwmin<0 || nw[i]<nwmin) nwmin=nw[i];
                  }
                  else
                  if (bwmin<0 || nw[i]<bwmin)
                  {
                     if (nwmax<0 || nw[i]>nwmax) nwmax=nw[i];
                  }
              }
          }
//          printf("nwmin=%d mwmax=%d nhmin=%d nhmax=%d\n",nwmin,nwmax,nhmin,nhmax);
          scanf("%d",&m);
          printf("Case #%d:\n",test++);
          for (i=0;i<m;i++)
          {
              scanf("%d%d",&w,&h);
              if (top==n)
              {
                  for (j=0;j<top;j++)
                  if (nw[j]==w && nh[j]==h) break;
                  if (j<top) printf("NOT BIRD\n");
                  else printf("UNKNOWN\n");
                  continue;
              }
              if (w<=bwmax && w>=bwmin && h>=bhmin && h<=bhmax)
              {
                 printf("BIRD\n");
                 continue;
              }
              if (top>0 && (nwmin>=0 && w>=nwmin) || (nwmax>=0 && w<=nwmax) || (nhmin>0 && h>=nhmin) || (nhmax>0 && h<=nhmax))
              {
                  printf("NOT BIRD\n");
                  continue;
              }
              printf("UNKNOWN\n");
          }
    }
          return 0;
}
/*
2
2
100 200 Ndsf ss
100 300 Ndsf sdfsd
*/
