#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string.h>
#include <string>

#define PI 3.14159265358979
#define PB(x) push_back(x)
using namespace std;
typedef long long LL;

const int N = 5100,M = 300;

char data[N][30];
bool str[30][M];
int n,l,m;

    void inputing1()
    {
        int i,j;
        scanf("%d%d%d",&l,&n,&m);
        getchar();
        for (i=0;i<n;i++)
        {
            for (j=0;j<l;j++)
            {
                char ch;
                ch = getchar();
                data[i][j] = ch;
            }
            getchar();
        }
    }

    void inputing2()
    {
        int i;
        char ch;
        for (i=0;i<l;i++)
        {
            memset(str[i],0,sizeof(str[i]));
            ch = getchar();
            if (ch!='(' )
            {
                str[i][(int) ch ] = 1;
//                printf("at pos %d  ch = %c ok\n",i,ch);//debug
                continue ;
            }
            while (1)
            {
                ch = getchar();
                if (ch == ')') break;
                str[i][(int) ch ] = 1;
//                printf("at pos %d  ch = %c ok\n",i,ch);//debug
            }
        }
        getchar();
    }

    void work()
    {
        int i,j;
        int ans = 0;
        for (i=0;i<n;i++)
        {
            for (j=0;j<l;j++)
            if (!str[j][ (int)data[i][j] ])
            break;
            if (j == l)
            {
                ans ++;
//                printf("%d  : data = %s is ok\n",i,data[i]);//debug
            }
        }
        printf("%d\n",ans);
    }


int main()
{
//    freopen("inputing","r",stdin);
//    freopen("outputing","w",stdout);
    inputing1();
    for (int i = 1;i<=m;i++)
    {
        inputing2();
        printf("Case #%d: ",i);
        work();
    }

    return 0;
}


