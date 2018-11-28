# include <iostream>
# include <string>
# include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int r,c,t,cas;
    string str[55];
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        int use[55][55]={0};
        cin>>r>>c;
        for(int i=0;i<r;i++) cin>>str[i];
        for(int i=0;i<r-1;i++)
        {
            for(int j=0;j<str[i].size()-1;j++)
            {
                if(str[i][j] == '#' && str[i+1][j] == '#' && str[i][j+1] == '#' && str[i+1][j+1] == '#')
                {
                    str[i][j] ='/';str[i][j+1] ='\\';
                    str[i+1][j] ='\\';str[i+1][j+1] ='/';
                }
            }
        }

        bool flag = true;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<str[i].size();j++)
            {
                if(str[i][j] == '#')
                    flag = false;
            }
        }


        printf("Case #%d:\n",cas);
        if(flag == false)
            printf("Impossible\n");
        else
        {
            for(int i=0;i<r;i++)
                cout<<str[i]<<endl;
        }
    }
    return 0;
}
