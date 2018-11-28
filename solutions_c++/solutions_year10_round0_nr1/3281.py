#include <iostream>
using namespace std;

typedef unsigned uT;
typedef unsigned long long ullT;
int main()
{
     uT T, N, K;

     scanf("%u", &T);

     for(uT i = 0; i < T ; ++i)
     {
        scanf("%u %u", &N, &K);

        ullT maxValue = 1LL<<N;

        string state = (K+1)%maxValue ? "OFF" : "ON";

        printf("Case #%u: %s\n", i+1, state.c_str());
     }
return 0;
}
