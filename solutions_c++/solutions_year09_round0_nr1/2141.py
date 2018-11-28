#include<iostream>
using namespace std;
bool use[16][130];
char str[5001][16];
char s[10000];
int main()
{
    int l,d,n;
    while(scanf("%d%d%d",&l,&d,&n)==3)
    {
         while(getchar()!='\n');
         for(int i=0;i<d;i++)
         gets(str[i]);
         for(int i=1;i<=n;i++)
         {
                 memset(use,0,sizeof(use));
                 gets(s);
                 int len=strlen(s);
                 int te=0;
                 bool judge=false;
                 for(int j=0;j<len;j++)
                 {
                         if(s[j]=='(')
                         {
                                  judge=true;
                                  continue;
                         }    
                         else if(s[j]==')')
                         {
                              judge=false;
                              te++;
                              continue;
                         }
                         else
                         {
                             use[te][s[j]]=true;
                             if(!judge)
                             te++;
                         }
                 }
                 int res=0;
                 for(int j=0;j<d;j++)
                 {
                         bool judge=true;
                         for(int k=0;k<l;k++)
                         if(!use[k][str[j][k]])
                         {
                               judge=false;
                               break;
                         }
                         if(judge)
                         res++;
                 }
                 printf("Case #%d: %d\n",i,res);
         }
    }
}
                 
                         
