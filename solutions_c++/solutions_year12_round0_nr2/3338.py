#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <climits>
#include <cstdio>
#include <algorithm>




using namespace std;
const int MAXN = 110;
int T;
int N;
int S, p;
int t[MAXN];
int record[MAXN][2];
bool vis[MAXN];
int tarray[MAXN];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for(int i = 0; i < T; i++)
    {
        int nMax = 0;
        scanf("%d %d %d", &N, &S, &p);
        for(int j = 0; j < N; j++)
        {
            scanf("%d", &t[j]);
        }
        memset(record, -1, sizeof(record));
        for(int j = 0; j < N; j++)
        {
            for(int k = 2; k <= 4; k++)
            {
                if((t[j] + k) % 3 == 0)
                {
                    int tmp = (t[j] + k) / 3;
                    record[j][0] = tmp;
                    break;
                }
            }
            record[j][1] = (t[j] / 3) + (t[j] % 3 > 0);
        }

        for(int j = 0; j < N; j++)
        {
            if(record[j][1] >= p) nMax++;
            else if(S > 0 && record[j][0] >= p && record[j][0] <= 10 && record[j][0] - 2 >= 0)
            {
                S--;
                nMax++;
            }
        }
        printf("Case #%d: %d\n", i + 1, nMax);
    }











    return 0;
}
