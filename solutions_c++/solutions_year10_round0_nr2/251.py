#include <iostream>
#include <algorithm>
using namespace std;

int fun(int a, int b)
{
    while(a % b)
    {
        int t = a % b;
        a = b;
        b = t;
    }
    return b;
}

int main(int argc, char *argv[])
{
    int C, N;
    cin >> C;
    for(int i = 1; i <= C; i++)
    {
        cout << "Case #" << i << ": ";
        cin >> N;
        int *ta = new int[N];
        for(int j = 0; j < N; j++) 
        {
            cin >> ta[j];
        }
        sort(ta, ta + N);
        int *tas = new int[N * (N - 1) / 2];
        int t = 0;
        for(int j = 0; j < N; j++)
        {
            for(int k = j + 1; k < N; k++)
            {
                tas[t++] = ta[k] - ta[j];
                if(tas[t - 1] == 0) t--;
            }
        }
        sort(tas, tas + t);
        int min = tas[0];
        for(int j = 1; j < t; j++)
        {
            min = fun(min, tas[j]);
        }
        cout << (min - ta[0] % min) % min << endl;
    }
    return 0;
}
