#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;


int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T , tcase = 0;
    scanf("%d",&T);
    while(T--)
    {
        vector<int> v;
        int n , i , sum = 0, min = 1<<30;
        scanf("%d",&n);
        for(i = 0 ; i < n ; i++)
        {
            int t ;
            scanf("%d",&t);
            v.push_back(t);
            sum += t ;
            if(t < min) min = t ;
        }
        int time = 32;
        int flag = 0 ;
        while(time--)
        {
            int tt = 0 ;
            for(i = 0 ; i < n ; i++)
            {
                if(v[i]%2 == 1)
                {
                    tt++;
                }
                v[i]/=2;
            }
            if(tt%2 == 1) flag = 1;
        }
        printf("Case #%d: ",++tcase);
        if(flag) puts("NO");
        else printf("%d\n",sum-min);
    }
    return 0;
}
