#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int count;
        scanf("%d", &count);
        int i;
        int pos1 = 1;
        int pos2 = 1;
        int time1 = 0;
        int time2 = 0;
        int currentTime = 0;
        for (i = 0; i < count; i++)
        {
            char s[10];
            int p;
            scanf("%s %d", s, &p);
            if (s[0] == 'O')
            {
                currentTime++;
                int cand = time1 + 1 + abs(p - pos1);
                if (cand > currentTime)
                    currentTime = cand;
                time1 = currentTime;
                pos1 = p;
            }
            else
            {
                currentTime++;
                int cand = time2 + 1 + abs(p - pos2);
                if (cand > currentTime)
                    currentTime = cand;
                time2 = currentTime;
                pos2 = p;
            }
        }
        printf("Case #%d: %d\n", t+1, currentTime);
    }
    return 0;
}
