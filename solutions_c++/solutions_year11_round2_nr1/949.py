#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
string map[101];
int wcnt[101];
int cnt[101];
double wp[101];
double wp1[101];
double wp2[101];
int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int T;
    cin>>T;
    int n;
    for(int t=1;t<=T;t++)
    {
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>map[i];
        for(int i=0;i<n;i++)
        {
            wp[i]=0.0;
            int tcnt=0;
            int twcnt=0;
            for(int j=0;j<n;j++)
            {
                if(map[i][j]=='1')
                    twcnt++,tcnt++;
                else if(map[i][j]=='0')
                    tcnt++;
            }
            cnt[i]=tcnt;
            wcnt[i]=twcnt;
            wp[i]=(twcnt*1.0)/(tcnt);
        }
        for(int i=0;i<n;i++)
        {
            wp1[i]=0.0;
            double sum=0.0;
            for(int j=0;j<n;j++)
            {
                if(map[i][j]!='.')
                {
                    if(map[j][i]=='0')
                        sum+=(wcnt[j]*1.0)/(cnt[j]-1);
                    else
                        sum+=((wcnt[j]-1)*1.0)/(cnt[j]-1);
                }
            }
            wp1[i]=sum/cnt[i];
        }
        for(int i=0;i<n;i++)
        {
            wp2[i]=0.0;
            double sum=0.0;
            for(int j=0;j<n;j++)
            {
                if(map[i][j]!='.')
                {
                    sum+=wp1[j];
                }
            }
            wp2[i]=sum/cnt[i];
        }
    cout<<"Case #"<<t<<":"<<endl;
    for(int i=0;i<n;i++)
        cout<<0.25*wp[i]+0.5*wp1[i]+0.25*wp2[i]<<endl;
    }
    return 0;
}
