#include<iostream>
#include<vector>
using namespace std;



int main()
{
    int t, n, k, caso = 1;
    cin >> t;
    while(t--)
    {
        cin >> n >> k;
        int num = 1;
        for(int i = 0; i < n; ++i)
        {
            num*=2;
        }
        cout << "Case #" << caso++ << ": ";
        ((k+1)%num == 0)? cout << "ON\n": cout << "OFF\n";
    }
    return 0;
}
