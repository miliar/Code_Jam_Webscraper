#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <iterator>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cstddef>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

#define SZ 12

int bn_read(char *str, int bn[SZ])
{
    int len = strlen(str);
    for (int i = 0; i < SZ; i++)
        bn[i] = 0;
    int factor = 1;
    for (int i = 0; i < len; i++)
    {
        bn[i/5] += (str[len-i-1]-'0')*factor;
        if (factor == 10000)
            factor = 1;
        else
            factor *= 10;
    }
    return 1;
}

int bn_double(int ori[SZ], int ret[SZ])
{
    memcpy(ret, ori, sizeof(int)*SZ);
    int up = 0;
    for (int i = 0; i < SZ; i++)
    {
        ret[i] = ret[i]*2;
        ret[i] += up;
        up = 0;
        if (i < SZ-1 && ret[i] >= 100000)
        {
            ret[i] -= 100000;
            up = 1;
        }
    }
    return 1;
}

int bn_half(int ori[SZ], int ret[SZ])
{
    memcpy(ret, ori, sizeof(int)*SZ);
    int down = 0;
    for (int i = SZ-1; i >= 0; i--)
    {
        if (down)
            ret[i] += 100000;
        down = 0;
        if (ret[i]&1)
            down = 1;
        ret[i] /= 2;
    }
    return 1;
}

int bn_comp(int a[SZ], int b[SZ])
{
    for (int i = SZ-1; i >= 0; i--)
    {
        if (a[i] > b[i])
            return 1;
        else if (a[i] < b[i])
            return -1;
    }
    return 0;
}

int bn_miner(int a[SZ], int b[SZ], int ret[SZ])
{
    int borrow = 0;
    for (int i = 0; i < SZ; i++)
    {
        ret[i] = a[i] - b[i] - borrow;
        borrow = 0;
        if (ret[i] < 0)
        {
            ret[i] += 100000;
            borrow = 1;
        }
    }
    return 1;
}

int bn_multi10(int ori[SZ], int ret[SZ])
{
    memcpy(ret, ori, sizeof(int)*SZ);
    int up = 0;
    for (int i = 0; i < SZ; i++)
    {
        ret[i] *= 10;
        ret[i] += up;
        up = 0;
        if (ret[i] >= 100000)
            up = ret[i]/100000;
        ret[i] %= 100000;
    }
    return 1;
}

int bn_mod(int a[SZ], int b[SZ], int ret[SZ])
{
    memcpy(ret, a, sizeof(int)*SZ);
    while (bn_comp(ret, b) >= 0)
    {
        int tmp1[SZ], tmp2[SZ];
        memcpy(tmp2, b, sizeof(int)*SZ);
        while (bn_comp(ret, tmp2) >= 0)
        {
            memcpy(tmp1, tmp2, sizeof(int)*SZ);
            bn_multi10(tmp1, tmp2);
        }
        int tmp3[SZ];
        memcpy(tmp3, ret, sizeof(int)*SZ);
        bn_miner(tmp3, tmp1, ret);
    }
    return 1;
}

int gcd(int a, int b)
{
    int min = a<b?a:b;
    int max = a<b?b:a;
    if (min == 0)
        return max;
    else if ((min&1)==0 && (max&1)==0)
        return 2*gcd(min/2, max/2);
    else if ((min&1)==0)
        return gcd(min/2, max);
    else if ((max&1)==0)
        return gcd(max/2, min);
    else
        return gcd(max-min, min);
    return 1;
}

int bn_gcd(int a[SZ], int b[SZ], int ret[SZ])
{
    int comp = bn_comp(a,b);
    int *min = (comp == -1?a:b);
    int *max = (comp == -1?b:a);
    int zero[SZ]={0};
    if (bn_comp(min,zero) == 0)
        memcpy(ret, max, sizeof(int)*SZ);
    else if ((min[0] & 1)==0 && (max[0] & 1)==0)
    {
        int m1[SZ];
        int m2[SZ];
        int tmp[SZ];
        bn_half(min, m1);
        bn_half(max, m2);
        bn_gcd(m1, m2, tmp);
        bn_double(tmp, ret);
    }
    else if ((min[0]&1)==0)
    {
        int m1[SZ];
        bn_half(min, m1);
        bn_gcd(m1, max, ret);
    }
    else if ((max[0]&1)==0)
    {
        int m1[SZ];
        bn_half(max, m1);
        bn_gcd(min, m1, ret);
    }
    else
    {
        int m1[SZ];
        bn_miner(max, min, m1);
        bn_gcd(m1, min, ret);
    }
    return 1;
}

int comp(const void *p1, const void *p2)
{
    return bn_comp((int *)p1, (int *)p2);
}

int main(int argc, char *argv[])
{
    /*
    int a[SZ],b[SZ],c[SZ];
    char str[60];
    scanf("%s", str);
    bn_read(str, a);
    scanf("%s", str);
    bn_read(str, b);
    bn_mod(a, b, c);
    for (int i = SZ-1; i>=0;i--)
        printf("%05d ", c[i]);
    printf("\n");
    return 0;
    */

    int ncase;
    scanf("%d", &ncase);
    for (int icase = 1; icase <= ncase; icase++)
    {
        /*
        int n;
        scanf("%d", &n);
        vector <int> vt;
        for (int i = 0; i < n; i++)
        {
            int t;
            scanf("%d", &t);
            vt.push_back(t);
        }
        sort(vt.begin(), vt.end(), less<int>());
        vector <int> vi;
        for (int i = 0; i < n-1; i++)
            vi.push_back(vt[i+1]-vt[i]);
        vi.push_back(vt[n-1]-vt[0]);
        int ret = vi[0];
        for (int i = 0; i < n; i++)
            ret = gcd(vi[i], ret);
        int rem = ret-vt[0]%ret;
        if (rem == ret)
            rem = 0;
        printf("Case #%d: %d\n", icase, rem);
        */

        int n;
        scanf("%d", &n);
        int vt[1000][SZ];
        for (int i = 0; i < n; i++)
        {
            char t[100];
            scanf("%s", t);
            int bn[SZ];
            bn_read(t, vt[i]);
        }
        qsort(vt, n, sizeof(int)*SZ, comp);
        int vi[1000][SZ];
        for (int i = 0; i < n-1; i++)
            bn_miner(vt[i+1],vt[i],vi[i]);
        bn_miner(vt[n-1],vt[0],vi[n-1]);
        int ret[SZ];
        memcpy(ret, vi[0], sizeof(int)*SZ);
        for (int i = 0; i < n; i++)
        {
            int tmp[SZ];
            memcpy(tmp, ret, sizeof(int)*SZ);
            bn_gcd(vi[i], tmp, ret);
        }
        int md[SZ];
        bn_mod(vt[0], ret, md);
        int zero[SZ] = {0};
        int rem[SZ] = {0};
        if (bn_comp(md, zero) != 0)
            bn_miner(ret, md, rem);
        printf("Case #%d: ", icase);
        int start = SZ-1;
        for (; rem[start] == 0 && start > 0; start--);
        printf("%d", rem[start]);
        for (start--; start >= 0; start--)
            printf("%05d", rem[start]);
        printf("\n");
    }
    return 0;
}
