#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#include <map>
#include <set>
#include <list>

int b;

void add(long long &a, long long b)
{
    a = (a + b) % 1000000007;
}

void mul(long long &a, long long b)
{
    a = (a * b) % 1000000007;
}


long long cc[71][71];

long long c(int n, int i)
{
    if (i > n)
        return 0;
    if (cc[n][i])
        return cc[n][i];
    if (n <= 1)
        return 1;
    if (i == 0)
        return 1;
    add(cc[n][i], c(n - 1, i - 1));
    add(cc[n][i], c(n - 1, i));
    return cc[n][i];
}

long long ff[71];

long long fact(int i)
{
    if (ff[i])
        return ff[i];
    if (i <= 1)
        return 1;
    ff[i] = i;
    mul(ff[i], fact(i - 1));
    return ff[i];
}

// excluding zero variant
long long gr[71][71][36][71];
// d - last digit
// num - number of summands
// over - overflow
// start - minimum digit
long long g(int d, int num, int over, int start)
{
    if (d == 0 && over == 0 && num == 0)
        return 1;

    if (over * b + d <= 0 || start >= b || num == 0)
        return 0;

    long long &r = gr[d][num][over][start];
    if (r >= 0)
        return r;

    r = 0;
    // not take start
    add(r, g(d, num, over, start + 1));
    // take start
    int d1 = d - start;
    add(r, g(d1 < 0 ? d1 + b : d1, num - 1, d1 < 0 ? over - 1 : over, start + 1));

    return r;
}

// n - sum
// z - number of summands
long long f(long long n, int z)
{
    if (z == 1 && n >= 0)
        return 1;

    if (n == 0)
        return 1;

    if (n < 0 || z <= 0)
        return 0;

    long long r = 0;
    for (int over = 0 ; over <= (b + 1) / 2 ; ++over)
    {
        if (n / b - over < 0)
            break;
        if (n / b - over == 0)
        {
            long long bb = g(n % b, z, over, 1);
            add(r, bb);
        }
        else
        {
            for (int i = 1 ; i <= z ; ++i)
            {
                // i digits in the next column
                long long bb = g(n % b, z, over, 1);
                if (bb)
                {
                    mul(bb, c(z, i));
                    mul(bb, fact(i));
                    mul(bb, f(n / b - over, i));
                    add(r, bb);
                }
                // or i-1 digits + zeros
                bb = g(n % b, z - 1, over, 1);
                if (bb)
                {
                    mul(bb, c(z-1, i-1));
                    mul(bb, fact(i));
                    mul(bb, f(n / b - over, i));
                    add(r, bb);
                }
            }
        }
    }

    return r;
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        memset(gr, -1, sizeof(gr));
        std::cout << "Case #" << t << ": ";

        long long n;
        std::cin >> n >> b;

        long long r = 0;
        for (int i = 1 ; i <= b ; ++i)
        {
            add(r, f(n, i));
        }

        std::cout << r << "\n";
    }
    return 0;
}
