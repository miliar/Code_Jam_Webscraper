#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int casos = 0;
    int nrocasos;
    cin >> nrocasos;
    while (nrocasos--)
    {
        casos++;
        int valorN, valorK;
        cin >> valorN >> valorK;
        int switches = pow(2.0,valorN);
        if ((valorK+1) % switches)
        {
            cout << "Case #" << casos << ": OFF" << endl;
        }
        else
        {
            cout << "Case #" << casos << ": ON" << endl;
        }

    }
    return 0;
}
