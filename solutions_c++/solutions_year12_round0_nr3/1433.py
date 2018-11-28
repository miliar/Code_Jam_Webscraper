#include <iostream>
using namespace std;

int pow;
int next(int number)
{
    int lastdig = number%10;
    number /= 10;
    number += pow*lastdig;

    if (lastdig == 0)
    {
        return next(number);
    }
    return number;
}

void solve()
{
    int A, B;
    cin >> A >> B;

    int k = A;
    pow = 1;
    while (k > 0) k /= 10, pow *= 10;
    pow /= 10;

    int ans = 0;
    for (int i = A; i <= B; i++)
    {
        int nexti = next(i);
        while (nexti != i)
        {
            if (nexti > i && nexti <= B)
            {
                ans++;
            }
            nexti = next(nexti);
        }
    }
    cout << ans << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
