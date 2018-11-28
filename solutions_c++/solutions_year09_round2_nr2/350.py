#include <iostream>
#include <algorithm>
using namespace std;

int digits[10];

int main()
{
    int T;
    cin >> T;
    for (int qq = 0; qq < T; qq++)
    {
        char N[24];
        cin >> N;
        int L = strlen(N);
        
        int ri = -1;
        for (int i = 0; i < L-1; i++) 
         if (N[i] < N[i+1]) ri = i;
        
        if (ri == -1)
        {
               N[L] = '0';
               L++;
               N[L] = '\0';
               sort(N, N+L);
               for (int i = 0; i < L; i++) if (N[i] != '0') { swap(N[i], N[0]); break; }
               cout << "Case #" << qq+1 <<": " << N << endl;
               continue;
        }
        
        int base = N[ri];
        for (int i = ri + 1; i < L; i++) 
         if (N[i] > base && (N[ri] == base || N[i] < N[ri])) swap(N[ri], N[i]);
         
        sort(N+ri+1, N+L);
        cout << "Case #" << qq+1 <<": " << N << endl;
    }
    return 0;
}
