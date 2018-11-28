#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

bool isprime[1200000];

int main()
{
    int teste, t;
    scanf("%d", &teste);

    int i, j;
    for (i=0; i < 1100000; i+=2)
    {
        isprime[i] = false;
        isprime[i+1] = true;
    }
    isprime[0] = false;
    isprime[1] = false;
    isprime[2] = true;
    for (i = 3; i < 1100000; i+=2)
    {
        if (isprime[i] == true)
        {
            for (j = i + i; j < 1100000; j+=i)
            {
                isprime[j] = false;
            }
        }
    }

    for (t=0; t<teste; t++)
    {
        long long a, b, n;
        scanf("%I64d", &n);

        if (n == 1)
        {
            printf("Case #%d: 0\n", t+1);
        }
        else
        {
            int ans = 1;

            for (a = 2; a * a <= n; a++)
            {
                if (isprime[a])
                {
                    int count = 0;
                    b = a * a;
                    while(b <= n)
                    {
                        b *= a;
                        count++;
                    }
                    ans += count;
                }
            }

            printf("Case #%d: %d\n", t+1, ans);
        }
    }
    return 0;
}
