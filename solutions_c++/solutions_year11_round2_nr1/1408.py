#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#define nabs(x) (x)<0?(-(x)):(x)
using namespace std;

#define N 105

struct node
{
    string cres;
    int nwin;
    int nlose;
    double wp;
    double owp;
    double oowp;
};

int main()
{
    int t, k;
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &t);
    for(k = 1; k <= t; ++k)
    {
        printf("Case #%d:\n", k);
        int n, i, j;

        struct node sn[N];
        scanf("%d", &n);
        for(i = 0; i < n; ++i)
        {
            cin >> sn[i].cres;
            for(sn[i].nwin = sn[i].nlose = j = 0; j < sn[i].cres.size(); ++j)
            {
                if(sn[i].cres[j] == '1')
                    ++sn[i].nwin;
                if(sn[i].cres[j] == '0')
                    ++sn[i].nlose;
            }
            sn[i].wp = double(1.0 * sn[i].nwin / (sn[i].nwin + sn[i].nlose));
        }
        int count;
        double sum;
        for(i = 0; i < n; ++i)
        {
            for(count = j = 0, sum = 0.0; j < sn[i].cres.size(); ++j)
            {
                if(sn[i].cres[j] != '.')
                {
                    if(sn[i].cres[j] == '1')
                        sum += double(sn[j].nwin) / (sn[j].nwin + sn[j].nlose - 1);
                    else
                        sum += double(sn[j].nwin - 1) / (sn[j].nwin + sn[j].nlose - 1);
                    ++count;
                }
            }
            sn[i].owp = sum / count;
        }
        for(i = 0; i < n; ++i)
        {
            for(count = j = 0, sum = 0.0; j < sn[i].cres.size(); ++j)
            {
                if(sn[i].cres[j] != '.')
                {
                    ++count;
                    sum += sn[j].owp;
                }
            }
            sn[i].oowp = sum / count;
        }
        for(i = 0; i < n; ++i)
            cout << 0.25 * sn[i].wp + 0.50 * sn[i].owp + 0.25 * sn[i].oowp << endl;
    }
    return 0;
}
