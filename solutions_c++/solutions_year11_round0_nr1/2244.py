#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cstring>
#include<map>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;

int who[200];
int pos[200];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    
    int T,CASE=1;
    int res,n,t1,t2,now1,now2,i,temp;
    char cc[3];
    scanf("%d",&T);
    while(T--)
    {
              scanf("%d",&n);
              for(i=0;i<n;i++)
              {
                              scanf("%s%d",cc,&pos[i]);
                              if(cc[0]=='O') who[i]=0;
                              else who[i]=1;
              }
              
              res=0;
              t1=0;t2=0;now1=1;now2=1;
              while(t1!=n||t2!=n)
              {
               
                  while(t1<n&&who[t1]==1) t1++;
                  while(t2<n&&who[t2]==0) t2++;
                  
                  if(t1<t2)
                  {
                           temp=abs(pos[t1]-now1)+1;
                           now1=pos[t1];
                           res+=temp;
                           t1++;
                           if(t2==n) continue;
                           if(temp<abs(pos[t2]-now2)) { if(pos[t2]<now2) now2-=temp; else now2+=temp;}
                           else now2=pos[t2];
                           
                           
                  }
                  else
                  {
                           temp=abs(pos[t2]-now2)+1;
                           now2=pos[t2];
                           res+=temp;
                           t2++;
                           if(t1==n) continue;
                           if(temp<abs(pos[t1]-now1)) { if(pos[t1]<now1) now1-=temp; else now1+=temp;}
                           else now1=pos[t1];
                           
                           
                  }
                  
              }
              
              printf("Case #%d: %d\n",CASE++,res);         
    }
    return 0;
}
