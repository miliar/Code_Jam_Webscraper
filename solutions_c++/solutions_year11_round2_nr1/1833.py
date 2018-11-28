#include<iostream>
#include<iomanip>
#include<stdio.h>
using namespace std;
char team[102][102];
struct fac
{
    double p,q;
};
fac wp[102];
double owp[102],oowp[102];
int main()
{
   // freopen("A-large (1).in","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    // freopen("out.txt","w",stdout);
    int i,j,k,n,t;
    double cnt,cnt1;
    cin>>t;
    for(k=0; k<t; k++)
    {
        cin>>n;
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
                cin>>team[i][j];
        }
        for(i=0; i<n; i++)
        {
            cnt=0;
            cnt1=0;
            for(j=0; j<n; j++)
            {
                if(team[i][j]=='1')
                {
                    cnt++;
                    cnt1++;
                }
                else if(team[i][j]=='0')
                    cnt++;
            }
            wp[i].p=cnt1;
            wp[i].q=cnt;
        }
        for(i=0; i<n; i++)
        {
            cnt1=0;
            cnt=0;
            for(j=0; j<n; j++)
            {
                if(team[i][j]=='1')
                {
                    cnt1+=double((wp[j].p)/(wp[j].q-1));
                    cnt++;
                }
                else if(team[i][j]=='0')
                {
                    cnt1+=double((wp[j].p-1)/(wp[j].q-1));
                    cnt++;
                }
            }
            owp[i]=cnt1/cnt;
        }
        for(i=0; i<n; i++)
        {
            cnt1=0;
            cnt=0;
            for(j=0; j<n; j++)
            {
                if(team[i][j]=='0' || team[i][j]=='1')
                {
                    cnt1+=owp[j];
                    cnt++;
                }
            }
            oowp[i]=cnt1/cnt;
        }
        cout<<"Case #"<<k+1<<": "<<endl;
        for(i=0; i<n; i++)
        {
           // cout<<wp[i].p<<' '<<wp[i].q<<' '<<owp[i]<<' '<<oowp[i]<<endl;
            cout<<setiosflags(ios::fixed)<<setprecision(12)<<0.25*wp[i].p/wp[i].q+0.5*owp[i]+0.25*oowp[i]<<endl;
        }
    }
}
