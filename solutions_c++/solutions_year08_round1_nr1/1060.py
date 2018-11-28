#include <cstdio>
#include <algorithm>
const int inf = 0x3fffffff;
long long v1[800];
long long v2[800];

int main()
{
    int i, j, tmp;
    int n;
    long long pro;
    int casenum, casei;
    scanf("%d", &casenum);
    for(casei=1;casei<=casenum;casei++)
    {
        scanf("%d", &n);
        for(j=0;j<n;j++)
            scanf("%I64d", &v1[j]);
        for(j=0;j<n;j++)
            scanf("%I64d", &v2[j]);
        std::sort(v1, v1+n);
        std::sort(v2, v2+n);
        for(j=pro=0;j<n;j++)
            pro+=v1[j]*v2[n-j-1];
        printf("Case #%d: %d\n", casei, pro);
    }
}
