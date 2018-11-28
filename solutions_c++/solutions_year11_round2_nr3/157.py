#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

vector<int> train[10];
int u[10], v[10], n, m, trainNum, numC, col[10], ansCol[10];
bool flag;

bool check()
{
    int i, j;
    for(i = 0; i < trainNum; i++)
    {
        set<int> cSet;
        for(j = 0; j < train[i].size(); j++) cSet.insert(col[train[i][j]]);
        if(cSet.size() < numC) return false;
    }
    return true;
}

void dfs(int k)
{
    int i, a;
    if(flag) return;
    if(k > n)
    {
        if(check())
        {
            flag = true;
            for(i = 1; i <= n; i++) ansCol[i] = col[i];
        }
        return;
    }
    
    for(a = 1; a <= numC; a++)
    {
        col[k] = a;
        dfs(k + 1);
    }
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int T, tt, i, j, k, st, ed;
    
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++)
    {
        scanf("%d%d", &n, &m);
        for(i = 0; i < 10; i++) train[i].clear();
        for(i = 1; i <= n; i++) train[0].push_back(i);
        trainNum = 1;
        for(i = 0; i < m; i++) scanf("%d", &u[i]);
        for(i = 0; i < m; i++) scanf("%d", &v[i]);
        for(i = 0; i < m; i++)
            for(j = 0; j < trainNum; j++)
            {
                st = ed = -1;
                for(k = 0; k < train[j].size() && ed < 0; k++)
                    if(train[j][k] == u[i] || train[j][k] == v[i])
                        if(st < 0) st = k; else ed = k;
                if(ed < 0) continue;
                for(k = st; k <= ed; k++)train[trainNum].push_back(train[j][k]);
                for(k = 0; k < ed - st - 1; k++) train[j].erase(train[j].begin() + (st + 1));
                trainNum++;
                break;
            }
        numC = n;
        for(i = 0; i < trainNum; i++)
            if(train[i].size() < numC) numC = train[i].size();
        printf("Case #%d: %d\n", tt, numC);
        col[1] = 1;
        flag = false;
        dfs(2);
        printf("%d", ansCol[1]);
        for(i = 2; i <= n; i++) printf(" %d", ansCol[i]);
        printf("\n");
    }
    
    return 0;
}
