#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

#define sqr(a) ((a)*(a))


int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("A-small-attempt3.out","w",stdout);
    int T,R,C;
    char P[51][51];
    bool yes;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        cin>>R>>C;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                cin>>P[i][j];
        yes=true;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(P[i][j]=='#')
                {
                    if(i+1>=R || j+1>=C)
                    {
                        yes=false;
                        break;
                    }
                    if(P[i][j]!='#' || P[i+1][j]!='#' || P[i][j+1]!='#' || P[i+1][j+1]!='#')
                    {
                        yes=false;
                        break;
                    }
                    P[i][j]  ='/';P[i][j+1]='\\';
                    P[i+1][j]='\\';P[i+1][j+1]='/';
                }
            }
            if(!yes)break;
        }
        if(yes)
        {
            cout<<"Case #"<<t<<":"<<endl;
            for(int i=0;i<R;i++)
            {
                for(int j=0;j<C;j++)
                {
                    cout<<P[i][j];
                }
                cout<<endl;
            }
        }
        else
        {
            cout<<"Case #"<<t<<":"<<endl<<"Impossible"<<endl;
        }
    }
    return 0;
}






