#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        int n;
        cin>>n;
        int a[100][100];
        for(int i=0;i<n;i++)
        {
            string s;
            cin>>s;
            for(int j=0;j<n;j++)
            {
                if(s[j]=='.')a[i][j]=-1;
                else a[i][j]=s[j]-'0';
            }
        }
        double wp[100],owp[100],oowp[100];
        for(int i=0;i<n;i++)
        {
            int wins=0,games=0;
            for(int j=0;j<n;j++)
                if(a[i][j]!=-1)
                {
                    games++;
                    if(a[i][j]==1)
                        wins++;
                }
            wp[i]=double(wins)/double(games);
        }
        for(int i=0;i<n;i++)
        {
            double tot=0;
            int count=0;
            for(int j=0;j<n;j++)
                if(a[i][j]!=-1)
                {
                    count++;
                    double wp1=0;
                    int c=0,w=0;
                    for(int k=0;k<n;k++)
                    if(a[j][k]!=-1&&k!=i)
                    {
                        c++;
                        if(a[j][k]==1)
                            w++;
                    }
                    wp1=(double)w/(double)c;


                    tot+=wp1;

                }
            owp[i]=tot/double(count);
        }
        for(int i=0;i<n;i++)
        {
            double tot=0;
            int count=0;
            for(int j=0;j<n;j++)
                if(a[i][j]!=-1)
                {
                    count++;
                    tot+=owp[j];
                }
            oowp[i]=tot/double(count);
        }
        cout<<"Case #"<<test_case+1<<":"<<endl;
        for(int i=0;i<n;i++)
        {
            double ans=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
            printf("%.10f\n",ans);
        }
    }
    return 0;
}
