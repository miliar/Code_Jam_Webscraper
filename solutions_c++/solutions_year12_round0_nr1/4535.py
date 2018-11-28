#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int f[100];
int flag[100];
char ch[10005];
int main()
{


freopen("C:\\Users\\pyxf\\Desktop\\A-small-attempt0.in","r",stdin);
freopen("C:\\Users\\pyxf\\Desktop\\out.txt","w",stdout);
f[0]=24;
f[1]=7;
f[2]=4;
f[3]=18;
f[4]=14;
f[5]=2;
f[6]=21;
f[7]=23;
f[8]=3;
f[9]=20;
f[10]=8;
f[11]=6;
f[12]=11;
f[13]=1;
f[14]=10;
f[15]=17;
f[16]=25;
f[17]=19;
f[18]=13;
f[19]=22;
f[20]=9;
f[21]=15;
f[22]=5;
f[23]=12;
f[24]=0;
f[25]=16;
   int t;
   scanf("%d",&t);
   getchar();
   int as=1;
   while(t--)
   {
       gets(ch);
       printf("Case #%d: ",as++);
       int i;
       int l=strlen(ch);
       for(i=0;i<=l-1;i++)
       {
           if(ch[i]==' ')
           printf(" ");
           else
           printf("%c",f[ch[i]-'a']+'a');
       }
       printf("\n");
   }
}
