#include<iostream>
#include<cstdlib>
#include<cstdio>

using namespace std;

int T;
int Pd,Pg;
int cno = 0;
bool ff;
int ak;
double ans;
int b[2010];
int e[2010];
int w[2010];
int X,S,R,N;
int tmp;
int M;
double t,tmp2;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        cin >> X >> S >> R >> t >> N;
        for(int i=1;i<=N;i++) cin >> b[i]>>e[i]>>w[i];
        for(int i=1;i<=N;i++)
            for(int j=i+1;j<=N;j++)
            {
                if(b[i]>b[j])
                {
                    tmp=b[i];b[i]=b[j];b[j]=tmp;
                    tmp=e[i];e[i]=e[j];e[j]=tmp;
                    tmp=w[i];w[i]=w[j];w[j]=tmp;
                }
            }
        M=N;
        ans = 0;
        if(b[1]>0)
        {
            M++;
            b[M]=0;
            e[M]=b[1];
            w[M]=0;
        }
        for(int i=2;i<=N;i++)
        {
            if(b[i]>e[i-1])
            {
                M++;
                b[M]=e[i-1];
                e[M]=b[i];
                w[M]=0;
            }
        }
        if(e[N]<X)
        {
            M++;
            b[M]=e[N];
            e[M]=X;
            w[M]=0;
        }
        N=M;
        for(int i=1;i<=N;i++)
            for(int j=i+1;j<=N;j++)
            {
                if(w[i]>w[j])
                {
                    tmp=b[i];b[i]=b[j];b[j]=tmp;
                    tmp=e[i];e[i]=e[j];e[j]=tmp;
                    tmp=w[i];w[i]=w[j];w[j]=tmp;
                }
            }
        //for(int i=1;i<=N;i++)
        //cout<<b[i]<<" "<<e[i]<<" "<<w[i]<<endl;
        for(int i=1;i<=N;i++)
        {
            if (t==0) ans+= 1.0 * (e[i]-b[i])/(S+w[i]);
            else
            {
                tmp2 = 1.0 * (e[i]-b[i])/(R+w[i]);
                if(t>=tmp2)
                {
                    t=t-tmp2;
                    ans+=tmp2;
                }
                else
                {

                    ans = ans + t + 1.0 * (e[i]-b[i]-(R+w[i])*t)/(S+w[i]);
                    t=0;
                }
            }
        }
        cno++;
        printf("Case #%d: %.6lf\n",cno,ans);
    }
    return 0;
}
