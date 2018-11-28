#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int main()
{

    freopen("c.in","r",stdin);
    freopen("c.ans","w",stdout);

    int t;
    sf("%d",&t);
    int kase=1;
    while ( t--)
    {
        int n,l,h;
        sf("%d %d %d",&n,&l,&h);
        int fre[100];
        int i;
        for(i=0;i<n;i++)
            sf("%d",&fre[i]);
        int num=-1;
        int j;
        for(i=l;i<=h;i++)
        {
            for(j=0;j<n;j++)
                if ( (fre[j] % i == 0 || i%fre[j] == 0) == false )
                    break;
            if ( j==n)
            {
                num = i;
                break;
            }

        }
        printf("Case #%d: ",kase++);
        if ( num == -1)
            pf("NO\n");
        else
            pf("%d\n",num);
    }
    return 0;
}
