#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<cmath>
#include<iostream>
#define out(x) cout<<#x<<": "<<(x)<<endl;
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    int t,i,j,k,n,m,res,mark,cnt,T=1;
    char a[200][200],b[200][200];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        
        for(i=0;i<n;i++) scanf("%s",a[i]);
        for(i=0;i<m;i++) scanf("%s",b[i]);
        
        for(i=0;i<n;i++) 
        {
            for(j=0;a[i][j];j++) ;
            a[i][j]=47;
            a[i][j+1]=0;
        }
        for(i=0;i<m;i++) 
        {
            for(j=0;b[i][j];j++) ;
            b[i][j]=47;
            b[i][j+1]=0;
        }
        
        int ans=0;
        
        for(i=0;i<m;i++)
        {
            res=1;
            mark=n;
            for(j=0;j<n;j++)
            {
                for(k=0;b[i][k]&&a[j][k];k++)
                {
                    if(b[i][k]!=a[j][k]) break;
                }
                if(k>res) {res=k;mark=j;}
            }
            
            for(j=res;b[i][j];j++)
            {
                if(b[i][j]==47) ans++;
            }
            
            for(j=0;b[i][j];j++)
            {
                a[n][j]=b[i][j];
            }
            a[n][j]=0;
            n++;
            //out(ans);
        }
        
        printf("Case #%d: %d\n",T++,ans);
    }
    return 0;
}
