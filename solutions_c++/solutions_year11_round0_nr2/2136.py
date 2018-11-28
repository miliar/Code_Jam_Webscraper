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

int mm[300][300];
int mark[300][300];

int main()
{
    int T,CASE=1,now,i,j,n,m,ll;
    char cc[300];
    char res[300];
    
    freopen("B-large.in","r",stdin);
    freopen("1.out","w",stdout);
    
    scanf("%d",&T);
    while(T--)
    {
        memset(mm,0,sizeof(mm));
        memset(mark,0,sizeof(mark));
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",cc);
            mm[cc[0]][cc[1]]=cc[2];
            mm[cc[1]][cc[0]]=cc[2];
        }
        
        scanf("%d",&m);
        for(i=0;i<m;i++)
        {
            scanf("%s",cc);
            mark[cc[0]][cc[1]]=-1;
            mark[cc[1]][cc[0]]=-1;
        }
        
        scanf("%d",&ll);
        scanf("%s",cc);
        
        now=0;
        
        for(i=0;i<ll;i++)
        {
              res[now++]=cc[i];
              
              if(now<2) {continue;}
              
              if(mm[res[now-1]][res[now-2]]!=0)
              {
                  res[now-2]=mm[res[now-1]][res[now-2]];
                  now--;
              }
               
              for(j=0;j<now-1;j++)
              {
                  if(mark[res[j]][res[now-1]]==-1) {now=0;break;}
              }
              
        }
        
        
        if(now==0) printf("Case #%d: []\n",CASE++);
        else
        {
            printf("Case #%d: [",CASE++);
            for(i=0;i<now-1;i++) printf("%c, ",res[i]);
            printf("%c]\n",res[i]);
        }
                                        
    }
    return 0;
}
