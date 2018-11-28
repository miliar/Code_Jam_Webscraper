#include <stdio.h>
#include <cstring>
#include <iostream>
using namespace std;

int main()
{
    int test, n, S, p;
    int total[1000];
    scanf("%d",&test);
    for (int cas=1;cas<=test;cas++)
    {
        cin >> n >> S >> p;
        for (int i=0;i<n;i++) cin >> total[i];
        
        int ans = 0;
        for (int i=0;i<n;i++)
        {
            if (total[i] >= p + max(p-1,0) + max(p-1,0))
                ans++;
            else if (S > 0 && total[i] >= p + max(p-2,0) + max(p-2,0))
            {
                S--;
                ans++;
            }
        }
        printf("Case #%d: %d\n",cas, ans);
    }
}

