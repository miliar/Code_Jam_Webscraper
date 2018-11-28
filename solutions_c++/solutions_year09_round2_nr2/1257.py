/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>

#define pf printf
#define sf scanf
#define TIME pf("%f\n", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N;

int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    
    cin >> N;
    char c[21];
    
    for (int i = 0; i < N; i++) {
        cin >> c;
        int j = 0, n = strlen(c);
        for (j = n - 1; j > 0; j--)
            if (c[j] > c[j - 1]) {
          //     if (c[j - 1] != '0')
            //      swap(c[j], c[j - 1]);
            //   else {
                 int minn = c[j], minj = j;
                 for (int k = j + 1; k < n; k++)
                     if (c[k] != '0') 
                        if (minn > c[k] && c[k] > c[j - 1]) minn = c[k], minj = k;
                 swap (c[j - 1], c[minj]);
             //  }
               sort(c + j, c + n);
               break;
            }
        cout << "Case #" << i + 1 << ": ";
        if (j != 0) cout << c << endl;
        else {
           int minn = INT_MAX, minj = -1;
           for (int j = 0; j < n; j++)
               if (c[j] != '0') 
                  if (minn > c[j]) minn = c[j], minj = j;
           char cc = minn;
           c[minj] = '0';
           sort (c, c + n);
           cout << cc;
           for (int j = 0; j < n; j++)
               cout << c[j];
           cout << endl;
        }
    }
    

    sf("%i", &N);
}
