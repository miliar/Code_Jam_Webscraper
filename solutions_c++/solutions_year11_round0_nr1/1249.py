#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
    int C;
    scanf("%d", &C);
    for(int c = 1; c <= C; ++c)
    {
        printf("Case #%d: ", c);
        
        long long Pi[2];
        Pi[0] = Pi[1] = 1;
        
        long long Ti[2];
        Ti[0] = Ti[1] = 0;
        
        int N;
        scanf("%d ", &N);
        
        for(int i = 0; i < N; ++i)
        {
            char robot;
            int button;
            scanf("%c %d ", &robot, &button);
            
            int this_robot = 0;
            int other_robot = 1;
            
            if(robot == 'B')
            {
                this_robot = 1;
                other_robot = 0;
            }
            
            long long distance = fabs(Pi[this_robot] - (long long)button);
            
            Pi[this_robot] = button;
            Ti[this_robot] = max(Ti[other_robot] + 1, Ti[this_robot] + distance + 1);
        }
        
        printf("%lld\n", max(Ti[0], Ti[1]));
    }
    return 0;
}