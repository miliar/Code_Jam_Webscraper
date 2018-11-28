#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

enum
{
    TR_AB,
    TR_BA,
};

typedef struct Trip
{
    int     start;
    int     end;
    int     type;

    friend bool operator<(const struct Trip &p, const struct Trip &q);

} trip_t;

bool operator<(const struct Trip &p, const struct Trip &q)
{
    return p.start > q.start;
}




void
zestaw()
{
    vector<trip_t>  req_ab;
    vector<trip_t>  req_ba;

    vector<trip_t>  reqd;

    vector<trip_t>  ava_ab;
    vector<trip_t>  ava_ba;

    int     turn;
    int     nab, nba;

    int     res_a = 0, res_b = 0;
    static int  count = 1;

    scanf("%d %d %d", &turn, &nab, &nba);

    for (int it = 0; it < nab; ++it)
    {
        int     h, m;
        trip_t  tr;

        scanf("%d:%d", &h, &m);
        tr.start = h * 60 + m;
        scanf("%d:%d", &h, &m);
        tr.end = h * 60 + m;

        tr.type = TR_AB;

        req_ab.push_back(tr);

        reqd.push_back(tr);
    }

    for (int it = 0; it < nba; ++it)
    {
        int     h, m;
        trip_t  tr;

        scanf("%d:%d", &h, &m);
        tr.start = h * 60 + m;
        scanf("%d:%d", &h, &m);
        tr.end = h * 60 + m;

        tr.type = TR_BA;

        req_ba.push_back(tr);

        reqd.push_back(tr);
    }

    make_heap(req_ab.begin(), req_ab.end());
    make_heap(req_ba.begin(), req_ba.end());

    make_heap(reqd.begin(), reqd.end());

//    printf("%d:%d %d:%d\n", req_ab[0].start/60, req_ab[0].start%60, req_ab[0].end/60, req_ab[0].end%60);

//    if (!req_ab.empty())
//    {
//        ava_ab.push_back(req_ab[0]);
//    }
//    if (!req_ba.empty())
//    {
//        ava_ba.push_back(req_ba[0]);
//    }


    while(true)
    {
        if (!reqd.empty())
        {
            if (reqd[0].type == TR_AB)
            {
                if (ava_ab.empty())
                {
//printf("No ready train from A\n");
                    /* nie ma wolnych A->B */
                    ++res_a;
                }
                else
                {
                    if (ava_ab[0].start <= reqd[0].start)
                    {
//printf("Available train from A: %02d:%02d / ready from %02d:%02d\n", reqd[0].start / 60, reqd[0].start % 60, ava_ab[0].start / 60, ava_ab[0].start % 60);
                        /* jest wolny gotowy A->B */
                        /* usun z available */
                        pop_heap(ava_ab.begin(), ava_ab.end());
                        ava_ab.pop_back();
                    }
                    else
                    {
//printf("Train not ready from A: %02d:%02d / ready from %02d:%02d\n", reqd[0].start / 60, reqd[0].start % 60, ava_ab[0].start / 60, ava_ab[0].start % 60);

                        /* jest wolny ale nie gotowy */
                        ++res_a;
                    }
                }

                /* przesun go do ava_ba */
                trip_t  tr;
                tr = reqd[0];
                tr.start = tr.end + turn;
                ava_ba.push_back(tr);
                push_heap(ava_ba.begin(), ava_ba.end());

                /* usun z reqd */
                pop_heap(reqd.begin(), reqd.end());
                reqd.pop_back();

            }
            else
            {
                if (ava_ba.empty())
                {
//printf("No ready train from B\n");
                    /* nie ma wolnych B->A */
                    ++res_b;
                }
                else
                {
                    if (ava_ba[0].start <= reqd[0].start)
                    {
//printf("Available train from B: %02d:%02d / ready from %02d:%02d\n", reqd[0].start / 60, reqd[0].start % 60, ava_ba[0].start / 60, ava_ba[0].start % 60);
                        /* jest wolny gotowy B->A */
                        pop_heap(ava_ba.begin(), ava_ba.end());
                        ava_ba.pop_back();
                    }
                    else
                    {
//printf("Train not ready from B: %02d:%02d / ready from %02d:%02d\n", reqd[0].start / 60, reqd[0].start % 60, ava_ba[0].start / 60, ava_ba[0].start % 60);
                        /* jest wolny ale nie gotowy */
                        ++res_b;
                    }
                }

                /* przesun go do ava_ab */
                trip_t  tr;
                tr = reqd[0];
                tr.start = tr.end + turn;
                ava_ab.push_back(tr);
                push_heap(ava_ab.begin(), ava_ab.end());

                /* usun z reqd */
                pop_heap(reqd.begin(), reqd.end());
                reqd.pop_back();

            }
        }
        else
        {
            break;
        }
    }

    printf("Case #%d: %d %d\n", count++, res_a, res_b);
}

int
main()
{
    int     ile;

    scanf("%d", &ile);

    while(ile--)
    {
        zestaw();
    }

    return 0;
}
