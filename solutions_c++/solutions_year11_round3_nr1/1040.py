#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
#define rep(X,Y) for ( unsigned X=0; X<Y ; X++)

void run(vector <string > &v,int T)
{

    rep(i,v.size()-1)
    {
        rep(j,v[i].size())
        {
            if (j <v[i].size()-1)
            {
                if (v[i][j]=='#' && v[i][j+1]=='#'  && v[i+1][j]=='#' && v[i+1][j+1]=='#')
                {
                    v[i][j] = '/';
                    v[i][j+1] = '\\';
                    v[i+1][j] = '\\';
                    v[i+1][j+1] = '/';

                }

            }

        }

    }
    bool check=false;
    rep(i,v.size())
    {

        if (v[i].find('#') != string::npos)
        {
            check = true;
            break;
        }
    }
    cout<<"Case #"<<T+1<<": "<<endl;
    if (check)
    {

        cout<<"Impossible\n";
    }
    else
    {
        rep(i,v.size())
    {
        cout<<v[i]<<endl;
    }

    }

}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
unsigned T=0,r=0,c=0;
cin>>T;
rep(i,T)
{
    cin>>r>>c;

    vector <string > v(r);
    rep(j,r)
    {
        cin>>v[j];
    }
    run(v,i);

}
}
