#include<iostream>
#include<cstdio>

using namespace std;

struct LINE
{
   int l,r;    
};

LINE line[10];
int main()
{
   //freopen("A-large.in","r",stdin);
   //freopen("out.txt","w",stdout);
   int cs , cnt , N;
   scanf("%d",&cs);
   for(int c=1;c<=cs;c++)
   {
       scanf("%d",&N);
       for(int i=0;i<N;i++)
          scanf("%d%d",&line[i].l , &line[i].r);    
       cnt = 0;
       for(int i=0;i<N;i++)
          for(int  j=i+1;j<N;j++)
             if( (line[i].l - line[j].l) * (line[i].r - line[j].r) < 0)
                cnt++;
       
       printf("Case #%d: %d\n",c,cnt);                
   }
   return 0;
}
