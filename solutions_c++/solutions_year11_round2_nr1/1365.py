#include<iostream>
#include<cstring>
using namespace std;

int s[111][111];
double wp[111];
double wp1[111];
double wp2[111];
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    int n;
    cin>>n;
    char r;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cin>>r;
            if(r=='0')s[i][j]=0;
            else if(r=='1')s[i][j]=1;
            else if(r=='.')s[i][j]=2;
        }
    }
    for(int i=1;i<=n;i++)
    {
        int ss=0;
        int ww=0;
        for(int j=1;j<=n;j++)
        {
            if(s[i][j]==1)ww++;
            if(s[i][j]!=2)ss++;
        }
        wp[i]=double(ww)/double(ss);
    }
    for(int i=1;i<=n;i++)
    {
        int ass=0;
        double aww=0;
        for(int j=1;j<=n;j++)
        {
            if(s[i][j]==2)continue;
            ass++;
            //20ewkfpwokfwrf

        int ss=0;
        int ww=0;
        for(int jj=1;jj<=n;jj++)
        {
            if(jj==i)continue;
            if(s[j][jj]==1)ww++;
            if(s[j][jj]!=2)ss++;
        }
        aww+=double(ww)/double(ss);

            //fefeferfrwfwrf
        }
        wp1[i]=double(aww)/double(ass);
    }
    for(int i=1;i<=n;i++)
    {
        int ss=0;
        double ww=0;
        for(int j=1;j<=n;j++)
        {

            if(s[i][j]!=2)
            {
            ww+=wp1[j];
            ss++;
            }
        }
        wp2[i]=ww/double(ss);
    }
    cout<<"Case #"<<i<<":"<<endl;
    for(int i=1;i<=n;i++)
    {
        printf("%.12lf\n",(wp[i]*0.25+wp1[i]*0.5+0.25*wp2[i]));
//        cout<<(wp[i]*0.25+wp1[i]*0.5+0.25*wp2[i])<<endl;
    }
}
return 0;
}
