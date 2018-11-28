#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
vector<int> con[10][1000];
int pr[10][1000];
int need[1200];
int t,p;

int main()
{
    freopen("B-small-attempt1 (1).in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&t);
    for(int ca =1;ca<=t;ca++)
    {
              scanf("%d",&p);
              for(int i=0;i<(1<<p);i++)
              {
                      scanf("%d",&need[i]);
                      need[i]=p-need[i];
              }
              for(int i=0;i<p;i++)
                for(int j=0;j<(1<<(p-1-i));j++)
                {
                        con[i][j].clear();
                        scanf("%d",&pr[i][j]);
                        if(i==0)
                        {
                                con[i][j].push_back(2*j);
                                con[i][j].push_back(2*j+1);
                        }
                        else 
                        {
                             for(int k=0;k<con[i-1][2*j].size();k++)
                             con[i][j].push_back(con[i-1][2*j][k]);
                             for(int k=0;k<con[i-1][2*j+1].size();k++)
                             con[i][j].push_back(con[i-1][2*j+1][k]);
                        }
                }
                int ans=0;
                int o;
              for(int i=p-1;i>=0;i--)
               for(int j=0;j<(1<<(p-i-1));j++)
               {
                       o=0;
                       for(int k=0;k<con[i][j].size();k++)
                       if(need[con[i][j][k]]>0)
                       {
                                               o=1;
                                               need[con[i][j][k]]--;
                       }
                       ans+=o;
               }
               printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
               
                                         
                               
                        
                      
              
    
    
