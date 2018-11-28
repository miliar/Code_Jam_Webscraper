#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin>>T;

    for(int i = 1; i <= T; i++)
    {
        int n, k;
        cin>>n>>k;

        int mid = 1<<n;
        k %= mid;

        bool f = (k == (mid-1));

        printf("Case #%d: %s\n", i, f ? "ON" : "OFF");
    }
}
