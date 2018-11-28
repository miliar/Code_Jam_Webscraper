//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int cas,kas;
    cin>>kas;
    for(cas=0;cas<kas;cas++)
    {
        int R,C,flag=0;
        string str[109];
        cin>>R>>C;
        for(int i=0;i<R;i++)cin>>str[i];

        for(int i=0;i<R-1;i++)
        {
            for(int j=0;j<C-1;j++)
            {
                if(str[i][j]=='#')
                {
                    if(str[i][j+1]!='#'||str[i+1][j+1]!='#'||str[i+1][j]!='#')
                    {
                        flag=1;
                    }
                    else{
                        str[i][j]='/';
                        str[i][j+1]='\\';
                        str[i+1][j]='\\';
                        str[i+1][j+1]='/';
                    }
                }
            }
        }

        for(int i=0;i<R;i++)if(str[i][C-1]=='#')flag=1;
        for(int i=0;i<C;i++)if(str[R-1][C])flag=1;

        printf("Case #%d:\n",cas+1);
        if(flag==1)cout<<"Impossible"<<endl;
        else for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)cout<<str[i][j];
            cout<<endl;
        }
    }
}
