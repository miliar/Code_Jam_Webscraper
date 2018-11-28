#include <iostream>
using namespace std;

int N, K, T, Ti;

void init()
{
     cin >> N >> K;
}

void work()
{
    int i, x, res;

    res = 1;
    for (i = 1; i <= N; i++)
    {
        x = K % 2;
        if (!x)
        {
            res = 0;
            break;
        }
        K /= 2;
    }
    cout << "Case #" << Ti << ": " << (res ? "ON" : "OFF") << endl;
}

int main()
{
    cin >> T;
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

    //system("pause");
    return 0;
}
