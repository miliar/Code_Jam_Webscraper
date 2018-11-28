#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main( int argc, char* argv[] )
{
    FILE *fr = fopen("A-large.in", "r");
    FILE *fw = fopen("A-large.out", "w");

    int T;

    fscanf(fr, "%d", &T);

    for(int i = 1; i <= T; ++i)
    {
        unsigned long N, K;

        fscanf(fr, "%u %u", &N, &K);

        if(K == 0)
            fprintf(fw, "Case #%d: OFF\n", i);
        else
        {
            unsigned long pow = 1 << N;

            K %= pow;

            if(K == pow - 1)
                fprintf(fw, "Case #%d: ON\n", i);
            else
                fprintf(fw, "Case #%d: OFF\n", i);
        }
    }

    fclose(fr);
    fclose(fw);

    return 0;
}