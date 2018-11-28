#include <iostream>
#include <cstdio>


using namespace std;


int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        int n;
        cin >> n;

        int small = -1;
        int sum = 0;
        int xorSum = 0;
        while(n --)
        {
            int a;
            cin >> a;
            sum += a;
            xorSum ^= a;
            if(small == -1 || small > a)
                small = a;
        }
        cout << "Case #" << i + 1 << ": ";

        if(xorSum)
            cout << "NO" << endl;
        else
            cout << sum - small << endl;
    }
    return 0;
}
