#include<iostream>
using namespace std;

int main()
{
    int t, r, c;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>r>>c;
        char a[50][50];
        for(int j=0;j<r;j++)
        {
            for(int k = 0; k < c; k++)
            {
                cin>>a[j][k];
            }
        }
        bool done = false;
        for(int j=0;j<r-1;j++)
        {
            for(int k = 0; k < c-1; k++)
            {
                if(a[j][k]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#'&&a[j][k+1]=='#')
                {
                    a[j][k]='/';
                    a[j+1][k]='\\';
                    a[j+1][k+1]='/';
                    a[j][k+1]='\\';
                    done = true;
                }
            }
        }
        for(int j=0;j<r;j++)
        {
            for(int k=0;k<c;k++)
            {
                if(a[j][k]=='#')
                    done = false;
            }
        }
        if (r==1&&c==1) if(a[0][0]=='#') done = false; else done = true;
        cout<<"Case #"<<i+1<<": \n";
        if(!done)
        {
            cout<<"Impossible\n";
        }
        else
        {
            for(int j=0;j<r;j++)
            {
                for(int k = 0; k < c; k++)
                {
                    cout<<a[j][k];
                }
                cout<<'\n';
            }
        }
    }
    return 0;
}
