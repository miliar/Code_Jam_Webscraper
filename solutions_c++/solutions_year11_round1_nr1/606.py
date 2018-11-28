#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,pd,pg;
    long long n;
    cin >> t;
    for (int casenum=1; casenum<=t; ++casenum){
        cin >> n >> pd >> pg;
        bool ok = true;
        if (pd != 100 && pg == 100)
            ok = false;
        if (pd != 0 && pg == 0)
            ok = false;
        if (ok){
            int d = 100;
            if (pd % 5 == 0) d /= 5;
            if (pd % 25 == 0) d /= 5;
            if (pd % 2 == 0) d /= 2;
            if (pd % 4 == 0) d /= 2;
            if (d > n) ok = false;
        }
        if (ok)
            printf("Case #%d: Possible\n",casenum);
        else printf("Case #%d: Broken\n",casenum);
    }
    return 0;
}
