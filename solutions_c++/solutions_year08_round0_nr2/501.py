
#include <cstdio>
#include <vector>
using namespace std;

const int MAXS = 128;

struct trip
{
    int departure;
    int arrival;
};

int t, na, nb;
char s [16];
bool mark [MAXS];
vector <trip> left, right;

inline int parse ()
{
    int h, m;
    scanf ("%d:%d", &h, &m);
    return h * 60 + m;
}
void solve ()
{
    int ra = na, rb = nb;
    for (int k = 0; k < 2; ++k)
    {
        memset (mark, 0, sizeof (mark));
        for (int j = 0; j < nb; ++j)
        {
            int id = -1;
            for (int i = 0; i < na; ++i)
                if (!mark [i] && (left [i].arrival + t <= right [j].departure))
                {
                    if (id == -1)
                        id = i;
                    else if (left [id].arrival < left [i].arrival)
                        id = i;
                }
            if (id >= 0)
            {
                mark [id] = true;
                --rb;
            }
        }
        swap (ra, rb);
        swap (na, nb);
        swap (left, right);
    }
    printf (" %d %d\n", ra, rb);
}
int main ()
{
    int N;
    scanf ("%d", &N);
    for (int i = 1; i <= N; ++i)
    {
        scanf ("%d %d %d", &t, &na, &nb);
        left.clear ();
        left.resize (na);
        for (int j = 0; j < na; ++j)
            left [j].departure = parse (), left [j].arrival = parse ();
        right.clear ();
        right.resize (nb);
        for (int j = 0; j < nb; ++j)
            right [j].departure = parse (), right [j].arrival = parse ();
        
        printf ("Case #%d:", i);
        solve ();
    }
    return 0;
}
