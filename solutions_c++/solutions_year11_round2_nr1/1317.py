#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<iomanip>
using namespace std;
double wp[105],owp[105],oowp[105],rpi[105];
int main()
{
    int t,n,score[105][105];
    char get;
    cin>>t;
    for(int count=1;count<=t;count++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                cin>>get;
                if(get=='0')
                    score[i][j]=0;
                else if(get=='1')
                    score[i][j]=1;
                else
                    score[i][j]=-1;
            }
        }
        for(int i=0;i<n;i++)
        {
            double all=0;
            int co=0;
            for(int j=0;j<n;j++)
            {
                if(score[i][j]==1||score[i][j]==0)
                {
                    co++;
                    all+=score[i][j];
                }
            }
            wp[i]=all/(double)co;
        }
        for(int k=0;k<n;k++)
        {
            int c=0;
            double al=0;
            for(int i=0;i<n;i++)
            {
                if(i==k||score[k][i]==-1)   {continue;}
                c++;
                double all=0;
                int co=0;
                for(int j=0;j<n;j++)
                {
                    if((score[i][j]==1||score[i][j]==0)&&j!=k)
                    {
                        co++;
                        all+=score[i][j];
                    }
                }
                al+=all/(double)co;
            }
            owp[k]=al/(double)c;
        }
        for(int i=0;i<n;i++)
        {
            double all=0;
            int co=0;
            for(int j=0;j<n;j++)
            {
                if(score[i][j]!=-1)
                {
                    co++;
                    all+=owp[j];
                }
            }
            oowp[i]=all/(double)co;
        }
        for(int i=0;i<n;i++)
            rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
        cout<<"Case #"<<count<<": "<<endl;
        for(int i=0;i<n;i++)
            cout<<fixed<<setprecision(8)<<rpi[i]<<endl;
    }
    return 0;
}
