#include "iostream"
using namespace std;
#include "string.h"
#include "vector"

double wp[101],owp[101],oowp[101],rsi[101];
double twp[101];
int num[101],onum[101],oonum[101];
char ch[110][110];
vector<int> v[101];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    
    for(int C=1;C<=t;C++)
    {
            int n;
            scanf("%d",&n);
            int i,j;
            
            for(i=0;i<=n;i++)
            {
                wp[i]=owp[i]=oowp[i]=num[i]=onum[i]=oonum[i]=0;
                v[i].clear();
            }
            for(i=1;i<=n;i++)
            {
                cin>>ch[i];
                for(j=0;j<n;j++)
                {
                    if(ch[i][j]=='.')continue;
                    if(ch[i][j]=='1')wp[i]+=1;
                    
                    num[i]++;
                    v[i].push_back(j+1);
                }
                if(num[i]!=0)
                wp[i] = wp[i]/num[i];
            }
            for(i=1;i<=n;i++)
            {
                for(j=0;j<num[i];j++)
                {
                    twp[v[i][j]] = wp[v[i][j]]*num[v[i][j]];
                    if(ch[v[i][j]][i-1]=='1')twp[v[i][j]]-=1;
                    if(num[v[i][j]]>1)twp[v[i][j]]/=(num[v[i][j]]-1);
                    
                    owp[i]+=twp[v[i][j]];
                }
                if(num[i]!=0)
                 owp[i] = owp[i]/num[i];

            }
            for(i=1;i<=n;i++)
            {
                for(j=0;j<num[i];j++)
                {
                    oowp[i]+=owp[v[i][j]];
                }
                if(num[i]!=0)
                 oowp[i] = oowp[i]/num[i];
    
            }
            printf("Case #%d:\n",C);
            for(i=1;i<=n;i++)
            {
                             rsi[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
                             printf("%.8lf\n",rsi[i]);
            }
    }
    
    return 0;
}
