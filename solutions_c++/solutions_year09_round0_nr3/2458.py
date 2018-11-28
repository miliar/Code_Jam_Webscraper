
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char str[501];
char ans[18][18];
void add(char *a,char *b)
{
    int r=0;
    for(int i=3;i>=0;i--)
    {
      int sum=a[i]-'0'+b[i]-'0'+r;
      a[i]=sum%10+'0';
      r=sum/10;
    }
}
int main( )
{
 int n;
 //freopen("in","r",stdin);
 freopen("out","w",stdout);
 scanf("%d",&n);
 getchar( );
 for(int t=0;t<n;t++)
 {

 gets(str);
 for(int i=0;i<=18;i++)
 {
     ans[i][0]=ans[i][1]=ans[i][2]=ans[i][3]='0';
     ans[i][4]='\0';
 }
 for(int i=0;str[i]!='\0';i++)
 {
   if(str[i]=='w')
    { add(ans[0],"0001");

    }
   else if(str[i]=='e')
   {
        add(ans[1],ans[0]);
        add(ans[6],ans[5]);
        add(ans[14],ans[13]);
   }
   else if(str[i]=='l')
   {
       add(ans[2],ans[1]);
   }
   else if(str[i]=='c')
   {
       add(ans[3],ans[2]);
       add(ans[11],ans[10]);
   }
   else if(str[i]=='o')
   {
       add(ans[4],ans[3]);
       add(ans[9],ans[8]);
       add(ans[12],ans[11]);
   }
   else if(str[i]=='m')
   {
       add(ans[5],ans[4]);
       add(ans[18],ans[17]);
   }
   else if(str[i]==' ')
   {
       add(ans[7],ans[6]);
       add(ans[10],ans[9]);
       add(ans[15],ans[14]);
   }
   else if(str[i]=='t')
   {
       add(ans[8],ans[7]);
   }
   else if(str[i]=='d')
   {
       add(ans[13],ans[12]);
   }
   else if(str[i]=='j')
   {
       add(ans[16],ans[15]);
   }
   else if(str[i]=='a')
   {
       add(ans[17],ans[16]);
   }
 }
 printf("Case #%d: %s\n",t+1,ans[18]);

 }
 return 0;
}
