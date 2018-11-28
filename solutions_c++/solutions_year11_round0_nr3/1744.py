#include <cstdio>
#include <algorithm>

#define MAX 1024

using namespace std;
int candy[MAX];
    
int xoro(int a, int b)
{
    int solution = candy[a];
    for(int i=a+1;i<=b;i++)
        solution = solution ^ candy[i];
    return solution;
}

int main()
{
    int t,n;

    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&candy[i]);
        int sol = xoro(0,n-1);
        sort(candy,candy+n);
        printf("Case #%d: ",c);
        if(sol != 0)
            puts("NO");
        else
        {
            int s;
            for(s=0;s<n-1;s++)
                if(xoro(0,s) == xoro(s+1,n-1))
                    break;
            int jum = 0;
            for(int i=s+1;i<n;i++)
                jum += candy[i];
            printf("%d\n",jum);
        }
    }
    return 0;
}
