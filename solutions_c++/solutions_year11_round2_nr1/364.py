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

char cc[200][200];
double wp[200];
double tempwp[200];
double owp[200];
double oowp[200];

int main()
{
    int CASE,T=1;
    int n,i,j,k;
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&CASE);
    while(CASE--)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",cc[i]);
        }
        
        for(i=0;i<n;i++)
        {
            double t1,t2;
            t1=t2=0;
            for(j=0;j<n;j++)
            {
                if(cc[i][j]=='.') continue;
                
                if(cc[i][j]=='1') {t1++;t2++;}
                else t2++;
            }
            
            if(t2<1e-9) wp[i]=0;
            else wp[i]=t1/t2;
            
            //out(wp[i]);
        }
        
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                double t1,t2;
                t1=t2=0;
                for(k=0;k<n;k++)
                {
                    if(k==i) continue;
                    if(cc[j][k]=='.') continue;
                    
                    if(cc[j][k]=='1') {t1++;t2++;}
                    else t2++;
                }
                
                if(t2<1e-9) tempwp[j]=0;
                else tempwp[j]=t1/t2;
            }
            
            double t1,t2;
            t1=t2=0;
            for(j=0;j<n;j++)
            {
                if(cc[i][j]=='.') continue;
                
                t1+=tempwp[j];t2++;
            }
            
            if(t2<1e-9) owp[i]=0;
            else owp[i]=t1/t2;
            
            //out(owp[i]);
        }
        
        for(i=0;i<n;i++)
        {
            double t1,t2;
            t1=t2=0;
            for(j=0;j<n;j++)
            {
                if(cc[i][j]=='.') continue;
                
                t1+=owp[j];t2++;
            }
            
            if(t2<1e-9) oowp[i]=0;
            else oowp[i]=t1/t2;
            
            //out(oowp[i]);
        }
        
        printf("Case #%d:\n",T++);
        
        for(i=0;i<n;i++) printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }
    return 0;
}
