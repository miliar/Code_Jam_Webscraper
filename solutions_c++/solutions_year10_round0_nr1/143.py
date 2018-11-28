#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 32

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int C = 0, T;
    int turn[SIZE] = {0};

    for (int i = 1; i < SIZE; i++)
        turn[i] = 2 * turn[i - 1] + 1;
    scanf("%d", &T);
    while (T--)
    {
        int N, K;
        scanf("%d %d", &N, &K);
        bool res = K % (turn[N] + 1) == turn[N];
        printf("Case #%d: %s\n", ++C, res ? "ON" : "OFF");
    }

    return 0;
}
