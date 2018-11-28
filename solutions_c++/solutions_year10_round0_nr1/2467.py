#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("A-large.out");
    int T, N, K, i =1;

    cin >> T;
    while(T--)
    {
        cin >> N >> K;
        bool a = false;
        while(N--)
            if(K % 2)
                K /= 2;
            else
            {
                a = true;
                break;
            }
        if(a) cout << "Case #" << i++ << ": OFF"  << endl;
        else  cout << "Case #" << i++ << ": ON" << endl;

    }

    return 0;
}
