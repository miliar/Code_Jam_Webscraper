#include <iostream>
using namespace std;

int solve()
{
     int A[40];
     
     int N;
     cin >> N;
     for (int i = 0; i < N; i++)
     {
         char r[41];
         cin >> r;
         A[i] = -1;
         for (int k = 0; k < N; k++) if (r[k] == '1') A[i] = k;
     }
     
     int ans = 0;
     for (int i = 0; i < N; i++)
     {
         if (A[i] <= i) continue;
         
         int i2 = i + 1;
         for (; i2 < N; i2++) if (A[i2] <= i) break;
         
         while (i2 != i) swap(A[i2], A[i2-1]), ans++, i2--;
     }
     return ans;
}
int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) 
    {
        cout << "Case #" << i + 1 << ": " << solve() << endl;
    }
    return 0;
}
