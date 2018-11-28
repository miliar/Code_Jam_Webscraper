#include <stdio.h>
#include <stdlib.h>
int t,n,c,d,len;
char comb[101][101];
bool oppose[101][101];
char A[101];
char ans[101];
int at;
char tmp;
char i1,i2,i3;
inline void init()
{
 for(int i='A';i<='Z';i++)
 {
  for(int j='A';j<='Z';j++)
  {
   oppose[i-'A'][j-'A']=false;
   comb[i-'A'][j-'A']=0;
  }
 }
}
main()
{
 freopen("B-large.in","r",stdin);
 freopen("B-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  //scanf("%d",&n);
  scanf("%d",&c);
  //printf("c %d\n",c);
  init();
  if(c>0)
  {
   //scanf("%c",&i1);
   for(int i=1;i<=c;i++)
   {
    scanf("%c",&i1);
    scanf("%c%c%c",&i1,&i2,&i3);
    //printf("%c%c%c",i1,i2,i3);
    //system("pause");
    comb[i1-'A'][i2-'A']=i3;
    comb[i2-'A'][i1-'A']=i3;
   }
  }
   scanf("%d",&d);
   //printf("d %d\n",d);
  if(d>0)
  {
   //scanf("%c",&i1);
   for(int i=1;i<=d;i++)
   {
    scanf("%c",&i1);
    scanf("%c%c",&i1,&i2);
    oppose[i1-'A'][i2-'A']=true;
    oppose[i2-'A'][i1-'A']=true;
   }
  }
  scanf("%d",&len);
  scanf("%s",A);
  //printf(">> %s\n",A);
  at=0;
  for(int j=0;j<len;j++)
  {
   at++;
   ans[at]=A[j];
   if(at>1)
   {
    if(comb[ans[at]-'A'][ans[at-1]-'A']!=0)
    {
     tmp=comb[ans[at]-'A'][ans[at-1]-'A'];
     at--;
     ans[at]=tmp;
    }
    else
    {
     for(int k=1;k<at;k++)
     {
      if(oppose[ans[at]-'A'][ans[k]-'A']==true)
      {
       at=0;
       break;
      }
     }
    }
   }
    /* printf("Case #%d: [",i);
  for(int k=1;k<=at;k++)
  {
   if(k!=1){printf(" ");}
   printf("%c",ans[k]);
   if(k!=at){printf(",");}
  }
  printf("]\n");*/
 }
  
  printf("Case #%d: [",i);
  for(int k=1;k<=at;k++)
  {
   if(k!=1){printf(" ");}
   printf("%c",ans[k]);
   if(k!=at){printf(",");}
  }
  printf("]\n");
 }
 //system("pause");
 return 0;
}
