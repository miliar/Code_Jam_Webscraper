#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int T,N,sum[105],win[105];
char m[105][105];
double rpi[105];
double wp[105],owp[105],oowp[105];

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("a.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N;
        for(int i=1;i<=N;i++)
        {
            scanf("%s",m[i]);
        }
        memset(rpi,0,sizeof(rpi));
        memset(wp,0,sizeof(wp));
        memset(owp,0,sizeof(owp));
        memset(oowp,0,sizeof(oowp));
        for(int i=1;i<=N;i++)
        {
            int s=0,w=0;
            for(int j=0;j<N;j++)
            {
                if(m[i][j]!='.')
                {
                    s++;
                    if(m[i][j]=='1') w++;
                }
            }
            sum[i]=s,win[i]=w;
            wp[i]=double(w)/double(s);
        }
        for(int i=1;i<=N;i++)
        {
            int s=0;
            double f=0;
            for(int j=0;j<N;j++)
            {
                if(m[i][j]!='.')
                {
                    s++;
                    if(m[i][j]=='1')
                    {
                        f+=(double(win[j+1])/double(sum[j+1]-1));
                    }
                    else
                    {
                        f+=(double(win[j+1]-1)/double(sum[j+1]-1));
                    }
                }
            }
            owp[i]=f/double(s);
        }
        for(int i=1;i<=N;i++)
        {
            int s=0;
            double f=0;
            for(int j=0;j<N;j++)
            {
                if(m[i][j]!='.')
                {
                    s++;
                    f+=owp[j+1];
                }
            }
            oowp[i]=f/double(s);
        }
        for(int i=1;i<=N;i++)
        {
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
        }
        printf("Case #%d:\n",ca);
        for(int i=1;i<=N;i++)
        {
            printf("%.10f\n",rpi[i]);
        }
    }
    return 0;
}
