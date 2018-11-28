#include <iostream>
using namespace std;


int getOrd(int x, int n, int ss)
{
    if(!((ss >> (x - 1)) & 1))
        return -1;
    int counter = 0;
    for(int i = 1; i <= x; i++)
    {
        counter += (ss & 1);
        ss >>= 1;
    }
    return counter;
}

bool isPure(int n, int ss)
{
    int x = n;
    while(x > 1)
    {
        x = getOrd(x, n, ss);
        if(x < 0)
            return false;
    }
    return true;
}

int getTot(int n)
{
    int sum = 0;
    for(int i = 2; i < (1 << (n-1)); i+=2)
    {
        int ss = i | (1 << (n-1));
        sum = (sum + isPure(n, ss)) % 100003;
    }
    return (sum + 1) % 100003;
}

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        int n;
        cin >> n;
        cout << "Case #" << t << ": " << getTot(n) << endl;
    }
    return 0;
}

