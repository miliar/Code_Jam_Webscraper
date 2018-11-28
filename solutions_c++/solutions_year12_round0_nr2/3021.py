#include <iostream>
#include <string>
#include <map>

using namespace std;

bool yes(int num, int & s, int p)
{
    int exp = 0;
    if (num == 0)
    {
        exp = 0;
    }
    else if (num == 1)
    {
        exp = 1;
    }
    else if (num == 2)
    {
        exp = 1;
        if (exp >= p)
        {
            return true;
        }
        else if (s > 0)
        {
            exp = 2;
            if (exp >= p)s--;
        }
    }
    else if (num % 3 == 0)
    {
        exp = num / 3;
        if (exp >= p)
        {
            return true;
        }
        else if (s > 0)
        {
            exp = num / 3 + 1;
            if (exp >= p)s--;
        }
    }
    else if (num % 3 == 1)
    {
        exp = num / 3 + 1;
    }
    else
    {
        exp = num / 3 + 1;
        if (exp >= p)
        {
            return true;
        }
        else if (s > 0)
        {
            exp = num / 3 + 2;
            if (exp >= p)s--;
        }
    }
    
    if (exp >= p) return true;
    else return false;
}

void run()
{
    int n, s, p;
    scanf("%d %d %d", &n, &s, &p);
    int a[110];
    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        if (yes(a[i], s, p))
        {
            ans++;
        }
    }
    cout << ans << endl;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    int N = 0;
    scanf("%d", &N);
    getchar();
    for (int k = 1; k <= N; k++)
    {
        printf("Case #%d: ", k);
        run();
    }
    return 0;
}
