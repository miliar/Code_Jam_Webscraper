#include <cstdio>
#include <iostream>
#include <sstream>

#include <cstring>
#include <cstdlib>

#include <list>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>

#include <complex>
#include <cmath>

#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

char buffer[1000];

unsigned long long solve()
{
    unsigned int symbols[100];
    unsigned int next_symbol = 0;
    
    for(int i = 0; i < 100; ++i)
        symbols[i] = i;
    
    symbols[0] = 1;
    symbols[1] = 0;
    
    char table[256];
    fill(table, table+256, -1);
    
    int pos = 0;
    
    while(buffer[pos] != 0)
    {
        if(table[buffer[pos]] == -1)
            table[buffer[pos]] = symbols[next_symbol++];
        
        ++pos;
    }
    
    unsigned long long ans = 0;
    
    unsigned long long power = 1;
    
    if(next_symbol == 1)
        next_symbol = 2;
    
    for(int i = pos-1; i >= 0; --i)
    {
        
//         printf("%lld %c %d\n", table[buffer[i]]*power, buffer[i], table[buffer[i]]);
        ans += table[buffer[i]]*power;
        power *= next_symbol;
    }
    
    return ans;
}

int main(int argc, char** argv)
{
    int T;
    scanf("%d\n", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        scanf("%s", buffer);
        
//         printf("%s\n", buffer);
        
        printf("Case #%d: %lld\n", t, solve());
    }
    
    return 0;
}