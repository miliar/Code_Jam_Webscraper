#include<iostream>
#include<cstdlib>
#include<cstring>

using namespace std;

const int xx = 500;
      
int a[xx][xx], s[xx][xx], x[xx][xx], y[xx][xx];
        
int get_min(int p, int q)
{
    if (p<q)
        return p;
    return q;
}

bool same(double r1, double r2)
{
    if ((r1-r2)*(r1-r2)<0.00000001)
        return true;
    return false;
}

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int ts;
    cin>>ts;
    for (int ti=0; ti<ts; ti++)
    {
        int n,m,d;
        cin>>n>>m>>d;
        cout<<"Case #"<<ti+1<<": ";
        for (int i=0; i<=n; i++)
            for (int j=0; j<=m; j++)
            {
                s[i][j]=0;
                x[i][j]=0;
                y[i][j]=0;
            }
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++)
            {
                char cc;
                cin>>cc;
                int k=int(cc)-int('0')+d;
                a[i][j]=k;
                s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+k;
                x[i][j]=x[i-1][j]+x[i][j-1]-x[i-1][j-1]+k*i;
                y[i][j]=y[i-1][j]+y[i][j-1]-y[i-1][j-1]+k*j;
            }
        int ans=get_min(n,m);      
        while (ans>=3)
        {
            for (int i=0; i<=n-ans; i++)
            {
                if (ans==0) break;
                for (int j=0; j<=m-ans; j++)
                {
                    double x0, y0, s0;
                    int l=ans;
                    x0=x[i+l][j+l]-x[i+l][j]-x[i][j+l]+x[i][j];
                    x0=x0-(a[i+l][j+l]+a[i+l][j+1])*(i+l)-(a[i+1][j+1]+a[i+1][j+l])*(i+1);
    
                    y0=y[i+l][j+l]-y[i+l][j]-y[i][j+l]+y[i][j];
                    y0=y0-(a[i+1][j+1]+a[i+l][j+1])*(j+1)-(a[i+1][j+l]+a[i+l][j+l])*(j+l);
    
                    s0=s[i+l][j+l]-s[i+l][j]-s[i][j+l]+s[i][j];
                    s0=s0-(a[i+1][j+1]+a[i+l][j+1])-(a[i+1][j+l]+a[i+l][j+l]);

                    if (same(x0/s0,double(i)+double(ans)/2+0.5)&&same(y0/s0,double(j)+double(ans)/2+0.5))
                    {
                        cout<<ans<<endl;
                        ans=0;
                        break;
                    }
                }
            }
            ans--;
        }
        if (ans>0)
            cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}

                    
                    
                    
            
