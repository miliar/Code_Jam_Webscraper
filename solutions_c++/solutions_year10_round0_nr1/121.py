#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, k;
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        cin >> n >> k;
        int mask = (1 << n) - 1;
        cout << "Case #" << t << ": ";
        if( (k & mask) == mask) 
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }
}