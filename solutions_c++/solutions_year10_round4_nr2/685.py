#include<iostream>
#define MAX 100000000
#include<cmath>
#include "BigInt.h"
#include<string>
using namespace std;

FILE *in,*out;
int t,tt;

long long  p,pp,m[2000],cost[20][2000][20],price[20][2000],i,j,k,l,power[20],ans;

int pow(int a,int b)
{
    int tmp=0,ii;
    tmp=1;
    for (ii=1;ii<=b;ii++)
        tmp*=a;
    return tmp;
}


int max(int a,int b)
{
    return a>b?a:b;
}

int min(int a,int b)
{
    return a<b?a:b;
}


int main()
{
    in=freopen("B-large.in","r",stdin);
    out=freopen("B-large.out","w",stdout);
    
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>p;
        memset(power,0,sizeof(power));
        memset(price,0,sizeof(price));
        memset(m,0,sizeof(m));
        for (i=0;i<=p;i++)
            power[i]=pow(2,i);
        pp=power[p];
        for (i=0;i<pp;i++)  
        {
            cin>>m[i];
            //cout<<m[i]<<" ";
            m[i]=p-m[i];
            //cout<<m[i]<<endl;
        }
        for (i=0;i<p;i++)
            for (j=0;j<power[p-i-1];j++)
                cin>>price[i][j];
        memset(cost,0,sizeof(cost));
        
        /*for (i=0;i<pp;i++)
            cout<<m[i]<<"   ";
        cout<<endl<<endl;*/
        
        i=0;
        for (j=0;j<power[p-i-1];j++)
        {
            k=max(m[2*j],m[2*j+1]);
            if (k>0)
                cost[i][j][k-1]=price[i][j];
            for (l=0;l<k-1;l++)
                cost[i][j][l]=MAX;
        }    
        /*for (j=0;j<power[p-i-1];j++)
        {
            for (k=0;k<pp-1;k++)
                cout<<cost[i][j][k]<<" ";
            cout<<endl;
        }
        cout<<endl<<endl;
            */
            
            
            
            
        for (i=1;i<p;i++)
        {
            for (j=0;j<power[p-i]-1;j++)
            //{
                for (k=0;k<pp-1;k++)
                    //cost[i][j][k]=min(min(cost[i-1][2*j][k],cost[i-1][2*j+1][k]),min(cost[i-1][2*j][k+1],cost[i-1][2*j+1][k+1])+price[i][j]);
                    cost[i][j][k]=min(cost[i-1][2*j][k]+cost[i-1][2*j+1][k],cost[i-1][2*j][k+1]+cost[i-1][2*j+1][k+1]+price[i][j]);
            /*for (j=0;j<power[p-i]-1;j++)
            {
                for (k=0;k<pp-1;k++)
                    cout<<cost[i][j][k]<<" ";
                cout<<endl;
            }
            cout<<endl<<endl;*/
        }
                
        ans=cost[p-1][0][0];
        /*for (k=1;k<p;k++)
            if (cost[p][0][k]<ans)
                ans=cost[p][0][k];*/
        cout<<"Case #"<<tt<<": "<<ans<<endl;       
    }
    fclose(in);
    fclose(out);
    return 0;
}
