#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char dict[10001][11];
char guess[101][27];
bool can[10001][27];
int match[101][101];
int len[101];
bool tck[27];
int t,n,m;
int ans;
int pts;
int nowp;
bool isava;
inline int match2(int a,int b,int c)
{
 int res=0;
 if(len[a]!=len[b]){return -1;}
 else
 {
  for(int i=0;i<=26;i++)
  {
   tck[i]=false;
  }
  for(int i=0;i<=25;i++)
  {
   tck[guess[c][i]-'a']=true;
   for(int j=0;j<len[a];j++)
   {
    if(dict[a][j]!=dict[b][j]&&(tck[dict[a][j]-'a']==true||tck[dict[b][j]-'a']==true)){return res;}
   }
   res++;
  }
  return res;
 }
}
inline void matching(int a)
{
 for(int i=1;i<=n;i++)
 {
  for(int j=1;j<=n;j++)
  {
   match[i][j]=match2(i,j,a);
   //printf("match %d %d : str %d : %d\n",i,j,a,match[i][j]);
  }
 }
}
main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d%d",&n,&m);
  for(int j=1;j<=n;j++)
  {
   scanf("%s",dict[j]);
   len[j]=strlen(dict[j]);
   for(int k=0;k<=25;k++)
   {
    can[j][k]=false;
   }
   for(int k=0;k<len[j];k++)
   {
    can[j][dict[j][k]-'a']=true;
   }
  }
  for(int j=1;j<=m;j++)
  {
   scanf("%s",guess[j]);
  }
  printf("Case #%d:",i);
  for(int l=1;l<=m;l++)
  {
   ans=0;
   pts=(-1);
   matching(l);
   for(int j=1;j<=n;j++)
   {
    nowp=0;
    for(int k=0;k<25;k++)
    {
     isava=false;
     for(int s=1;s<=n;s++)
     {
      if(len[s]==len[j])
      {
       if(match[s][j]>=k)
       {
        if(can[s][guess[l][k]-'a']==true)
        {
         isava=true;
         //printf("char %c avaliable in word %d\n",guess[l][k],s);
         break;
        }
       }
      }
     } 
     if(isava==true)
     {
      if(can[j][guess[l][k]-'a']==false){nowp++;}
     }
    }
    if(nowp>pts){pts=nowp;ans=j;}
   }
   printf(" %s",dict[ans]);
  }
  printf("\n");
 }
 //system("pause");
 return 0;
}
