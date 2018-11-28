#include<cmath>
#include<cstdio>
#include<cstring>
#include<map>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;

#define minn(x,y) ((x)<(y)?(x):(y))
#define maxx(x,y) ((x)>(y)?(x):(y))

char m[100][100];
int T,R,C;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("a.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>R>>C;
        for(int i=0;i<R;i++)
        {
            scanf("%s",m[i]);
        }
        bool ch=true;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(m[i][j]=='#')
                {
                    if((i+1>=R)||(j+1>=C))
                    {
                        ch=false;
                        break;
                    }
                    else
                    {
                        if(m[i][j+1]=='#'&&m[i+1][j]=='#'&&m[i+1][j+1]=='#')
                        {
                            m[i][j]='/';
                            m[i][j+1]='\\';
                            m[i+1][j]='\\';
                            m[i+1][j+1]='/';
                        }
                        else
                        {
                            ch=false;
                            break;
                        }
                    }
                }
            }
            if(!ch)
            {
                break;
            }
        }
        printf("Case #%d:\n",ca);
        if(!ch)
        {
            printf("Impossible\n");
        }
        else
        {
            for(int i=0;i<R;i++)
            {
                printf("%s\n",m[i]);
            }
        }
    }
    return 0;
}









