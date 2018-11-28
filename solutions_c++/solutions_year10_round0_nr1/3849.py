// gcj snapper.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        unsigned long long int N, K;
        scanf("%llu%llu", &N, &K);
        if(K % ((unsigned long long int)1 << N) == ((unsigned long long int)1 << N) - (unsigned long long int)1)
            printf("ON");
        else
            printf("OFF");
        printf("\n");
    }
    return 0;
}
