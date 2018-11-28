#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test = 0;
    scanf("%d", &test);
    for(int i = 0; i < test; i++)
    {
        int n = 0;
        scanf("%d", &n);
        long long  Xor = 0;
        long long min = -1;
        long long sum = 0;
        for(int j = 0; j < n; j++)
        {
            long long t;
            cin >> t;
            if((min == -1) || (t < min))
                min = t;
            Xor ^= t;
            sum += t;
        }
        printf("Case #%d:", i + 1);
        if(Xor != 0)
            printf(" NO\n");
        else
            cout << " " << sum - min << endl;
    }
    return 0;
}
