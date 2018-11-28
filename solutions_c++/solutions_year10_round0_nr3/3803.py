/* 
 * File:   newmain.cpp
 * Author: David
 *
 * Created on 2010��5��8��, ����10:45
 */

#include <stdlib.h>
#include <stdio.h>
#include <queue>
using namespace std;

const int MAX = 1001;
//queue<int> q;
int q[MAX];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        int R, k, N;
        scanf("%d%d%d", &R, &k, &N);
        for (int n = 0; n < N; n++)
        {
            //int a;
            //scanf("%d", &a);
            //q.push(a);
            scanf("%d", &q[n]);
        }

        int start = 0;
        int sum = 0;
        for (int i = 0; i < R; i++)
        {
            int kk = 0;
            int count = 0;
            while (kk + q[start] <= k && count < N)
            {
                kk += q[start];
                if (start < N - 1)
                    start++;
                else
                    start = 0;
           
                count++;
            }
              sum += kk;
        }

        printf("Case #%d: %d\n", c, sum);
    }

    return 0;
}

