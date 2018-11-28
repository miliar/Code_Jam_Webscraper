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

typedef pair<int, int> pxy;
typedef pair<pxy, int> pxyz;

char buffer[1000];

#ifdef DEBUG
#define PRINT(s, x...) \
fprintf(stderr, "Line %d: ", __LINE__); \
fprintf(stderr, s, x);
#define VAR(x) cerr << "Line " << __LINE__ << ": " << #x << " = " << (x) << "\n";
#define PRINTARR(x, a, b) for(int __ = (a); __ < (b); ++__) cerr << "Line " << __LINE__ << ": " <<  #x << "[" << __ << "] = " << (x)[__] << endl;
#else
#define PRINT(s, x...)
#define VAR(x)
#define PRINTARR(x, n)
#endif

int N;

class State
{
    public:
    int arr[101];
    
    bool operator<(const State& s) const
    {
        return lexicographical_compare(arr, arr+N, s.arr, s.arr+N);
    }
    
    bool check()
    {
//         printf("%d\n", N);
//         for(int i = 0; i < N; ++i)
//             printf("%d %d\n", i, arr[i]);
            
        for(int i = 0; i < N; ++i)
            if(arr[i] > i)
                return false;
            
        return true;
    }
};

int T;

int bfs(State& s)
{
    set<State> seen;
    
    queue<State> qs;
    queue<int> qc;
    
    qs.push(s);
    qc.push(0);
    
    seen.insert(s);
    
    while(!qs.empty())
    {
        State state = qs.front(); qs.pop();
        int cost = qc.front(); qc.pop();
        
        if(state.check())
            return cost;
        
        for(int i = 0; i < N-1; ++i)
        {
            State new_state = state;
            swap(new_state.arr[i], new_state.arr[i+1]);
            
            if(seen.find(new_state) == seen.end())
            {
                seen.insert(new_state);
                qs.push(new_state);
                qc.push(cost+1);
            }
        }
    }
    
    return 90000;
}



int solve(int* arr, int N, int cur = 0, int score = 0)
{
//     printf("C %d\n", cur);
//     int swaps = 0;
//     
//     for(int i = 0; i < N-1; ++i)
//         for(int j = i+1; j < N; ++j)
//             if(arr[i] > arr[i+1])
//             {
//                 swap(arr[i], arr[j]);
//                 ++swaps;
//             }
//     
//     return swaps;

    if(cur == N)
    {
            
        for(int i = 0; i < N; ++i)
            if(arr[i] > N-i)
                return 9000000;
            
        printf("SCORE %d\n", score);
        return score;
    }
    
    int mini = 9000000;
    
    for(int i = cur+0; i <= N; ++i)
    {
        if(i != N)
            swap(arr[cur], arr[i]);
        
        int sss;
        
        if(i == N)
            sss = solve(arr, N, N, score);
        else
        {
                printf("OK %d %d\n", i, cur);
                sss = solve(arr, N, cur+1, score + max(0, 2*(i - cur) - 1));   
        }
        
        if(sss < mini)
            mini = sss;
        
        if(i != N)
            swap(arr[cur], arr[i]);
    }
    
    return mini;
}

int main(int argc, char** argv)
{
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
//         int N;
        scanf("%d\n", &N);
//         printf("%d\n", N);
        int max_N[41];
        
        for(int i = 0; i < N; ++i)
        {
            int max_i = 0;
            
            for(int j = 0; j < N; ++j)
            {
                char in;
                scanf("%c", &in);
                
//                 printf("%c", in);
                if(in == '1')
                    max_i = j;
            }
            
            scanf("\n");
            max_N[i] = max_i;
//             printf("%d\n", max_N[i]);
        }
        
        State s;
        
        for(int i = 0; i < N; ++i)
        {
            s.arr[i] = max_N[i];
//             printf("%d\n", s.arr[i]);
        }
//         printf("Case #%d: %d\n", t, solve(max_N, N));
        printf("Case #%d: %d\n", t, bfs(s));
//         break;
    }
    
    return 0;
}