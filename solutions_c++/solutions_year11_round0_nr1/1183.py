#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>

using namespace std;

struct bot
{
    char color;
    int pos;
};

queue<bot> tot;
queue<bot> o;
queue<bot> b;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, cases = 0;
    int seq;
    char color;
    int p;
    bot temp, temp1, temp2;
    int curO, curB;
    int seconds;
    int step;

    scanf("%d", &T);

    while (cases++ < T)
    {
        while(!tot.empty()) tot.pop();
        while(!o.empty()) o.pop();
        while(!b.empty()) b.pop();

        curO = 1;
        curB = 1;
        seconds = 0;
        scanf("%d", &seq);
        for (int i = 0; i < seq; i++)
        {
            scanf(" %c %d", &color, &p);
            temp.color = color;
            temp.pos = p;
            tot.push(temp);
            if (color == 'O') o.push(temp);
            if (color == 'B') b.push(temp);
        }
        while (!tot.empty() && !o.empty() && !b.empty())
        {
            temp = tot.front();
            temp1 = o.front();
            temp2 = b.front();
            if (temp.color == 'O')
            {
                step = fabs(temp.pos - curO);
                seconds += step + 1;
                curO = temp.pos;
                if (fabs(temp2.pos - curB) < step + 1)
                {
                    curB = temp2.pos;
                }
                else
                {
                    if (temp2.pos - curB > 0)
                    {
                        curB += step + 1;
                    }
                    else if (temp2.pos - curB < 0)
                    {
                        curB -= (step + 1);
                    }
                }
                tot.pop();
                o.pop();
//                printf("O moves to %d and press button, B moves to %d\n", curO, curB);
//                printf("Seconds + %d\n", step + 1);
            }
            if (temp.color == 'B')
            {
                step = fabs(temp.pos - curB);
                seconds += step + 1;
                curB = temp.pos;
                if (fabs(temp1.pos - curO) < step + 1)
                {
                    curO = temp1.pos;
                }
                else
                {
                    if (temp1.pos - curO > 0)
                    {
                        curO += step + 1;
                    }
                    else if (temp1.pos - curO < 0)
                    {
                        curO -= (step + 1);
                    }
                }
                tot.pop();
                b.pop();
//                printf("B moves to %d and press button, O moves to %d\n", curB, curO);
//                printf("Seconds + %d\n", step + 1);
            }
        }
        while(!o.empty())
        {
            temp1 = o.front();
            step = fabs(temp1.pos - curO);
            seconds += fabs(temp1.pos - curO) + 1;
            curO = temp1.pos;
            o.pop();
//            printf("O moves to %d and press button\n", curO);
//            printf("Seconds + %d\n", step + 1);
        }
        while(!b.empty())
        {
            temp2 = b.front();
            step = fabs(temp2.pos - curB);
            seconds += fabs(temp2.pos - curB) + 1;
            curB = temp2.pos;
            b.pop();
//            printf("B moves to %d and press button\n", curB);
//            printf("Seconds + %d\n", step + 1);
        }
        printf("Case #%d: %d\n", cases, seconds);
    }
}

