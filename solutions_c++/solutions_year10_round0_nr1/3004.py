#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int snapper(int n, int k);

int main()
{
    int inputs;
    cin >> inputs;


    for (int i = 0; i < inputs; ++i) {
        int n, k;
        cin >> n >> k;

        int output = snapper(n,k);
        if (output == 0)
                cout << "Case #" << (i+1) << ": OFF" << endl;
        if (output == 1)
                cout << "Case #" << (i+1) << ": ON" << endl;
    }

    cin.get();
}

int snapper(int n, int k)
{

    int mask = ~(~0<<n);
    int on = (k & mask) == mask;
    return on;
}
