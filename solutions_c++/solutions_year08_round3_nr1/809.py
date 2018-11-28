#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int nb_tests;
long long P, K, L, aux, cnt = 1, rez, sum;
vector<int> v;

int main()
{
    FILE *fin = fopen("A.in", "r");
    FILE *fout = fopen("A.out", "w");
    fscanf(fin, "%d", &nb_tests);
    for (int t = 1; t <= nb_tests; ++t)
    {
        fscanf(fin, "%lld%lld%lld", &P, &K, &L);
        v.clear();
        cnt = 1;
        rez = 0;
        sum = 0;
        for (int i = 0; i < L; ++i)
        {
            fscanf(fin, "%d", &aux);
            v.push_back(aux);
        }
        sort(v.begin(), v.end());
        for (int i = L-1; i >= 0 && P; i -= K)
        {
            sum = 0;
            for (int j = i; j > i-K && j >= 0; --j)
                sum += v[j];
            rez += (sum * cnt);
            P--;
            cnt++;
        }
        fprintf(fout, "Case #%d: %lld", t, rez);
        if (t != nb_tests)
            fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
    
    return 0;
}
