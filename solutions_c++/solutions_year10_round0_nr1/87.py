// Compile by: g++ -O2 thisfile.cc
// Tested with g++ (GCC) 4.3.4 20090804 (release) 1 on Cygwin

#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int idxCase = 0; idxCase < T; ++idxCase)
    {
        int N, K;
        scanf("%d%d", &N, &K);
        printf("Case #%d: %s\n", idxCase + 1, ((K + 1) & ((1 << N) - 1)) == 0 ? "ON" : "OFF");
    }
    return 0;
}
