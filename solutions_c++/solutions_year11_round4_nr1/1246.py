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

struct node
{
       int ww;
       int bb;
       int ee;
};

node yy[2000];

const double eps=1e-9;

int compare(node left,node right)
{
    return left.ww<right.ww;
}

int main()
{
    int T=1,CASE;
    int i,xx,ss,rr,tt,n;
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&CASE);
    while(CASE--)
    {
        scanf("%d%d%d%d%d",&xx,&ss,&rr,&tt,&n);
        int hh=0;
        for(i=0;i<n;i++) 
        {
            scanf("%d%d%d",&yy[i].bb,&yy[i].ee,&yy[i].ww);
            hh+=yy[i].ee-yy[i].bb;
        }
        
        hh=xx-hh;
        
        yy[n].bb=0;
        yy[n].ee=hh;
        yy[n].ww=0;
        n++;
        
        sort(yy,yy+n,compare);
        
        double now=tt*(rr-ss);
        double res=0;
        double sum=0;
     
        int mark=0;
        
        for(i=0;i<n;i++)
        {
            
            //out(res);
            double temp1=yy[i].ee-yy[i].bb;
            double temp2=temp1/(yy[i].ww+ss);
            double temp3=temp1/(yy[i].ww+rr);
            double temp4=(temp2-temp3)*(yy[i].ww+ss);
            
            sum+=temp2;
            if(mark) continue;
            
            if(now>temp4-eps)
            {
                res+=temp2-temp3;
                now-=temp4;
            }
            else
            {
                res+=now/(yy[i].ww+ss);
                mark=1;
            }
        }
      
        //out(res);
        printf("Case #%d: %.9lf\n",T++,sum-res);
    }
    return 0;
}
    
                
