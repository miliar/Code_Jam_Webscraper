#include <cstdio>
#include <algorithm>

using namespace std;

/// suprising, value
int highest[2][31];

int scores[101];

int main(int argc, char** argv)
{
    for(int a = 0; a <= 10; ++a)
        for(int b = a; b <= 10; ++b)
            for(int c = b; c <= 10; ++c)
            {
                if(c - a > 2)
                    break;
                
                bool surprising = (c - a == 2);
                int sum = a + b + c;
                highest[surprising][sum] = c;
            }
            
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        int N, S, p;
        scanf("%d %d %d", &N, &S, &p);
        for(int i = 0; i < N; ++i)
            scanf("%d", scores + i);
        
        sort(scores, scores + N);
        
        int answer = 0;
        for(int i = 0; i < N; ++i)
        {
            int sum = scores[i];
            if(highest[false][sum] >= p)
            {
                ++answer;
            }
            else if(highest[true][sum] >= p && S > 0)
            {
                ++answer;
                --S;
            }
        }
        
        printf("Case #%d: %d\n", t, answer);
        
    }
    
    return 0;
}