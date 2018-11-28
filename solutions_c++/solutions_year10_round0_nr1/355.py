#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;
int power2[40];

int a, b, n;

int main(void)
{
    power2[0] = 1;
    for (int i=1; i<32; ++i)
        power2[i] = power2[i-1] * 2;
    cin >> n;
    for (int i=1; i<=n; ++i) {
        cin >> a >> b;
        if ((b+1) % power2[a] == 0)
            cout << "Case #" << i << ": ON" << endl;
        else
            cout << "Case #" << i << ": OFF" << endl;
    }
    return 0;
}
