#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

const int MAXN = 10008;

int N;
int far;

int dist[MAXN];
int len[MAXN];

bool can;
set< pair<int, int> > used;

void dfs(int node, int prev)
{
    int prevDist = 0;
    if (prev != -1) prevDist = dist[prev];
          
    int many = min(len[node], dist[node] - prevDist);
    
    if (dist[node] + many >= far)
    {
        can = true;
        return;             
    }
     
    used.insert(make_pair(node, prev)); 
    for (int i = node + 1; i < N; i++)
    {
        if (dist[node] + many < dist[i]) break;
        pair<int, int> next = make_pair(i, node);
        if (used.count(next) == 0) dfs(i, node);
    }
}

void solve()
{
    can = false; 
    used.clear();
    dfs(0, -1);
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> dist[i] >> len[i];
            
        cin >> far;    
            
        solve();
        
        string result = "";
        if (can) result = "YES"; else result = "NO";
        
        cout << "Case #" << t << ": " << result << endl;
    }
    
    return 0;
}
