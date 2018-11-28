#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("ouptut.txt","wr",stdout);
    int t;
    cin>>t;
    for(int test_case=0;test_case<t;test_case++)
    {
        int n,m;
        cin>>n>>m;
        string s[50];
        for(int i=0;i<n;i++)
        {
            cin>>s[i];
        }
        bool bad=false;
        for(int i=0;i<n&&!bad;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(s[i][j]=='#')
                {
                    if(i==n-1||j==m-1)
                    {
                        bad=true;
                        break;
                    }
                    else
                    if(s[i][j+1]=='#'&&s[i+1][j]=='#'&&s[i+1][j+1]=='#')
                    {
                        s[i][j]='/';
                        s[i][j+1]='\\';
                        s[i+1][j]='\\';
                        s[i+1][j+1]='/';
                    }
                    else
                    {
                        bad=true;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<test_case+1<<":\n";
        if(bad)
            cout<<"Impossible"<<endl;
        else
        for(int i=0;i<n;i++)
            cout<<s[i]<<endl;
    }
    return 0;
}
