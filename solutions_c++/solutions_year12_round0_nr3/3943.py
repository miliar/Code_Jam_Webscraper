#include <iostream>
#include <cstdlib>
#include <string.h>
#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>

using namespace std;

int n;

int next_num(int num, int r, int l)
{
    int res = 0;
    char s[10];
    sprintf(s, "%d", num);
    int len = strlen(s);

    for(;;)
    {
        char tmp = s[len - 1];
        for (int i = len - 1; i > 0; i--)
            s[i] = s[i - 1];
        s[0] = tmp;

        int val = atoi(s);
        if (val == num)
            break;
        if (s[0] != '0' && val <= r && val >= l)
            res++;
    }
    return res;
}

int go(int l, int r)
{
    int res = 0;
    for (int i = l; i <= r; i++)
    {
        res += next_num(i, r, l);
    }
    return res / 2;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for (int i = 0;i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": " << go(a, b) << endl;
    }
    return 0;
}
