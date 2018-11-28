#include<cstdio>
#include<cstdlib>
#include<cstring>

long long revenue(int R, int k, int N, int g[])
{
        long long euros = 0;
        int pivot = 0;
        do
        {
                int residue = k;
                int count = 0;
                int first = pivot;
                while (g[pivot] <= residue)
                {
                        if (pivot == first && count > 0) break;
                        residue -= g[pivot];
                        ++count;
                        ++pivot;
                        if (pivot == N) pivot = 0;
                }
                euros += k - residue;
        } while (--R);
        return euros;
}

int main(int argc, char **argv)
{
        int T, R, k, N;
        int g[1024];
        fscanf(stdin, "%d", &T);
        for (int i = 0; i < T; ++i) 
        {
                memset(g, 0, sizeof(g));
                fscanf(stdin, "%d%d%d", &R, &k, &N);
                for (int idx = 0; idx < N; ++idx)
                        fscanf(stdin, "%d", &g[idx]);
                fprintf(stdout, 
                        "Case #%d: %lld\n", 
                        i + 1, 
                        revenue(R, k, N, g));
        }

        return 0;
}
