#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <math.h>

#define Pi acos(-1.0)
#define INT_MAX 2147000000
#define INF 1000000
#define mp make_pair
#define pb push_back

#define EPS 1e-13

using namespace std;

struct rec
{
    double r;
    int num;
};

bool cmp(rec a, rec b)
{
    return a.r > b.r;
}

rec b[100000];

int n;
double w, l;
double r[100000];
double ansx[100000], ansy[100000], ansx1[100000], ansy1[100000];
bool canuse[100000];



int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++)
    {
        cin >> n >> w >> l;
        memset(canuse, 1, sizeof(canuse));
        memset(b, 0, sizeof(b));
        memset(ansx, 0, sizeof(ansx));
        memset(ansy, 0, sizeof(ansy));
        memset(r, 0, sizeof(r));

        for (int i = 0; i < n; i++)
        {
            cin >> b[i].r;
            b[i].num = i;
        }
        sort(b, b + n, cmp);
        for (int i = 0; i < n; i++)
        {
            r[i] = b[i].r;
            canuse[i] = 1;
        }

        int i = 1;
        double prev = 0;
        ansx[0] = ansy[0] = 0;
        while (i < n &&  ansx[i - 1] + r[i - 1] + 2 * r[i] < w + r[i] + 1e-7)
        {
            ansx[i] = ansx[i - 1] + r[i - 1] + r[i];
            i++;
        }
        for (; i < n; i++)
        {
            double x = w - r[i], y = l - r[i];
            int v = 0;
            for (int j = 0; j < i; j++)
            {
                if (!canuse[j]) continue;
                double curx = max(ansx[j] - r[j], -r[i]), cury = ansy[j] + r[j];
                if (cury < y || (fabs(cury - y) < 1e-7 && curx < x))
                {
                    x = curx;
                    y = cury;
                    v = j;
                }
            }
            ansx[i] = x + r[i];
            ansy[i] = y + r[i];
            canuse[v] = 0;
        }

        cout.precision(40);
        cout << "Case #" << tc << ": ";

        for (int i = 0; i < n; i++)
        {
            ansx1[b[i].num] = ansx[i];
            ansy1[b[i].num] = ansy[i];
        }

        for (int i = 0; i < n; i++)
        {
            cout << ansx1[i] << " " << ansy1[i] << " ";
            if (ansx[i] > w || ansy[i] > l)
            {
                cout << "WA";
                return 0;
            }
        }

        cout << endl;

    }


    return 0;
}
