#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
    int I,T,n,m,i,j;
    bool f;
    cin>>T;
    vector<vector<char> > a;
    for(I=1;I<=T;I++)
    {
        cin>>n>>m;
        a.resize(n);
        for(i=0;i<n;i++)
        {
            a[i].resize(m);
            for(j=0;j<m;j++)
                cin>>a[i][j];
        }
        for(i=0;i<n-1;i++)
        {
            for(j=0;j<m-1;j++)
            {
                if(a[i][j]=='#'&&a[i+1][j]=='#'&&a[i][j+1]=='#'&&a[i+1][j+1]=='#')
                {
                    a[i][j]='/';
                    a[i+1][j]='\\';
                    a[i][j+1]='\\';
                    a[i+1][j+1]='/';
                }
            }
        }
        f=true;
        for(i=0;i<n&&f;i++)
        {
            for(j=0;j<m&&f;j++)
                if(a[i][j]=='#')f=false;
        }
        cout<<"Case #"<<I<<": "<<endl;
        if(!f)
        {
            cout<<"Impossible"<<endl;
            continue;
        }
        for(i=0;i<n&&f;i++)
        {
            for(j=0;j<m&&f;j++)
                cout<<a[i][j];
            cout<<endl;
        }
    }
}
