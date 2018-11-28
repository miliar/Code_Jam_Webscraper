#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

struct robot
{
    int position, time;
};

robot O;
robot B;

int main()
{
    int T, N;
    
    scanf("%d", &T);
    for (int C = 1; C <= T; C++)
    {
        O.position = 1;
        O.time = 0;
        B.position = 1;
        B.time = 0;

        char r; int destination, dist;

        scanf("%d ", &N);
        for (int i = 0; i < N; i++)
        {
            scanf("%c%d ", &r, &destination);
            if (r == 'O')
            {
                dist = abs(O.position - destination) + 1;
                O.time = max(O.time + dist, B.time + 1);
                O.position = destination;
            }
            else if (r == 'B')
            {
                dist = abs(B.position - destination) + 1;
                B.time = max(B.time + dist, O.time + 1);
                B.position = destination;
            }
        }
        
        printf("Case #%d: %d\n", C, max(O.time, B.time));
    }
    
    return 0;
}
