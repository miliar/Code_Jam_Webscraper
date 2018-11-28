#include <iostream>
using namespace std;
bool happy(int n, int base)
{
    bool used[100000] = {false};
    int i, temp;
    while(1)
    {
        temp = 0;
        while(n != 0)
        {
            temp += (n % base) * (n % base);
            n /= base;
        }
        n = temp;
        if(n == 1 || used[n])
            break;
        used[n] = true;
    }
    return n == 1;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i, j, t, b[10], c, k;
    bool m[100001][11] = {false};
    for(i = 2; i <= 10; i++)
        for(j = 2; j <= 100000; j++)
            if(happy(j, i))
                m[j][i] = true;
    cin >> t;
    for(i = 1; i <= t; i++)
    {
        cout << "Case #" << i << ": ";
        c = 0;
        while(1)
        {
            cin >> b[c++];
            if(b[c - 1] == -1)
                break;
        }
        for(j = 2; j <= 100000; j++)
        {
            bool found = true;
            for(k = 0; k < c - 1; k++)
                if(!m[j][b[k]])
                    found = false;
            if(found)
            {
                cout << j << endl;
                break;
            }
        }
    }
    return 0;
}
