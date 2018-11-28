#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <sys/time.h>

using namespace std;
typedef unsigned long u32;
typedef unsigned long long u64;
typedef signed long s32;

#pragma pack(0)

typedef struct
{
    u32 I;
    u32 Pos;
    u32 Speed;
} Chicken;

int main()
{
    u32 c;
    cin >> c;

    for(u32 cs = 1; cs <= c; ++cs)
    {
        u32 n, k, b, t;
        string positions, speeds;
        cin >> n >> k >> b >> t;

        Chicken chicks[n];
        for(u32 i = 0; i < n; ++i)
        {
            chicks[i].I = i;
            cin >> chicks[i].Pos;
        }

        u32 canReach = 0;
        for(u32 i = 0; i < n; ++i)
        {
            cin >> chicks[i].Speed;

            if(chicks[i].Speed * t >= (b - chicks[i].Pos))
                ++canReach;
        }

        if(canReach < k)
        {
            cout << "Case #" << cs << ": IMPOSSIBLE" << endl;
            continue;
        }

        Chicken best[k];
        u32 chicks_pos = (n-1);
        for(u32 i = 0; i < k; ++i)
        {
            while(chicks[chicks_pos].Speed * t < (b - chicks[chicks_pos].Pos))
                --chicks_pos;

            best[i].I = chicks[chicks_pos].I;
            best[i].Pos = chicks[chicks_pos].Pos;
            best[i].Speed = chicks[chicks_pos].Speed;
            --chicks_pos;
        }

        u32 swaps = 0;
        for(u32 i = 0; i < k; ++i)
        {
            u32 dist = n - 1 - best[i].I - i;
            swaps += dist;
        }

        cout << "Case #" << cs << ": " << swaps << endl;
    }

    return 0;
}
