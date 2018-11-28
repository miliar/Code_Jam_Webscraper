#include <iostream>
#include <fstream>

using namespace std;

int w, h;
int in[100][100];
int ot[100][100];
char output[100][100];

ofstream outs ("output.txt");
#define cout outs

ifstream ins ("input.txt");
#define cin ins

struct point {int h, i, j;};

point findHighest(int w,int h)
{
    point r;
    r.h = 0;
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++)
            if (in[i][j] > r.h && in[i][j] != 999999)
            {
                r.h = in[i][j];
                r.i = i;
                r.j = j;
            }

    return r;
}

point findNeigh (point a)
{
    point r;
    r.h = 999999;

    if (a.i-1 >= 0 && in[a.i-1][a.j] != 999999)
    {
        r.h = in[a.i-1][a.j];
        r.i = a.i-1;
        r.j = a.j;
    }

    if (in[a.i][a.j-1] < r.h && a.j-1 >= 0 && in[a.i][a.j-1] != 999999)
    {
        r.h = in[a.i][a.j-1];
        r.i = a.i;
        r.j = a.j-1;
    }

    if (in[a.i][a.j+1] < r.h && a.j+1 < h && in[a.i][a.j+1] != 999999)
    {
        r.h = in[a.i][a.j+1];
        r.i = a.i;
        r.j = a.j+1;
    }

    if (in[a.i+1][a.j] < r.h && a.i+1 < w && in[a.i+1][a.j] != 999999)
    {
        r.h = in[a.i+1][a.j];
        r.i = a.i+1;
        r.j = a.j;
    }

    return r;
}

void connectPoint (point f, point t)
{
    int change = ot[t.i][t.j];
    int to = ot[f.i][f.j];
    in[f.i][f.j] = 999999;
    if (t.h == 999999 || t.h == f.h)
        return;
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++)
            if (ot[i][j] == change)
                ot[i][j] = to;
}

int findNext ()
{
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++)
            if ( ot[i][j] != 999999)
                return ot[i][j];
    return 999999;
}

void fillthi (int a, int b)
{
    for (int i = 0; i < w; i++)
        for (int j = 0; j < h; j++)
            if ( ot[i][j] == a)
            {
                ot[i][j] = 999999;
                output[i][j] = 'a' + (char)b;
            }
    return;
}

int main()
{
    int n;
    point f, t;
    cin >> n >> w >> h;
    for (int z = 1; z <= n; z++)
    {
        for (int i = 0; i < w; i++)
            for (int j = 0; j < h; j++)
            {
                cin >> in[i][j];
                ot[i][j] = (i*h) + j;
                output[i][j] = '-';
            }
        for (int i = 0; i < w*h; i++)
        {
            f = findHighest (w, h);
            t = findNeigh (f);
            connectPoint(f, t);
        }

        int thi = ot[0][0];
        int q = 0;
        while (thi != 999999)
        {
            fillthi (thi, q);
            q++;
            thi = findNext();
        }

        cout << "Case #" << z << ":" << endl;

        for (int i = 0; i < w; i++)
        {
            for (int j = 0; j < h; j++)
                cout << output[i][j] << " ";
            cout << endl;
        }

        cin >> w >> h;
    }
    return 0;
}
