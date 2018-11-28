#include <stdio.h>
#include <iostream>

using namespace std;

#define MAX_N 100009

int main(void)
{
    long long count = 0;
    int grupo[3][3];
    int N, n, A, B, C, D, x0, y0, M;
    
    scanf("%d\n", &N);
    for (int caso = 1; caso <= N; caso++)
    {
        scanf("%d %d %d %d %d %d %d %d\n", &n, &A, &B, &C, &D, &x0, &y0, &M);
        /*
        X = x0, Y = y0
        print X, Y
        for i = 1 to n-1
          X = (A * X + B) mod M
          Y = (C * Y + D) mod M
          print X, Y
        */
        memset(grupo, 0, sizeof(grupo));
        long long X = x0;
        long long Y = y0;
        grupo[X % 3][Y % 3]++;
        for (int i = 1; i < n; i++)
        {
            X = ((long long) A * (long long) X + (long long) B) % M;
            Y = ((long long) C * (long long) Y + (long long) D) % M;
            grupo[X % 3][Y % 3]++;
        }

/*        for (int x = 0; x < 3; x++)
            for (int y = 0; y < 3; y++)
                printf("%d %d: %d\n", x, y, grupo[x][y]);
  */      
        count = 0;
        int x1, x2, x3, y1, y2, y3;

        //tres grupos diferentes
        long long tres_diferentes = 0;
        for (int x1 = 0; x1 < 3; x1++)
        for (int y1 = 0; y1 < 3; y1++)
            for (int x2 = 0; x2 < 3; x2++)
            for (int y2 = 0; y2 < 3; y2++)
                for (int x3 = 0; x3 < 3; x3++)
                for (int y3 = 0; y3 < 3; y3++)
                    if ((x1+x2+x3) % 3 == 0 && (y1+y2+y3) % 3 == 0)
                    {
                        int grupo1 = 3*x1+y1;
                        int grupo2 = 3*x2+y2;
                        int grupo3 = 3*x3+y3;
                        if (grupo1 != grupo2 && grupo1 != grupo3 && grupo2 != grupo3)
                        {
                            long long g1 = grupo[x1][y1];
                            long long g2 = grupo[x2][y2];
                            long long g3 = grupo[x3][y3];
                            tres_diferentes += g1 * g2 * g3;
                        }
                    }
        tres_diferentes /= 6;
        
        //tres grupos iguales
        long long tres_iguales = 0;
        for (int x1 = 0; x1 < 3; x1++)
        for (int y1 = 0; y1 < 3; y1++)
        {
            long long g1 = grupo[x1][y1];
            long long g2 = grupo[x1][y1] - 1;
            long long g3 = grupo[x1][y1] - 2;

            tres_iguales += g1 * g2 * g3 / 6;
        }

        //dos iguales
        long long dos_iguales = 0;
        for (int x1 = 0; x1 < 3; x1++)
        for (int y1 = 0; y1 < 3; y1++)
            for (int x2 = 0; x2 < 3; x2++)
            for (int y2 = 0; y2 < 3; y2++)
                if ((2*x1+x2) % 3 == 0 && (2*y1+y2) % 3 == 0)
                {
                    int grupo1 = 3*x1+y1;
                    int grupo2 = 3*x2+y2;
                    if (grupo1 == grupo2)
                        continue;

                    long long g1 = grupo[x1][y1];
                    long long g2 = grupo[x1][y1] - 1;
                    long long g3 = grupo[x2][y2];

                    dos_iguales += g1 * g2 * g3 / 2;
                }

        count = dos_iguales + tres_iguales + tres_diferentes;
        cout << "Case #" << caso << ": " << count << "\n";
    }
    return 0;
}
