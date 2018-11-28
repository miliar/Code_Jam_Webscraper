#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
using namespace std;

vector<int> e[1010];
bool fr[1010];
int n , m , X;
bool ok;

void dfs(int u)
{
    fr[u] = false;
    for (int i = 0 ; i < e[u].size() ; i ++)
    {
        int v = e[u][i];
        if (fr[v])
            dfs(v);
        else if (v != X)
            ok = true;
        if (ok)
            return ;
    }
}

int main()
{
    freopen("I.txt" , "r" , stdin);
    freopen("O.txt" , "w" , stdout);
    int ctest;
    cin >> ctest;
    for (int test = 1 ; test <= ctest ; test ++)
    {
        cin >> n;
        for (int i = 1 ; i <= n ; i ++)
        {
            e[i].clear();
            cin >> m;
            for (int j = 0 ; j < m ; j ++)
            {
                int k;
                cin >> k;
                e[i].push_back(k);
            }
        }
        ok = false;

        for (X = 1 ; X <= n ; X ++)
        {
            memset(fr , true , sizeof fr);
            dfs(X);
        }
        cout << "Case #" << test << ": ";
        if (ok)
            cout << "Yes";
        else
            cout << "No";
        cout << endl;
    }
    return 0;
}
