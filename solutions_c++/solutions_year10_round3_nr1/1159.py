#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

int main ()
{
    int T, id = 1;
    int i, j;
    
    scanf ("%d", &T);
 
    while (id <= T) {
        vector <int> X1, X2;
        int A, B, N;
        scanf ("%d", &N);

        for (i = 0; i < N; i ++) {
            scanf ("%d %d", &A, &B);
            X1.push_back (A);
            X2.push_back (B);
        }
        
        int ans = 0;
        
        for (i = 0; i < N; i ++) {

            for (j = 0; j < N; j ++) {

                if (j == i)
                    continue;

                if ((X1[i] > X1[j]) && (X2[i] < X2[j]))
                    ans ++;
                if ((X1[i] < X1[j]) && (X2[i] > X2[j]))
                    ans ++;
            }
        }

        cout << "Case #" << id << ": " << ans/2 << endl;
        id ++;
    }
    return 0;
}
