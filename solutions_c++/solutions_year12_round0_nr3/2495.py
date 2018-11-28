#include <cstring>
#include <cstdio>
using namespace std;

#define MAX 2000020

int len[MAX], t;
int power10[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, MAX};

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
    scanf("%d", & t);
    
    for (int i = 0; i < 7; ++ i)
        for (int j = power10[i]; j < power10[i + 1]; ++ j)
            len[j] = i + 1;
    
    for (int ii = 1; ii <= t; ++ ii)
    {
        int a, b, answer = 0;
        scanf("%d %d", & a, & b);
        for (int n = a; n <= b; ++ n)
        {
            int tmp[10];
            for (int j1 = 1, j2 = len[n] - 1; j1 < len[n]; ++ j1, -- j2)
            {
                int X = n / power10[j1], Y = n % power10[j1];
                int m = Y * power10[j2] + X;
            
                tmp[j1] = m;
                for (int t = 1; t < j1; ++ t)
                    if (tmp[t] == m)
                        m = 0;
            
                answer += (m > n && m <= b);
            }
        }
        printf("Case #%d: %d\n", ii, answer);
    }
//    fclose(stdout);
}


