#include <iostream>
#include <stdlib.h>

using namespace std;

int power(int x, int m)
{
    if (m > 1)
    {
        div_t temp = div(m, 2);
        int rec = power(x, temp.quot);
        if (temp.rem == 1)
        {
            return rec*rec*x;
        }
        else
        {
            return rec*rec;
        }
    }
    else if (m == 1)
    {
        return x;
    }
    else
    {
        return 1;
    }
}

int main()
{
    int count;
    cin >> count;
    for (int i=0;i<count;i++)
    {
        int n, k;
        cin >> n;
        cin >> k;
        int mult = power(2, n);
        int new_k = (div(k, mult)).rem;

        cout << "Case #" << (i+1) << ": ";
        if (new_k == (mult-1) )
        {
            cout << "ON" << endl;
        }
        else
        {
            cout << "OFF" << endl;
        }
    }
    return 1;
}

