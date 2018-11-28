#include<iostream>
#include<stdio.h>
#include<cstdio>
#include<string.h>
#include<cstring>
using namespace std;

char cc[105][105];
double wp[105];
double owp[105];
double oowp[105];
int n;
int gam[105];
int win[105];
void init(){
    cin>>n;

    memset(gam,0,sizeof(gam));
    memset(win,0,sizeof(win));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%c",&cc[i][j]);
            if(cc[i][j]!='0'&&cc[i][j]!='1'&&cc[i][j]!='.')
            {j--;continue;}
            if(cc[i][j]=='0')
            gam[i]++;
            else if(cc[i][j]=='1')
            {
                gam[i]++;
                win[i]++;
            }
        }
        cc[i][n]=0;
    }
//    cout<<"*********"<<endl;
//    for(int i=0;i<n;i++)
//    cout<<cc[i]<<endl;
//    cout<<"*********"<<endl;
}
void getwp()
{
    for(int i=0;i<n;i++)
    {
        wp[i]=win[i]*1.0/gam[i];
//        cout<<wp[i]<<endl;
    }
//    cout<<"******* wp+********"<<endl;
}
void getowp()
{
    double temp;
    int num;
    for(int i=0;i<n;i++)
    {
        num=temp=0;
        for(int j=0;j<n;j++)
        {
            if(cc[i][j]!='.')
            {
                if(cc[j][i]=='1')
                temp=temp+(win[j]-1)*1.0/(gam[j]-1);
                else
                temp=temp+(win[j])*1.0/(gam[j]-1);
                num++;
            }
        }
        owp[i]=temp/num;
//        cout<<owp[i]<<endl;
    }
//    cout<<"**********owp<********"<<endl;
}
void getoowp()
{
    for(int i=0;i<n;i++)
    {
        double temp=0;
        int num=0;
        for(int j=0;j<n;j++)
        {
            if(cc[i][j]!='.')
            {
                temp+=owp[j];
                num++;
            }
        }
        oowp[i]=temp/num;
//        cout<<oowp[i]<<endl;
    }
//    cout<<"*******OOwp********"<<endl;
}
void print()
{
    for(int i=0;i<n;i++)
    {
        double ans=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
        printf("%lf\n",ans);
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        init();
        getwp();
        getowp();
        getoowp();
        printf("Case #%d:\n",i);
        print();
    }
    return 0;
}




















