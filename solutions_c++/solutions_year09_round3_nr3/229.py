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

int P, Q;
vector<int> prisoners;

long long dp[100][100];

long long recurse(int a, int b)
{
//     printf("%d %d\n", a, b);
    
    if(dp[a][b] != -1)
        return dp[a][b];
    
//     set<int>::iterator start = prisoners.lower_bound(a);
//     set<int>::iterator end = prisoners.upper_bound(b-1);
    
    vector<int> things;
    
    for(int i = 0; i < prisoners.size(); ++i)
    {
//         printf("GAR %d (%d %d)\n", prisoners[i], a, b);
        if(prisoners[i] >= a && prisoners[i] < b)
        {
            things.push_back(prisoners[i]);
//             printf("FOUND %d\n", prisoners[i]);
        }
    }
    if(things.size() == 0)
    {
        dp[a][b] = 0;
        return 0;
    }
    else
    {
        long long minimum = 100000000;
        
        for(int i = 0; i < things.size(); ++i)
        {
            int prisoner_pos = things[i];
            
            long long this_cost = b - a - 1 + recurse(a, prisoner_pos) + recurse(prisoner_pos+1, b);
            
            minimum = min(minimum, this_cost);
        }
        
        return minimum;
    }
}

int main(int argc, char** argv)
{
    int N;
    
    scanf("%d", &N);
    
    for(int t = 1; t <= N; ++t)
    {
        prisoners.clear();
        
        for(int i = 0; i < 100; ++i)
            for(int j = 0; j < 100; ++j)
                dp[i][j] = -1;
        
        scanf("%d %d", &P, &Q);
        
        for(int i = 0; i < Q; ++i)
        {
            int tmp;
            scanf("%d", &tmp);
            prisoners.push_back(tmp-1);
        }
        
        sort(prisoners.begin(), prisoners.end());
        
        printf("Case #%d: %lld\n", t, recurse(0, P));
    }
    
    return 0;
}