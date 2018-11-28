#include <stdio.h>
#include <algorithm>
#define A 1
#define B 2
#define ARRIVE 1
#define DEPART 2

using namespace std;

class event
{
public:
    int hh, mm, s, e;

    event(): hh(0), mm(0), s(0), e(0) {};
    event(int thh, int tmm, int ts, int te) { hh = thh; mm = tmm; s = ts; e = te; };
};

event operator + (event a, int t)
{
    a.mm += t;
    if (a.mm >= 60)
    {
        a.mm -= 60;
        a.hh += 1;
    }
    return a;
}

bool operator < (event a, event b)
{
    if (a.hh < b.hh)
        return true;
    if (a.hh == b.hh && a.mm < b.mm)
        return true;
    if (a.hh == b.hh && a.mm == b.mm && a.e < b.e)
        return true;
    return false;
}

FILE *inf, *outf;
int n, t, na, nb, hh, mm;
event e[410];
int nt, w[3];
int answer[3];

int main()
{
    int l1, l2;

    inf = fopen("b.in", "r");
    outf = fopen("b.out", "w");
    fscanf(inf, "%d", &n);
    for (l1 = 1; l1 <= n; l1++)
    {
        fscanf(inf, "%d%d%d", &t, &na, &nb);
        for (l2 = 1; l2 <= na; l2++)
        {
            fscanf(inf, "%2d:%2d", &hh, &mm);
            e[l2] = event(hh, mm, A, DEPART);
            fscanf(inf, "%2d:%2d", &hh, &mm);
            e[na + l2] = event(hh, mm, B, ARRIVE) + t;
        }
        for (l2 = 1; l2 <= nb; l2++)
        {
            fscanf(inf, "%2d:%2d", &hh, &mm);
            e[na * 2 + l2] = event(hh, mm, B, DEPART);
            fscanf(inf, "%2d:%2d", &hh, &mm);
            e[na * 2 + nb + l2] = event(hh, mm, A, ARRIVE) + t;
        }
        nt = (na + nb) * 2;
        sort(e + 1, e + nt + 1);
        w[A] = w[B] = 0;
        answer[A] = answer[B] = 0;
        for (l2 = 1; l2 <= nt; l2++)
        {
            if (e[l2].e == ARRIVE)
                w[e[l2].s]++;
            else
            {
                if (w[e[l2].s] == 0)
                {
                    w[e[l2].s]++;
                    answer[e[l2].s]++;
                }
                w[e[l2].s]--;
            }
        }
        fprintf(outf, "Case #%d: %d %d\n", l1, answer[A], answer[B]);
    }
    return 0;
}
