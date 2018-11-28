#include<iostream>
#include<string>
#include<set>
using namespace std;
set<char>st[15];
char ss[5000][16];
char s[1000];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.txt","w",stdout);
    int l,d,n;scanf("%d%d%d",&l,&d,&n);
    int i,j;  
    for(i=0;i<d;i++)
    scanf("%s",ss[i]);       
    for(int c=0;c<n;c++)
    {
         scanf("%s",s);int ind=0;
         bool in=0;
         for(i=0;i<l;i++)st[i].clear();
         for(i=0;s[i];i++)
         {
              if(s[i]=='(')
              {
                   in=1;            
              } 
              else if(s[i]==')')
              {
                   in=0; 
                   ind++;   
              }
              else 
              {
                  if(in)st[ind].insert(s[i]);
                  else 
                  {
                      st[ind].insert(s[i]);  
                      ind++;  
                  }     
              }            
         }
         /*for(i=0;i<l;i++){
         for(set<char>::iterator it=st[i].begin();it!=st[i].end();it++)
         printf("%c ",*it);
         printf("\n");                 
         }       printf("*****\n");*/
         int sum=0;
         for(i=0;i<d;i++)
         {
              bool is=1;
              for(j=0;j<l;j++)
              if(st[j].find(ss[i][j])==st[j].end())
              {is=0;break;}
              if(is)sum++;                
         }
         printf("Case #%d: %d\n",c+1,sum);
    }
}
