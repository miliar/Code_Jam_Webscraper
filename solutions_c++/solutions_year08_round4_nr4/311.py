#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long lint;

const int N = 50001;
const int M = 16;
char s[N];
char t[N];

int main()
{
    //freopen("D.in", "r", stdin);
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; ++cs)
    {
        int k;
        scanf("%d %s", &k, s);
        int n = strlen(s);
        int p[M]; for (int i = 0; i < k; ++i) p[i] = i;
        int res = n;
        do{
            for (int h = 0; h < n; h += k)
            {
                for (int i = 0; i < k; ++i)
                    t[h + i] = s[h + p[i]];
            }
            int comp = 0;
            for (int i = 1; i < n; ++i)
                if (t[i] != t[i-1]) ++comp;
            res = min(res, comp);
            //printf("%d\n", comp);
        }while (next_permutation(p, p + k));
        printf("Case #%d: %d\n", cs, res + 1);
    }
    return 0;
}
