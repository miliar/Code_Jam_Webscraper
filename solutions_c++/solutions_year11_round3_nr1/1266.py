#include <iostream>
using namespace std;
int main()
{
    int i,j,k,t,r,c,s;
    char a[51][51];
    cin>>t;
    for (k=1;k<=t;k++)
    {
        cin>>r>>c;
        s=0;
        for (i=1;i<=r;i++)
        {
            for (j=1;j<=c;j++)
            {
                cin>>a[i][j];
                if (i>=2&&j>=2) if (a[i][j]=='#')
                {
                    if (a[i-1][j-1]=='#'&&a[i][j-1]=='#'&&a[i-1][j]=='#')
                    {
                        a[i-1][j-1]='/';
                        a[i][j-1]='\\';
                        a[i-1][j]='\\';
                        a[i][j]='/';
                    }
                }
            }
        }
        cout<<"Case #"<<k<<":"<<endl;
        for (i=1;i<=r;i++)
        {
            for (j=1;j<=c;j++)
            {
                if (a[i][j]=='#') {cout<<"Impossible"<<endl;s=1;break;}
            }
            if (s) break;
        }
        if (!s)
        {
            for (i=1;i<=r;i++)
            {
                for (j=1;j<=c;j++) cout<<a[i][j];
                cout<<endl;
            }
        }
    }
}
                
            
        
