#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int T, N, K, potencia, temp;
    cin >> T;
    string status;
    for (int i = 1; i <= T; i++) {
        status = "ON";
        cin >> N >> K;
        temp = K;
        potencia = pow(2.0, N);
        while (temp > potencia) temp -= potencia;
        if (temp != potencia - 1) status = "OFF";
        cout << "Case #" << i << ": " << status << endl;
    }
}
