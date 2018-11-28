#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int tests;
    cin>>tests;
    for(int t=1;t<=tests;t++)
    {
        int n;
        cin>>n;
        int stat[120][120];
        for(int i=0;i<120;i++) for(int j=0;j<120;j++) stat[i][j]=10;
        for(int i=1;i<=n;i++)
        {
            string h;
            cin>>h;
            for(int j=1;j<=n;j++)
            {
                if(h[j-1]=='0')
                stat[i][j]=0;
                if(h[j-1]=='1')
                stat[i][j]=1;
            }
        }

        double WP[110],OP[110],OOP[110];
        int total[110];
        memset(WP,0.0,sizeof(WP));
        memset(OP,0.0,sizeof(OP));
        memset(OOP,0.0,sizeof(OOP));

        // WP cal

        for(int i=1;i<=n;i++)
        {
            int tot=0;
            for(int j=1;j<=n;j++)
             if(stat[i][j]!=10) tot++;
             total[i]=tot;
             int win=0;
            for(int j=1;j<=n;j++)
            {
                if(stat[i][j]==1)
                win++;
            }
            WP[i]=win/double(tot);
        }

        //OP cal

        for(int i=1;i<=n;i++)
        {
            double sum=0;
            for(int j=1;j<=n;j++)
            {
                if(stat[i][j]!=10)
                {
                    int cnt=0;
                    for(int k=1;k<=n;k++)
                    {
                        if(stat[j][k]==1&&k!=i)
                        {
                            cnt++;
                        }
                    }
                    int p=total[j]-1;
                    sum+=double(cnt)/double(p);
                }
            }
            OP[i]=sum/total[i];
        }

        //OPP cal

        for(int i=1;i<=n;i++)
        {
            double sum=0;
            for(int j=1;j<=n;j++)
            {
                if(stat[i][j]!=10)
                sum+=OP[j];
            }
            OOP[i]=sum/total[i];
        }

        //RPI

        double RPI[110];
        for(int i=1;i<=n;i++)
        {
            RPI[i]=0.25*WP[i]+0.5*OP[i]+0.25*OOP[i];
        }
        cout<<"Case #"<<t<<":\n";
        for(int i=1;i<=n;i++)
        cout<<RPI[i]<<"\n";
    }
    return 0;
}
