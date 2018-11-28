#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,i,j,c,N,k;
    double tot,cnt,t,tt;
    string mp[110];
    double wp[110],owp[110],oowp[110];
    cin>>T;
    for (c=1;c<=T;c++)
    {
        cin>>N;
        for (i=0;i<N;i++)
            cin>>mp[i];
        for (i=0;i<N;i++)
        {
            cnt=0;
            tot=0;
            for (j=0;j<N;j++)
                if (mp[i][j]!='.')
                {
                    tot+=1;
                    if (mp[i][j]=='1')
                        cnt+=1;
                }
            wp[i]=double(cnt/tot);

            cnt=0;
            tot=0;
            for (j=0;j<N;j++)
                if (mp[i][j]!='.')
                {
                    tot+=1;
                    t=0;
                    tt=0;
                    for (k=0;k<N;k++)
                        if (mp[j][k]!='.' && k!=i)
                        {
                            if (mp[j][k]=='1')
                                t+=1;
                            tt+=1;
                        }
                    cnt+=t/tt;
                }
            owp[i]=cnt/tot;
        }
        for (i=0;i<N;i++)
        {
            tot=0;
            cnt=0;
            for (j=0;j<N;j++)
                if (mp[i][j]!='.')
                {
                    tot+=1;
                    cnt+=owp[j];
                }
            oowp[i]=cnt/tot;
        }

        cout<<"Case #"<<c<<":"<<endl;
        for (i=0;i<N;i++)
            printf("%.9lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);

    }
    return 0;
}
