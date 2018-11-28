#include <iostream>
#include <stdio.h>
using namespace std;

const int N = 1005;
int a[N];

int main()
{
    //freopen("B-large (1).in", "r", stdin);
    //freopen("b.txt", "w", stdout);
    int cas;
    cin >> cas;
    int n, p, S;
    for (int k = 0; k < cas; k++)
    {
        cin >> n;
        cin >> S >> p;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int num = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] > 3 * p - 3) num++;
            else if (a[i] >= p && a[i] >= p * 3 - 4)
            {
                if (S > 0)
                {
                    S--;
                    num++;
                }
            }
        }
        cout << "Case #" << k + 1 << ": " << num << endl;
    }
    return 0;
}
