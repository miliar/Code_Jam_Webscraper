// Robots.cpp

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ASSERT(x)  {if(!(x)) __asm{int 3};}
typedef __int64 LONG;

#define ABS(x) ((x) >= 0? (x) : (0-(x)))
#define MAXN 100

typedef struct _Button
{
    char robot;
    int  pos;
    int time;
}Button;

Button buttons[MAXN];

int solve(int n)
{
    int i ;
    int lastOrange = 1, lastOrangeTime = 0;
    int lastBlue = 1, lastBlueTime = 0;
    for(i = 0 ; i < n; i++)
    {
        ASSERT(buttons[i].pos > 0 && buttons[i].robot > 1 && buttons[i].time == (-1));
        if(buttons[i].robot == 'O')
        {
            buttons[i].time = lastOrangeTime + ABS(buttons[i].pos - lastOrange) +1;
            lastOrange = buttons[i].pos;
            lastOrangeTime = buttons[i].time;
        }
        else
        {
            ASSERT(buttons[i].robot == 'B');
            buttons[i].time = lastBlueTime + ABS(buttons[i].pos - lastBlue) +1;
            lastBlue = buttons[i].pos;
            lastBlueTime = buttons[i].time;
        }
    }
    int orangeOffset = 0;
    int blueOffset = 0;
    for( i=1 ; i< n ; i++)
    {
        ASSERT(buttons[i].pos > 0 && buttons[i].robot > 1 && buttons[i].time > 0);
        if(buttons[i].robot == 'O')
        {
            buttons[i].time += orangeOffset;
            if(buttons[i].time <= buttons[i-1].time)
            {
                ASSERT(buttons[i].robot != buttons[i-1].robot);
                orangeOffset += buttons[i-1].time+1 - buttons[i].time;
                buttons[i].time = buttons[i-1].time+1;
            }
        }
        else
        {
            buttons[i].time += blueOffset;
            if(buttons[i].time <= buttons[i-1].time)
            {
                ASSERT(buttons[i].robot != buttons[i-1].robot);
                blueOffset += buttons[i-1].time+1 - buttons[i].time;
                buttons[i].time = buttons[i-1].time+1;
            }
        }
        ASSERT(orangeOffset >= 0 && blueOffset >= 0);
        ASSERT(buttons[i].time > 0);
    }
    return buttons[n-1].time;
}

int main(int argc, const char* argv[])
{
    int T = 0 ,N = 0;
    int ret;
    int i;
    int result = 0;
    int caseIndex = 1;
    ret = scanf("%d", &T);
    ASSERT(ret != EOF && T > 0 && T<=100);
    while(T--)
    {
        char c[2];
        memset(buttons, 0xff, sizeof(buttons));
        scanf("%d", &N);
        ASSERT(N >= 1 && N <= 100);
        for(i = 0; i<N ;i++)
        {
            scanf("%s%d", c, &buttons[i].pos);
            buttons[i].robot = c[0];
            ASSERT(ret != EOF);
        }
        result = solve(N);
        ASSERT(result > 0);
        printf("Case #%d: %d\n", caseIndex++, result);
    }
	return 0;
}

