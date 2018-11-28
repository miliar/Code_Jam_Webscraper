#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <ctime>
using namespace std;


#define forn(i, n) for(int i = 0; i < n; i++)
long long t, a, b;
int ans;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int test = 1; test <= t; test++)
    {
        cin >> a >> b;
        ans = 0;
        long long j = 1, z;
        while(j <= a)
        {
            j *= (long long)(10);
        }
        for(long long i = a; i <= b; i++)
        {
            long long temp = i + j * i;
            long long k;
            long long prevk = 1;
            z = j;
            while(1)
            {
                z /= 10;
                if(z != 1)
                {
                    k = (temp / z) % j;
                    if(k >= a  &&  k <= b  &&  i < k  &&  k != prevk)
                    {
                        ans++;
                        prevk = k;
                    }
                }
                else   break;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
}
