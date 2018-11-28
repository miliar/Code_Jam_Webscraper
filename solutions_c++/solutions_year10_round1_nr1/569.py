#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

string a [100];
int maxsize = 0;

int main ()
{
    freopen ("A-small-attempt0.in", "r", stdin);
    freopen ("output.txt", "w", stdout);

    int T;
    scanf ("%d", &T);
    for (int t=0; t<T; t++)
    {
        int N, K, isR=0, isB=0;
        scanf ("%d %d", &N, &K);
        for (int n=0; n<N; n++)
        {
            char in [100];
            scanf ("%s", &in);
            string str = in;
            a[n] = "";
            for (int i=0; i<str.size(); i++) if (str.compare (i, 1, "R") == 0 || str.compare (i, 1, "B") == 0) a[n] += str.substr(i, 1);
                            //while (a[n].size() > 0 && a[n].compare (a[n].size() - 1, 1, ".") == 0) a[n] = a[n].substr (0, a[n].size() - 1);
            if (a[n].size() > maxsize) maxsize = a[n].size();
            //printf ("%s\n", a[n].c_str());
        }
        for (int n=0; n<N; n++)
        {
            while (a[n].size() < maxsize) a[n] = "." + a[n];
            //printf ("%s\n", a[n].c_str());
        }

int x,y;
        // vertical
        for (x=maxsize-1; x>0; x--) for (y=0; y<=N-K; y++)
        {
            int rb = 1, rr = 1;
            for (int k=0; k<K; k++)
            {
                if (a[y+k].compare (x, 1, ".") == 0)
                {
                    rr = 0;
                    rb = 0;
                }
                if (a[y+k].compare (x, 1, "R") == 0)
                {
                    rb = 0;
                }
                if (a[y+k].compare (x, 1, "B") == 0)
                {
                    rr = 0;
                }
            }
            if (rr == 1) isR = 1;
            if (rb == 1) isB = 1;
        }

        // horizontal
        for (x=maxsize-1; x>=K-1; x--) for (y=0; y<N; y++)
        {
            int rb = 1, rr = 1;
            for (int k=0; k<K; k++)
            {
                if (a[y].compare (x-k, 1, ".") == 0)
                {
                    rr = 0;
                    rb = 0;
                }
                if (a[y].compare (x-k, 1, "R") == 0)
                {
                    rb = 0;
                }
                if (a[y].compare (x-k, 1, "B") == 0)
                {
                    rr = 0;
                }
            }
            if (rr == 1) isR = 1;
            if (rb == 1) isB = 1;
        }
            //printf ("%s\n", a[0].substr (maxsize-1, 1).c_str());

        // diag \
        int x1=123, y1 = 234;
        //for (int x1=maxsize-1; x1>=K-1; x1--) for (int y1=0; y1<=N-K; y1++)
        for (int x=maxsize-1; x>=K-1; x--) for (int y=0; y<=N-K; y++)
        {
            //printf ("%d %d\n", x, y);
            //printf ("%s\n", a[y].substr (x, 1).c_str());
        //return 0;

            int rb = 1, rr = 1;
            for (int k=0; k<K; k++)
            {
                if (a[y+k].compare (x-k, 1, ".") == 0)
                {
                    rr = 0;
                    rb = 0;
                }
                if (a[y+k].compare (x-k, 1, "R") == 0)
                {
                    rb = 0;
                }
                if (a[y+k].compare (x-k, 1, "B") == 0)
                {
                    rr = 0;
                }
            }
            if (rr == 1) isR = 1;
            if (rb == 1) isB = 1;
        }

        // vertical
        for (x=maxsize-K-2; x>0; x--) for (y=0; y<=N-K; y++)
        {
            int rb = 1, rr = 1;
            for (int k=0; k<K; k++)
            {
                if (a[y+k].compare (x+k, 1, ".") == 0)
                {
                    rr = 0;
                    rb = 0;
                }
                if (a[y+k].compare (x+k, 1, "R") == 0)
                {
                    rb = 0;
                }
                if (a[y+k].compare (x+k, 1, "B") == 0)
                {
                    rr = 0;
                }
            }
            if (rr == 1) isR = 1;
            if (rb == 1) isB = 1;
        }
        printf ("Case #%d: ", t+1);
        if (isR == 0 && isB == 0) printf ("Neither\n");
        else if (isR == 0 && isB == 1) printf ("Blue\n");
        else if (isR == 1 && isB == 0) printf ("Red\n");
        else if (isR == 1 && isB == 1) printf ("Both\n");
    }

    return 0;
}
