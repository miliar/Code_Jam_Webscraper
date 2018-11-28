#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int tests, n, a[1010], sum;

bool check(int k)
{
        int t = 0;
        for (int i = 0; i < n; i++)
                t ^= a[i];
        return t == 0;
}

void solve(int test)
{
        cin >> n;
        sum = 0;
        for (int i = 0; i < n; i++)
        {
                cin >> a[i];
                sum += a[i];
        }
        sort(a, a+n);
        for (int i = 0; i < n; i++)
                if (check(i))
                {
                        cout << "Case #" << test << ": " << sum - a[i] << endl;
                        return;
                }
        cout << "Case #" << test << ": NO" << endl;
}

int main()
{
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
        cin >> tests;
        for (int test = 1; test <= tests; test++)
        {
                solve(test);
        }
        return 0;
}