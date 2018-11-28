#include <cstdio>

using namespace std;

int T;

int N, K;

char s_on[3] = "ON";
char s_off[4] = "OFF";


char* state(bool s)
{
    if(!s)
        return s_on;

    return s_off;
}

int main(int argc, char** argv)
{
    scanf("%d", &T);
    
    for(int c = 1; c <= T; ++c)
    { 
        scanf("%d %d", &N, &K);
        
        int pow = (1 << N);
        int kp1 = K + 1;
//         printf("%d %d %d %d\n", N, K, pow, kp1);
        printf("Case #%d: %s\n", c, state(kp1%pow));
    }
    
    return 0;
}