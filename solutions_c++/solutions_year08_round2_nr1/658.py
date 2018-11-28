#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int T;
    scanf("%d\n", &T);
    for(int t = 0; t<T; t++) {
        long long n, A, B, C, D, x0, y0, M;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        scanf("\n");
        long long x [n], y[n];
        long long X = x0, Y = y0;
        x [0] = X, y [0] = Y;
        for(int i = 1; i < n; i++) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            x [i] = X; 
            y [i] = Y;
        }  
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j  + 1; k < n; k++) {
                    int p = (x [i] + x [j] + x [k]) % 3;
                    int q = (y [i] + y [j] + y [k]) % 3;
                    if ( p == 0 && q == 0 ) {
                        res++;
                    }
                }
            }
        }
        cout << "Case #" << t+1 << ": " << res << endl;
   }
   return 0;
}
   
        

            
