#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char Input[30];

int main()
{
    int n, count = 1;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++)
    {
        scanf("%s", Input);
        int len = strlen(Input);
        if(next_permutation(Input, Input+len))
        {
            printf("Case #%d: %s\n", count, Input);        
        }
        else
        {
            int zeroCount = 0;
            sort(Input, Input+len);            
            for(int i = 0; i < len; i++)
            {
                if(Input[i] == '0') zeroCount++;
                else break;
            }
            printf("Case #%d: %c0", count, Input[zeroCount]);
            for(int i = 0; i < zeroCount; i++)
            {
                putchar('0');
            }
            for(int i = zeroCount+1; i < len; i++)
            {
               putchar(Input[i]);
            }
            putchar('\n');
        }
        count++;
    }
    return 0;
}

            
                                   
    
