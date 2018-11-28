// Robots.cpp

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ASSERT(x)  {if(!(x)) __asm{int 3};}
typedef __int64 LONG;

int main(int argc, const char* argv[])
{
    int T = 0 ,N = 0;
    int ret;
    int result = 0;
    int caseIndex = 1;
    ret = scanf("%d", &T);
    ASSERT(ret != EOF && T > 0 && T<=100);
    while(T--)
    {
        scanf("%d", &N);
        int xor = 0;
        int sum = 0;
        int minvalue = 1000000+1;
        int x;
        while(N--)
        {
            scanf("%d", &x);
            xor ^=x;
            sum +=x;
            if(x < minvalue)
                minvalue = x;
        }
        if(xor == 0)
            printf("Case #%d: %d\n", caseIndex++, sum - minvalue);
        else
            printf("Case #%d: NO\n", caseIndex++);
    }
	return 0;
}

