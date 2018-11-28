#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int casos = 0;
    int T;
    cin >> T;
    while (T--)
    {
        casos++;
        int N, K;
        cin >> N >> K;
        int switches = pow(2,N);
        if ((K+1) % switches)
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
