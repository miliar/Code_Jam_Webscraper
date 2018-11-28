#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

int vec[25];

bool test(int n)
{
    while(true)
    {
        if(n == 1)
            return true;
        
        if(vec[n] == -1)
            return false;
        
        n = vec[n];
    }
}



int answers[25];


int main(int argc, char** argv)
{
    int C;
    
    scanf("%d", &C);
    
    for(int n = 2; n < 26; ++n)
    {
        
        int ans = 0;
        
        for(int i = 2; i < (1<<n); i += 2)
        {
            int counter = 1;
            int backup = i;
            int rank = 1;
            
            for(int j = 0; j <= 25; ++j)
                vec[j] = -1;
            
            while(backup)
            {
                if((backup&1) == 1)
                {
                    vec[counter] = rank++;
                }
                
                backup >>= 1;
                ++counter;
            }
            
            if(vec[n] == -1)
                continue;
            
            ans += test(n);
        }
        
        answers[n] = ans;
//         printf("%d %d\n", n, answers[n]); 
    }
    
    for(int c = 1; c <= C; ++c)
    {
        printf("Case #%d: ", c);
        int n;
        scanf("%d", &n);
        
        printf("%d\n", answers[n] % 100003);
    }
        
    return 0;
}