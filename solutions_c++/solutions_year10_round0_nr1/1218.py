#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<iostream>

// a set of chained snappers is just a binary counter with carry propatation
bool snapper_on(int N, int K)
{
        std::bitset<32> x(K % (1u << N)); // lowest N bits of K
        return (x.to_ulong() == (1u << N) - 1);  // is x all ones?
}

int main(int argc, char **argv)
{
        int T, N, K;
        fscanf(stdin, "%d", &T);

        for (int i = 1; i <= T; ++i) 
        {
                fscanf(stdin, "%d%d", &N, &K);
                fprintf(stdout, 
                        "Case #%d: %s\n", i,
                        snapper_on(N, K) ? "ON" : "OFF");
        }

        return 0;
}
