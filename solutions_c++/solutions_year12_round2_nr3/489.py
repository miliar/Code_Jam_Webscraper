#include <iostream>
#include <string>
using namespace std;

int sum[2000000];
  int S[500];

void printmask(int mask)
{
   bool flag = false;
   for (int j = 0; j < 20; j++)
   {
       if (mask&(1<<j))
       {
           if (flag) cout << " ";
           cout << S[j];
           flag = true;
       }
   }
   cout << endl;
}

void solve()
{
    memset(sum, 0, sizeof(sum));

    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> S[i];

    for (int mask = 1; mask < (1 << 20); mask++)
    {
        int cursum = 0;
        for (int j = 0; j < N; j++)
         cursum += (mask&(1<<j)) ? S[j] : 0;

        if (sum[cursum] == 0) sum[cursum] = mask;
        else
        {
            printmask(mask);
            printmask(sum[cursum]);
            return;
        }
    }
    cout << "Impossible" << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ":" << endl;
        solve();
    }
}
