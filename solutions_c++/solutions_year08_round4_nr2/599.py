#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

int N, M, A;

double abs(double x)
{
    return x < 0 ? -x : x;
}

int cross(int x1, int y1, int x2, int y2, int x3, int y3)
{
    return abs((x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1));
}

bool isInt(double d)
{
    return abs(d - round(d)) < 1e-9;
}

int main()
{  
    
    int C;
    scanf("%d", &C);
    for (int test = 1; test <= C; ++test)
    {
        scanf("%d %d %d", &N, &M, &A);
        bool solved = false;
        
        for (int i = 1; i <= N && !solved; ++i)
        {
            if (M * i >= A)
            {
                for (int x = 0; x <= N; ++x)
                    for (int y = 0; y <= M && !solved; ++y)
                        if (cross(0, 0, i, 0, x, y) == A)
                        {
                            printf("Case #%d: %d %d %d %d %d %d\n", test, 0, 0, i, 0, x, y);
                            solved = true;
                        }
            }
        }
        
        if (solved) continue;
    
        for (int x1 = 0; x1 <= N  && !solved; ++x1)
            for (int y2 = 0; y2 <= M && !solved; ++y2)
            {
                for (int x = 1; x <= N; ++x)
                    for (int y = 1; y <= M && !solved; ++y)
                        if (cross(x1, 0, 0, y2, x, y) == A)
                        {
                            printf("Case #%d: %d %d %d %d %d %d\n", test, x1, 0, 0, y2, x, y);
                            solved = true;
                        }
            }
        
        
        if (!solved)
            printf("Case #%d: IMPOSSIBLE\n", test);
    }

	return 0;
}
