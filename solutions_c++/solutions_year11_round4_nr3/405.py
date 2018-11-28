#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<ctime>
#include<vector>
#include<map>
#include<set>
#include<cstring>
using namespace std;

const int maxN = 1000010;

int pList[maxN], cntP = 0;
bool pFlag[maxN];

void makePrime()
{
    long long a, b;
    memset(pFlag, 0, sizeof(pFlag));
    for(a = 2; a < maxN && a * a < maxN; a++)
        if(!pFlag[a])
        {
            pList[cntP++] = a;
            b = a * a;
            while(b <= maxN) pFlag[b] = true, b += a;
        }
    for(; a < maxN; a++)
        if(!pFlag[a]) pList[cntP++] = a;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    makePrime();

    int T, tt, minAns, maxAns, i, ans;
    long long N, a;
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        cin >> N;
        //minAns = (N == 1) ? 1 : 0;
        //maxAns = 1;
        ans = 0;
        for(i = 0; i < cntP && (long long)pList[i] * pList[i] <= N; i++)
        {
            //minAns++;
            a = pList[i];
            while(a * pList[i] <= N) ans++, a *= pList[i];
        }
        if(N > 1) ans++;
        printf("Case #%d: %d\n", tt, ans);
    }

    return 0;
}
