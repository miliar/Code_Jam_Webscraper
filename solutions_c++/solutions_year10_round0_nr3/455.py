#include <iostream>

/*
 next[i] - какая следующая группа будет
 sum[i]  - сколько денег за этот раз

 O(R)

 Найти цикл i1-i2-i3-...-ik-i1
 f(R % k) + f(k) * (R / k)

 O(N)
*/

long long sum[10000];
int next[10000];
long long R, k;
int N;
long long g[10000];
int check[10000];

long long f(int start, long long count)
{
    long long res = 0;
    for (int i = start ; count ; --count, i = next[i])
        res += sum[i];
    return res;
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ": ";
        std::cin >> R >> k >> N;
        {
            for (int i = 0 ; i < N ; ++i)
                std::cin >> g[i];
            for (int i = 0 ; i < N ; ++i)
            {
                long long s = 0;
                int j = i;
                for ( ; s + g[j] <= k && (s == 0 || j != i) ; j = (j + 1) % N)
                   s += g[j];
                sum[i] = s;
                next[i] = j;
                check[i] = 0;
            }
        }
        {
            long long res = 0;
            int len = 0;
            int i = 0;
            for ( ; !check[i] ; i = next[i])
            {
                ++len;
                check[i] = len;
            }
            int first = check[i] - 1;
            len -= first;
            if (R >= first)
                res = f(0, first) + f(i, len) * ((R - first) / len) + f(i, (R - first) % len);
            else
                res = f(0, R);
            
            std::cout << res << "\n";
        }
    }

	return 0;
}

