#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <functional>
#include <algorithm>

using namespace std;

int main( void )
{
    int TC;
    scanf( "%d", &TC );

    for (int tc = 0; tc < TC; tc++)
    {
        int N, M, A;
        scanf( "%d%d%d", &N, &M, &A );

        int Ay = 0;
        for (int Ax = 0; Ax <= N; Ax++)
        {
            int Bx = 0;
            for (int By = 0; By <= M; By++)
            {
                for (int Cx = 0; Cx <= N; Cx++) for (int Cy = 0; Cy <= M; Cy++)
                {
                    int A2 = (Ax*(By-Cy) + Bx*(Cy-Ay) + Cx*(Ay-By));
                    if (A2 == A || A == -A2)
                    {
                        cout << "Case #" << (tc+1) << ": "
                            << Ax << " " << Ay << " "
                            << Bx << " " << By << " "
                            << Cx << " " << Cy
                            << endl;
                        goto end;
                    }
                }
            }
        }

        cout << "Case #" << (tc+1) << ": IMPOSSIBLE" << endl;
end:;
    }
}
