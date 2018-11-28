#include <iostream>
#include <stdio.h>
using namespace std;
const int maxn=100;
int t, n, s, p, cnt, ans;
int per[maxn];
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    cnt=1;
    while (t--)
    {
        scanf("%d %d %d", &n, &s, &p);
        for (int i=0; i<n; i++) scanf("%d", &per[i]);
        ans=0;
        for (int i=0; i<n; i++)
        {
            int avg=per[i]/3;
            int left=per[i]%3;
            if (avg>=p) {ans++; continue;}
            if (left==0)
            {
                if (avg==0) continue;
                if (avg==p-1&&s>0)
                {
                    ans++, s--;
                }
            }
            else if (left==1)
            {
                if (avg==p-1) ans++;
            }
            else
            {
                if (avg==p-1) ans++;
                else if (avg==p-2&&s>0)
                {
                    ans++, s--;
                }
            }
        }
        printf("Case #%d: %d\n",cnt++, ans);
    }
    return 0;
}
