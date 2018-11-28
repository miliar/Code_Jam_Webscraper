#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<vector<char> > vv;
vector<char> v;
int main()
{
    ifstream cin ("i.in");
    ofstream cout ("o.out");
    int t, n, m, i, j, k;
    char x;
    bool z;
    cin>>t;
    for (i=0;i<t;++i)
    {
        vv.clear();
        cin>>n>>m;
        for (j=0;j<n;++j)
        {
            v.clear();
            for (k=0;k<m;++k)
            {
                cin>>x;
                v.push_back(x);
            }
            vv.push_back(v);
        }
        z=0;
        for (j=0;j<n;++j)
        {
            for (k=0;k<m;++k)
            {
                if (vv[j][k]=='#')
                {
                    if (k==(m-1) || vv[j][k+1]!='#' || j==(n-1) || vv[j+1][k]!='#' || vv[j+1][k+1]!='#')
                    {
                        z=1;
                        break;
                    }
                    else
                    {
                        vv[j][k]='/';
                        vv[j][k+1]='0';
                        vv[j+1][k]='0';
                        vv[j+1][k+1]='/';
                    }
                }
            }
            if (z)
            {
                break;
            }
        }
        cout<<"Case #"<<(i+1)<<":"<<endl;
        if (z)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            for (j=0;j<n;++j)
            {
                for (k=0;k<m;++k)
                {
                    if (vv[j][k]=='0')
                    {
                        cout<<(char)92;
                    }
                    else
                    {
                        cout<<vv[j][k];
                    }
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
