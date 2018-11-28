#include <stdio.h>

char map[105][105];
double wp[105];
double owp[105];
double oowp[105];

int main()
{
    freopen("A-.in","r",stdin);
    freopen("a-.out","w",stdout);
    int i,j,n,T,s,t,p,cnt,k;
    double q;
    scanf("%d",&T);
    cnt=1;
    while(T--)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%s",map[i]);    
        }   
        for (i=0;i<n;i++)
        {
            s=0;
            t=0;
            for (j=0;j<n;j++)
            {
                if (map[i][j]!='.') s++;
                if (map[i][j]=='1') t++;        
            }    
            wp[i]=t*1.0/s;
        }      
        for (i=0;i<n;i++)
        {
            q=0;
            p=0;
            for (j=0;j<n;j++)
            {
                s=t=0;
                if (map[i][j]=='.') continue;
                p++;
                for (k=0;k<n;k++)
                {
                    if (k==i) continue;
                    if (map[j][k]!='.') s++;                     
                    if (map[j][k]=='1') t++;
                } 
                q+=t*1.0/s;
            }    
            owp[i]=q/p;
        }
        for (i=0;i<n;i++)
        {
            q=0;
            p=0;
            for (j=0;j<n;j++)
            {
                if (map[i][j]=='.') continue;
                p++;
                q+=owp[j];    
            }   
            oowp[i]=q/p; 
        }
        printf("Case #%d:\n",cnt++);
        for (i=0;i<n;i++)
        {
            printf("%lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
        }
    }
    return 0;
}
