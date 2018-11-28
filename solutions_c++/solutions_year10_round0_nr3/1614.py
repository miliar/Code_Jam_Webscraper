#include <iostream>
using namespace std;

int T, Ti;
int R, k, N, g[1100], p[1100][2];
long long res;

void init()
{
    int i;

    res = 0;
    memset(g, 0, sizeof(g));
    memset(p, 0, sizeof(p));
    cin >> R >> k >> N;
    for (i = 1; i <= N; i++)
        cin >> g[i];
}

void work()
{
    int i, j, count, sum;
    
    for (i = 1; i <= N; i++)
    {
        j = i;
        sum = 0;
        count = 0;
        while (count < N && sum + g[j] <= k)
        {
            sum += g[j];
            j = (j % N) + 1;
            count++;
        }
        p[i][0] = sum;
        p[i][1] = j;
    }

    j = 1;
    for (i = 1; i <= R; i++)
    {
        res += p[j][0];
        j = p[j][1];
    }
    cout << "Case #" << Ti << ": " << res << endl;
}

int main()
{
    cin >> T;
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }     

  //  system("pause");
    return 0;
}
