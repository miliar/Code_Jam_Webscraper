#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int n;
int pos[505];
int table[500];
int res;
vector<int> s;
void dfs(int cur)
{
    if(cur==n)
    {
        int p = s.size() + 1;
        int ok = 0;
        while( 1 )
        {
            if ( p == 1)
            {
                ok = 1;
                break;
            }
            p = pos[p];
            if(p==-1)break;    
        }
        if(ok)res++;
        return;
    }
    s.push_back(cur);
    pos[cur] = s.size();
    dfs(cur+1);
    pos[cur] = -1;
    s.pop_back();
    dfs(cur+1);
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int c;
    cin >> c;
    for(int ca = 1; ca <= c; ++ca)
    {
        cin >> n;
        res = 0;
        memset(pos, -1, sizeof(pos));
        if ( table[n] != 0 ) res = table[n];
        else
        {
            dfs(2);
            table[n] = res;
        }
        cout << "Case #" << ca << ": " << res%100003 << endl;
        
    }
   return 0;
}
