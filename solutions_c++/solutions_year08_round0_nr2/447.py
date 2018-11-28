#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

struct data
{
    int h;
    int m;
    int i;
    int d;
};

bool myfun (data i, data j)
{
    return ((i.h < j.h) || (i.h == j.h && (i.m < j.m || (i.m == j.m && i.d > j.d))));
}

void addMinutes(data &d, int m)
{
    d.m += m;
    if (d.m >= 60)
    {
        d.m -= 60;
        ++d.h;
    }
}

int main()
{
    int n, na, nb, i, j, c, t;
    int an[2], ac[2];
    data ad[400];
    char ch;

    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    if (fin.fail())
        exit(1);
    fout.open("out.txt");

    fin >> n;

    for (int tt = 1; tt <= n; ++tt)
    {
        fin >> t;
        fin >> na >> nb;

        j = 0;
        for (i = 0; i < na; ++i)
        {
            fin >> ad[j].h;
            fin >> ch;
            fin >> ad[j].m;
            ad[j].i = 0;
            ad[j].d = -1;
            ++j;

            fin >> ad[j].h;
            fin >> ch;
            fin >> ad[j].m;
            addMinutes(ad[j], t);
            ad[j].i = 1;
            ad[j].d = 1;
            ++j;
        }
        for (i = 0; i < nb; ++i)
        {
            fin >> ad[j].h;
            fin >> ch;
            fin >> ad[j].m;
            ad[j].i = 1;
            ad[j].d = -1;
            ++j;

            fin >> ad[j].h;
            fin >> ch;
            fin >> ad[j].m;
            addMinutes(ad[j], t);
            ad[j].i = 0;
            ad[j].d = 1;
            ++j;
        }

        c  = na+na+nb+nb;
        sort(ad, ad+c, myfun);

        memset(an, 0, sizeof(int) * 2);
        memset(ac, 0, sizeof(int) * 2);

        for (i = 0; i < c; ++i)
        {
            an[ad[i].i] += ad[i].d;
            if (an[ad[i].i] < 0)
            {
                ++an[ad[i].i];
                ++ac[ad[i].i];
            }
        }

        fout << "Case #" << tt << ": " << ac[0] << " " << ac[1] << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
