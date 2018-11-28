#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <utility>
#include <math.h>
#include <set>
#include <map>

#define forn(i, n) for(int i = 0; i < n; i++)
#define VI vector<int>
#define PII pair<int, int>
#define fi first
#define se second
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define deb(a); cout << #a << " = " << a << endl;

using namespace std;

const int maxn = 500000;
const long long inf = 10000000000000000LL;
const double eps = 1.0e-7;

char A[200][200];
double Wp[200], Owp[200], Oowp[200], Wp2_v[200], Wp2_pr[200];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n = 0, m, k;
    int t = 0;
    scanf("%d", &t);
    forn(z, t)
    {
        printf("Case #%d:\n", z + 1);
        int n = 0;
        scanf("%d", &n);
        forn(i, n)
        {
            forn(j, n)
            {
                char x[3];
                scanf("%1s", x);
                A[i][j] = x[0];
            }
        }
        forn(i, n)
        {
            int sum_all = 0;
            int sum_v = 0;
            forn(j, n)
            {
                if(A[i][j] !='.')
                {
                    sum_all++;
                    if(A[i][j] == '1')
                        sum_v++;
                }
            }
            Wp[i] = (double)sum_v / sum_all;
            Wp2_v[i] = (double)(sum_v - 1) / (sum_all - 1);
            Wp2_pr[i] = (double)(sum_v) / (sum_all - 1);
           // printf("Wp - i = %d\n", i);
           // printf("%.9f %.9f\n", Wp2_v[i], Wp2_pr[i]);
        }
        forn(i, n)
        {
           // printf("O_Wp: i = %d\n", i);
            double sum_all = 0;
            int kol = 0;
            forn(j, n)
            {
                if(A[i][j] != '.')
                {
             //       printf("+%d ", j);
                    if(A[i][j] == '1')
                        sum_all += Wp2_pr[j];
                    else
                        sum_all += Wp2_v[j];
                    kol++;
                }
            }
           // printf("\n");
            Owp[i] = sum_all / kol;
        }
        forn(i, n)
        {
            double sum_all = 0;
            int kol = 0;
            forn(j, n)
            {
                if(A[i][j] != '.')
                {
                    sum_all += Owp[j];
                    kol++;
                }
            }
            Oowp[i] = sum_all / kol;
        }
        forn(i, n)
        {
            printf("%.9f\n", 0.25*Wp[i] + 0.5*Owp[i] + 0.25*Oowp[i]);
        }
    }

    return 0;
}
