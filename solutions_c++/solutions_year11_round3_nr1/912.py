#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output","w",stdout);
    int T,TT=0;
    cin>>T;
    while(T--)
    {
        TT++;
        cout<<"Case #"<<TT<<":\n";

        int r,c,i,j;

        string s[51];

        cin>>r>>c;

        for(i=0;i<r;i++)
        {
            cin>>s[i];
        }

        int flag = 1;

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(s[i][j]=='#')
                {
                    if(s[i][j+1]=='#' && s[i+1][j]=='#' && s[i+1][j+1]=='#')
                    {
                        s[i][j]='/';
                        s[i][j+1]='\\';
                        s[i+1][j]='\\';
                        s[i+1][j+1]='/';

                    }
                    else
                    {
                        flag = 0;
                        break;
                    }
                }
            }
            if(!flag)
            break;
        }
        if(!flag)
        cout<<"Impossible\n";
        else
        {
            for(i=0;i<r;i++)
            cout<<s[i]<<endl;
        }
    }
    return 0;
}
