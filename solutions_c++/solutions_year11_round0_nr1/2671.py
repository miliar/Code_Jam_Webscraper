#include <cstdio>
#include <cstring>

struct Seq
{
    int pos;
    int num;
};

Seq O[100];
Seq B[100];

int abssub(int x)
{
    return x > 0 ? x : -x;
}

int main()
{
    int T, N;
    char str[2];

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    scanf("%d", &T);
    int cnt = 0;
    while(T--)
    {
        cnt++;
        scanf("%d", &N);

        int co= 0, cb = 0;

        for(int i = 0; i < N; ++ i)
        {
            scanf("%s", str);
            if(str[0] == 'O')
            {
                scanf("%d", &(O[co].pos));
                O[co++].num = i;
            }
            else
            {
                scanf("%d", &(B[cb].pos));
                B[cb++].num = i;
            }
        }

        int lo=0, lb=0;
        int po = 1, pb = 1;
        int ret = 0, interval = 0;
        while(lo < co && lb < cb)
        {
            if(O[lo].num < B[lb].num)
            {
                if(O[lo].pos == po) interval = 1;
                else interval = abssub(O[lo].pos - po) + 1;
                po = O[lo].pos;

                if(interval >= abssub(B[lb].pos - pb))
                {
                    pb = B[lb].pos;
                }
                else
                {
                    pb = B[lb].pos - pb > 0 ? pb + interval : pb - interval;
                }
                lo++;
            }
            else if(O[lo].num > B[lb].num)
            {
                if(B[lb].num == pb) interval = 1;
                else interval = abssub(B[lb].pos - pb) + 1;

                pb = B[lb].pos;

                if(interval >= abssub(O[lo].pos - po))
                {
                    po = O[lo].pos;
                }
                else
                {
                    po = O[lo].pos - po > 0 ? po + interval : po - interval;
                }
                lb ++;
            }

            ret += interval;
        }

        if(lo < co)
        {
            while(lo < co)
            {
                ret += abssub(O[lo].pos - po) + 1;
                po = O[lo].pos;
                lo++;
            }
        }
        else if(lb < cb)
        {
            while(lb < cb)
            {
                ret += abssub(B[lb].pos - pb) + 1;
                pb = B[lb].pos;
                lb++;
            }
        }

        printf("Case #%d: %d\n", cnt, ret);
    }
}
