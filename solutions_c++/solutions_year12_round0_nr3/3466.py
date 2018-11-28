#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;
bool vis [2000010];
int nextnum (int x)
{   int div =10;
    int dig=1;
    int temp =x;
    while (temp)
    {   temp/=10;
        dig*=10;
    }
    temp =x;
    while (temp%10 == 0)
    {   temp/=10;
        div*=10;
        dig/=10;;
    }
    dig/=10;
    temp =x;
    int a = temp%div;
    int b = temp/div;
    return (a*dig + b);
}

int main ()
{
    //freopen ("input.txt", "r", stdin);
    //freopen ("output.txt", "w", stdout);

    int T;
    scanf ("%d",&T);
    for (int f=0;f<T;f++)
    {   int a,b,res=0;
        scanf ("%d %d",&a,&b);
        memset(vis,false, sizeof(vis));
        int cnt=0;
        for (int i=a;i<=b;i++)
        {   cnt=0;
            if (!vis[i])
            {   int temp=i;
                vis[i]=1;
                while (1)
                {   int nxt = nextnum(temp);
                    vis[nxt]=1;
                    if (nxt == i)
                        break;
                    //printf ("%d\n",nxt);
                    temp = nxt;
                    if (nxt<=b && nxt>=a)cnt++;
                }
                res+= ((cnt * (cnt+1))/2);
            }
        }
        printf ("Case #%d: ",f+1);
        printf ("%d\n",res);
    }
return 0;
}
