/*
 * summary:
 *
 */

#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <string.h>
#define INF (1<<30)
#define MAX 0
#define EPS 0
using namespace std;

char D[10005][15];
bool bit[12][30][10005];
bool wordbit[10005][26];
bool len[11][10005];
char list[30];
bool remain[10005];
bool word[30];

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    int T, N, M;
    scanf("%d", &T);
    for(int tcase = 1; tcase <= T; tcase++)
    {
        scanf("%d%d", &N, &M);
        memset(bit, 0, sizeof(bit));
        memset(len, 0, sizeof(len));
        memset(wordbit, 0, sizeof(wordbit));
        for(int i = 0; i < N; i++)
        {
            scanf("%s", D[i]);
            int j;
            for(j = 0; D[i][j]; j++)
            {
                bit[j][ D[i][j] - 'a' ][i] = true;
                wordbit[i][ D[i][j] - 'a' ] = true;
            }
            len[j][i] = true;
        }
        printf("Case #%d:", tcase);
        for(int i = 0; i < M; i++)
        {
            scanf("%s", list);
            int max = 0, pos = 0;
            for(int j = 0; j < N; j++)
            {
                int point = 0;
                memset(word, 0, sizeof(word));
                int l = strlen(D[j]);
                for(int k = 0; k < N; k++)
                    if(len[l][k])
                        for(int kk = 0; D[k][kk]; kk++)
                            word[ D[k][kk] - 'a' ] = true;
                memcpy(remain, len[l], N);
                for(int k = 0; k < 26; k++)
                    if(word[ list[k] - 'a' ])
                    {
                        if(!wordbit[j][ list[k] - 'a' ]) point++;
                        for(int kk = 0; kk < N; kk++)
                            if(remain[kk])
                            {
                                for(int p = 0; D[j][p]; p++)
                                    if((D[j][p] == list[k] && D[kk][p] != list[k]) || (D[j][p] != list[k] && D[kk][p] == list[k]))
                                        remain[kk] = 0;
                            }
                        memset(word, 0, sizeof(word));
                        for(int kk =0; kk < N; kk++)
                            if(remain[kk])
                                for(int kkk = 0; D[kk][kkk]; kkk++)
                                    word[ D[kk][kkk] - 'a' ] = true;
                    }
                if(max < point)
                    max = point, pos = j;
            }
            printf(" %s", D[pos]);
        }
        printf("\n");
    }

    return 0;
}
