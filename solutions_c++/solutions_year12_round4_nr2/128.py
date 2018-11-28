#include <iostream>
#include <fstream>
#include <ctime>
#include <algorithm>

using namespace std;
typedef long long ll;

ifstream fin ("blah.in");
ofstream fout ("blah.txt");

int main()
{
    srand (time (NULL));
    int ntest; fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
        int n;
        ll w, l;
        pair <ll, int> r[1100];
        fin >> n >> w >> l;
        for (int i = 0; i < n; i++)
        {
            fin >> r[i].first;
            r[i].second = i;
        }
        sort (r, r + n);
        ll x[1100], y[1100];
        int count = 0, hmax = 0;
        while (count < n)
        {
            ll sum = r[count].first;
            x[count] = 0;
            if (hmax == 0)
                y[count] = 0;
            else
                y[count] = hmax + r[count].first;
            int next = count + 1;
            while (next < n)
            {
                if (sum + r[next].first <= w)
                {
                    x[next] = sum + r[next].first;
                    if (hmax == 0)
                        y[next] = 0;
                    else
                        y[next] = hmax + r[next].first;
                    sum += 2 * r[next].first;
                    next++;
                }
                else
                    break;
            }
            hmax = y[next-1] + r[next-1].first;
            for (int i = count; i < next; i++)
                y[i] = y[next-1];
            count = next;
        }
        
        /*bool good = true, good2 = true;
        for (int i = 0; i < n; i++)
        {
            if (!(0 <= x[i] && x[i] <= w && 0 <= y[i] && y[i] <= l))
                good = false;
            for (int j = i + 1; j < n; j++)
            {
                if ((x[j] - x[i]) * (x[j] - x[i]) + (y[j] - y[i]) * 
                    (y[j] - y[i]) < (r[i].first + r[j].first) * (r[i].first + r[j].first))
                    good2 = false;
            }
        }
        if (!good)
            fout << "DANR\n";
        if (!good2)
            fout << "NADIR\n";*/
        
        ll ansx[1100], ansy[1100];
        for (int i = 0; i < n; i++)
        {
            ansx[r[i].second] = x[i];
            ansy[r[i].second] = y[i];
        }
        fout << "Case #" << test + 1 << ": ";
        for (int i = 0; i < n; i++)
        {
            fout << ansx[i] << " " << ansy[i];
            if (i < n - 1)
                fout << " ";
        }
        fout << "\n";
    }
    //system ("Pause");
    return 0;
}
