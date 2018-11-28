#include<iostream>
#include<cstring>
#include<cstdlib>
//#include<cmath>
using namespace std;

int x[111];

int k[44][1011][4];
int kk[44][1011][4];
void ddd()
{
    memset(k,0,sizeof(k));
    for(int i=0;i<=10;i++)
    {
     for(int j=i;j<=10;j++)
    {
       for(int g=j;g<=10;g++)
    {
        if(abs(i-j)>2||abs(j-g)>2||abs(i-g)>2)continue;
        if(abs(i-j)==2||abs(j-g)==2||abs(i-g)==2)
        {
            kk[i+j+g][++kk[i+j+g][0][0]][1]=i;
        kk[i+j+g][kk[i+j+g][0][0]][2]=j;
        kk[i+j+g][kk[i+j+g][0][0]][3]=g;
            continue;
        }
        k[i+j+g][++k[i+j+g][0][0]][1]=i;
        k[i+j+g][k[i+j+g][0][0]][2]=j;
        k[i+j+g][k[i+j+g][0][0]][3]=g;
    }
    }
    }
}
bool m[111];
 int main()
 {
     int t;
     cin>>t;
     ddd();
     int n,s,p;
for(int i=1;i<=t;i++)
{
    cin>>n>>s>>p;
    for(int i=1;i<=n;i++)cin>>x[i];
    int an=0;
        memset(m,0,sizeof(m));
    for(int i=1;i<=n;i++)
    {
        if(k[x[i]][0][0]>0)
        {
            for(int ii=1;ii<=k[x[i]][0][0];ii++)
            {
                if(k[x[i]][ii][1]>=p||k[x[i]][ii][2]>=p||k[x[i]][ii][3]>=p)
                {
                   an++;
            m[i]=1;
            break;
                }
            }

        }
    }
    for(int i=1;i<=n&&s>0;i++)
    {
        if(m[i])continue;
        if(kk[x[i]][0][0]>0)
        {
            for(int ii=1;ii<=kk[x[i]][0][0];ii++)
            {
                if(kk[x[i]][ii][1]>=p||kk[x[i]][ii][2]>=p||kk[x[i]][ii][3]>=p)
                {
                   an++;
                   s--;
            break;
                }
            }

        }

    }
    cout<<"Case #"<<i<<": "<<an<<endl;
}
 return 0;
 }
