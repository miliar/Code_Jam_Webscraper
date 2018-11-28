#include <stdio.h>
#include <stdlib.h>
int t,n;
int cnto,cntb;
int ato,atb;
int nowo,nowb;
int po[101];
int pb[101];
char op[3];
char name[101];
int places[101];
int ans;
int times,otimes;
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  cnto=0;
  cntb=0;
  scanf("%d",&n);
  for(int j=1;j<=n;j++)
  {
   scanf("%s",op);
   scanf("%d",&places[j]);
   name[j]=op[0];
   if(name[j]=='O')
   {
   cnto++;
   po[cnto]=places[j];
   }
   else
   {
   cntb++;
   pb[cntb]=places[j];
   }
  }
  ans=0;
  ato=1;
  atb=1;
  nowo=1;
  nowb=1;
  for(int j=1;j<=n;j++)
  {
   //printf("togo %c %d\n",name[j],places[j]);
   //printf("before po %d pb %d\n",nowo,nowb);
   if(name[j]=='O')
   {
    if(places[j]>=nowo)
    {
     times=places[j]-nowo+1;
    }
    else
    {
     times=nowo-places[j]+1;
    }
    nowo=places[j];
    ato++;
    ans+=times;
    if(atb<=cntb)
    {
       if(pb[atb]>=nowb)
      {
       if(pb[atb]-nowb<=times){nowb=pb[atb];}
       else
       {
        nowb+=times;
       }
      }
      else
      {
       if(nowb-pb[atb]<=times){nowb=pb[atb];}
       else
       {
        nowb-=times;
       }
      }
    }
   }
   else
   {
        if(places[j]>=nowb)
    {
     times=places[j]-nowb+1;
    }
    else
    {
     times=nowb-places[j]+1;
    }
    nowb=places[j];
    atb++;
    ans+=times;
    if(ato<=cnto)
    {
       if(po[ato]>=nowo)
      {
       if(po[ato]-nowo<=times){nowo=po[ato];}
       else
       {
        nowo+=times;
       }
      }
      else
      {
       if(nowo-po[ato]<=times){nowo=po[ato];}
       else
       {
        nowo-=times;
       }
      }
    }
   }
  }
  printf("Case #%d: %d\n",i,ans);
 }
 return 0;
}
