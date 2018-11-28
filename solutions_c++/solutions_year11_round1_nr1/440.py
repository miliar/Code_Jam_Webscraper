#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>

using namespace std;

int tn,ti,i,pd,pg,win,tot;
bool flag;
long long n;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tn);
    for (ti = 1; ti <= tn; ti++)
    {
        cin >> n >> pd >> pg;
        flag = false;
        if (n >= (long long)100) n = 100;
        for (i = 1; i <= n; i++)
            if (i * pd % 100 == 0)
            {
                win = i * pd / 100;
                if (win < i && pg == 100 || win > 0 && pg == 0) continue;
                flag = true; break;
            }
        if (flag) printf("Case #%d: Possible\n",ti);
        else printf("Case #%d: Broken\n",ti);
    }
}
