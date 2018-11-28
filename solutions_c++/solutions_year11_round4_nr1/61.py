#include <cstdio>
#include <complex>
#include <algorithm>
#include <vector>
using namespace std;

int X, S, R, N, B, E, W;
double run;

void solve_case ()
{
    scanf ("%d %d %d %lf %d", &X, &S, &R, &run, &N);
    vector <pair <int, int> > segments;
    double walk_time = 0;

    for (int i = 0; i < N; i++)
    {
        scanf ("%d %d %d", &B, &E, &W);
        segments.push_back (make_pair (S + W, E - B));
        walk_time += (double) (E - B) / (S + W);
        X -= E - B;
    }

    segments.push_back (make_pair (S, X));
    walk_time += (double) X / S;
    sort (segments.begin (), segments.end ());

    for (int i = 0; i < (int) segments.size (); i++)
    {
        double speed = segments [i].first, length = segments [i].second;
        double save = length / speed - length / (speed + R - S);

        if (run >= length / (speed + R - S))
        {
            run -= length / (speed + R - S);
            walk_time -= save;
        }
        else
        {
            double run_length = run * (speed + R - S);
            walk_time -= run_length / speed - run;
            break;
        }
    }

    printf ("%.9lf\n", walk_time);
}

int main ()
{
    int T; scanf ("%d", &T);

    for (int tc = 1; tc <= T; tc++)
    {
        printf ("Case #%d: ", tc);
        solve_case ();
    }

    return 0;
}
