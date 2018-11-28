#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int a[1000], b[1000];
int fun(int n)
{
    int re = 0;
    for(int i = 0; i < n; i++)
    {
        for(int j = i + 1; j < n; j++)
        {
            if((a[i] - a[j]) * (b[i] - b[j]) < 0) re++;
        }
    }
    return re;
}
int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    for(int ci = 1; ci <= T; ci++)
    {
        int n;
        cin >> n;
        for(int i = 0; i < n; i++)
        {
            cin >> a[i] >> b[i];
        }
        cout << "Case #" << ci << ": " << fun(n) << endl;;
    }
    return 0;
}
