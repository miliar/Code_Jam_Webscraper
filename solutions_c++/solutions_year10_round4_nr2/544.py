#include<iostream>
using namespace std;


int main()
{
    int t,p,i,j,k,m,r,tr=0;
    cin>>t;
    int a[1024];
    int b[1025];
    int f[1025][11];
    while(t>0)
    {
        t--;tr++;
        cin>>p;
        for(i=0;i<(1<<p);i++)
            cin>>a[i];
        for(i=p;i>0;i--)
            for(j=0;j<(1<<(i-1));j++)
                cin>>b[(1<<(i-1))+j];
        //for(i=1;i<(1<<p);i++) cout<<b[i]<<' ';
        for(i=1<<(p-1);i<(1<<p);i++)
            for(j=0;j<p;j++)
            {
                m=min(a[(i<<1)-(1<<p)],a[(i<<1)-(1<<p)+1]);
                //cout<<i<<' '<<m<<endl;
                if(j>=p-m)
                    f[i][j]=0;
                else if(j==p-m-1)
                    f[i][j]=b[i];
                    else f[i][j]=-1;
                //cout<<i<<' '<<j<<' '<<f[i][j]<<endl;
            }
        for(i=(1<<(p-1))-1;i>0;i--)
            for(j=0,r=i;r>=1;j++,r>>=1)
            {
                if(f[i<<1][j+1]>=0 && f[(i<<1)+1][j+1]>=0)
                {
                    f[i][j]=b[i]+f[i<<1][j+1]+f[(i<<1)+1][j+1];
                    if(f[i<<1][j]>=0 && f[(i<<1)+1][j]>=0)
                        f[i][j]=min(f[i][j],f[i<<1][j]+f[(i<<1)+1][j]);
                }else
                    f[i][j]=-1;
                //cout<<i<<' '<<j<<' '<<f[i][j]<<endl;
            }
        cout<<"Case #"<<tr<<": "<<f[1][0]<<endl;
    }
    //system("pause");
}
