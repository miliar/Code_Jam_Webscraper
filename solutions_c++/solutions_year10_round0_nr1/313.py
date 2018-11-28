#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A.in","r",stdin); freopen("A.out","w",stdout);
    int t; scanf("%d",&t);
    for (int casenum = 1; casenum <= t; ++casenum){
        int n,k;
        scanf("%d %d",&n,&k);
        int state = 1 << n; state--;
        bool ok = false;
        if (k >= state){
            if ((k ^ state) == (k - state)) ok = true;
        }
        if (!ok) printf("Case #%d: OFF\n",casenum);
            else printf("Case #%d: ON\n",casenum);
    }
    return 0;
}
