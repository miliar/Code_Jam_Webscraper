#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

typedef long long LL;

const int MAXN = 1024;

int N;
vector<int> graph[MAXN];
int DP[MAXN];

int rec(int node, int goal)
{
    if (node == goal) return 1;
    if (DP[node] != -1) return DP[node];
    
    int result = 0;
    for (int i = 0; i < graph[node].size(); i++)
    {
        int nextNode = graph[node][i];
        result += rec(nextNode, goal);
    }
    
    return DP[node] = result;
} 

bool solve()
{
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
        {
            if (i == j) continue;
            
            memset(DP, -1, sizeof(DP));
            
            int many = rec(i, j);
            if (many > 1) return true;
        }
     
    return false; 
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
                
        for (int i = 1; i <= N; i++)
        {
           graph[i].clear(); 
            
           int M; cin >> M;
           for (int j = 0; j < M; j++)
           {
               int from; cin >> from;
               graph[i].push_back(from);
           }
        }
        
        bool ans = solve();
        string print = ans ? "Yes" : "No";
        
        printf("Case #%d: %s\n", t, print.c_str());               
    }
    
    return 0;
}
