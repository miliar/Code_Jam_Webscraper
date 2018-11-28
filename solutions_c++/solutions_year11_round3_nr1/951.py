#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>

#define maxn 10000
#define size 100
#define inf 1<<30
using namespace std;

char map[size][size];

int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("2.txt","w",stdout);
    int t,c,r;
    scanf("%d",&t);
    for(int k = 1;k <= t;++k)
    {
        scanf("%d%d",&r,&c);
        for(int i = 0;i < r;++i)
            scanf("%s",map[i]);
        int cnt = 0;
        bool flag = true;
        for(int i = 0;i < r;++i)
        {
            for(int j = 0;j < c;++j)
                if(map[i][j] == '#')
                    cnt++;
        }

        if(cnt%4)
            flag = false;
        if(!flag)
        {
            printf("Case #%d:\nImpossible\n",k);
            continue;
        }
        for(int i = 0;i < r;++i)
        {
            if(!flag)
                break;
            for(int j = 0;j < c;++j)
                if(map[i][j] == '#')
                {
                    if(j + 1 >= c || i+1 >= r)
                    {
                        flag = false;
                        break;
                    }
                    if(map[i][j+1] == '#'
                       && map[i+1][j] == '#'
                       && map[i+1][j+1] == '#')
                       {
                           map[i][j] = '/';
                           map[i][j+1] = '\\';
                           map[i+1][j] = '\\';
                           map[i+1][j+1] = '/';
                       }
                    else
                        flag = false;
                }
        }
        if(!flag)
        {
            printf("Case #%d:\nImpossible\n",k);
            continue;
        }
        else
        {
            printf("Case #%d:\n",k);
            for(int i = 0;i < r;++i)
            {
                printf("%s\n",map[i]);
            }
        }
    }
    return 0;
}
