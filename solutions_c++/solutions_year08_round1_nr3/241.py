#include <algorithm>
#include <iostream>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <queue>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

const string res[31] = {"001", "005", "027", "143", "751", "935", "607", "903", "991", "335",
                        "047", "943", "471", "055", "447", "463", "991", "095", "607", "263",
                        "151", "855", "527", "743", "351", "135", "407", "903", "791", "135", "647"};

int main()
{
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        printf("Case #%d: %s\n", i + 1, res[n].c_str());
    }
    return 0;
}

/*const int MAXN = 100000;

template <typename _Tp>
inline _Tp __cmath_power(_Tp __x, unsigned int __n)
{
	//If _Tp is a class, there must be a construct funciton
	_Tp __y = __n % 2 ? __x : 1;
	while (__n >>= 1)
	{
		__x = __x * __x;
		if (__n % 2)
		{
			__y = __y * __x;
		}
	}
	return __y;
}

template <class T>
inline T gcd(T a, T b)
{
    if (a == 0) return b;
    else return gcd(b % a, a);
}

inline int c(long long n, long long m)
{
    if (m * 2 > n) m = n - m;
    long long up = 1, down = 1;
    for (int i=1;i<=m;i++)
    {
        up *= (n - i + 1);
        down *= i;
        long long k = gcd(up, down);
        up /= k; down /= k;
    }
    return up % MAXN;
}

inline long long calc(int a, int b)
{
    return __cmath_power(5, a / 2) * __cmath_power(3, b) % MAXN;
}

inline long long MySqrt(long long n)
{
    long long left = 0, right = n;
    while (left <= right)
    {
        long long mid = (left + right) / 2;
        if (mid * mid == n) return mid;
        if (mid * mid > n) right = mid - 1;
        else left = mid + 1;
    }
    while (left * left > n) left--;
    return left;
}

int main()
{
    int t;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        long long sum1 = 0, sum2 = 0;
        for (int i=0;i<=n;i++)
        {
            // sqrt(5) ^ i * 3 ^ (n - i)
            if (i % 2 == 0) sum1 = (sum1 + calc(i, n - i) * c(n, i)) % MAXN;
            else sum2 = (sum2 + calc(i - 1, n - i) * c(n, i));
        }
        // Form a + b * sqrt(5)
        // Then calc 5 * b ^ 2, then sqrt it
        printf("Case #%d: %lld\n", i + 1, (sum1 + MySqrt(sum2 * sum2 * 5)) % 1000);
    }
	return 0;
}*/