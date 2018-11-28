#include <iostream>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for(int i = 0; i < T; i++)
    {
        int N, K;

        cin >> N >> K;

        cout << "Case #" << (i + 1) << ": ";

        bool b = true;

        for(; N != 0; N--, K /= 2)
        {
            if(K % 2 == 0) b = false;
        }

        if(b) cout << "ON ";
        else cout << "OFF";
        
        cout << endl;
    }

    return 0;
}

