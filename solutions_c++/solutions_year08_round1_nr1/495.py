#include <iostream>
#include <cstdio>
#include <functional>
#include <algorithm>
#define MAX 810
using namespace std;

int main()
{
    int T, t, n, i;
    int a[MAX],b[MAX];
	__int64 res;
    scanf("%d",&T);
    for (t = 1;t <= T;t++){
        scanf("%d",&n);
        for (i = 0;i < n;i++)
			scanf("%d",&a[i]);
        for (i = 0;i < n;i++)
			scanf("%d",&b[i]);
        sort(a,a+n);
        sort(b,b+n,greater<__int64>());
        res = 0;
        for (i = 0;i < n;i++)
            res += a[i]*b[i];
        printf("Case #%d: %I64d\n",t,res);
    }
}
