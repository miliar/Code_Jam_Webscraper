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
    int A[2000], B[2000];
    for(int t = 0; t < T; ++t)
    {
        int N;
        fscanf(fr, "%d", &N);

        for(int i = 0; i < N; ++i)
        {
            fscanf(fr, "%d %d", &A[i], &B[i]);
        }

        int cnt = 0;

        for(int i = 0; i < N; ++i)
        {
            for(int j = i + 1; j < N; ++j)
            {
                if(A[i] < A[j] && B[i] > B[j] || A[i] > A[j] && B[i] < B[j])
                    ++cnt;
            }
        }

        fprintf(fw, "Case #%d: %d\n", t + 1, cnt);
    }

    fclose(fr);
    fclose(fw);

    return 0;
}