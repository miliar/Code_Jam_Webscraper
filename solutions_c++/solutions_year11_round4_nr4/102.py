#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;

template<typename T>
ostream& operator<<(ostream& os, vector<T> v) {
    os << "[";
    for(int i = 0; i < v.size(); ++i) {
        cout << v[i];
        if(i != (v.size() - 1)) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}
vector<int> BFS(int v, int n, vector<vector<int> > g) {
    queue<int> q;
    q.push(v);
    vector<int> dist(n, -1);
    dist[v] = 0;
    while(!q.empty()) {
        v = q.front();
        q.pop();
        FOREACH(it, g[v]) {
            if(dist[*it] == -1) {
                dist[*it] = dist[v] + 1;
                q.push(*it);
            }
        }
    }
    return dist;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int testCase = 1; testCase <= t; ++testCase)
    {
        int n, p;
        scanf("%d %d", &n, &p);
        vector<vector<int> > g(n);
        vector<vector<bool> > m(n, vector<bool>(n, false));
        for(int i = 0; i < n; ++i) {
            g[i].push_back(i);
            m[i][i] = true;
        }
        for(int i = 0; i < p; ++i) {
            int a, b;
            scanf("%d,%d ", &a, &b);
            g[a].push_back(b);
            g[b].push_back(a);
            m[a][b] = m[b][a] = true;
        }
        vector<int> dist = BFS(0, n, g);
        vector<vector<int> > distT(n);
        vector<bool> important(n, false);
        important[1] = true;
        for(int i = 0; i < n; ++i) {
            if(dist[i] != -1)
                distT[dist[i]].push_back(i);
        }
        vector<vector<int> > res(n, vector<int>(n, -1));
        FOREACH(it, distT[dist[1] - 1]) {
            FOREACH(eit, g[*it]) {
                if(*eit == 1) {
                    res[*it][*it] = g[*it].size();
                }
            }
        }
        for(int i = dist[1] - 2; i >= 0; --i) {
            FOREACH(it, distT[i]) {
                FOREACH(it1, g[*it]) {
                    if((dist[*it]  + 1) == dist[*it1]) {
                        FOREACH(it2, g[*it1]) {
                            if(res[*it1][*it2] != -1) {
                                int bonus = 0;
                                FOREACH(it3, g[*it]) {
                                    if((!m[*it3][*it1]) && (!m[*it3][*it2])) {
                                        bonus++;
                                    }
                                }
                                res[*it][*it1] = max(res[*it][*it1], res[*it1][*it2] + bonus);
                            }
                        }
                    }
                }
            }
        }
        int ans = -1;
        FOREACH(it, g[0]) {
            ans = max(ans, res[0][*it]);
        }
        printf("Case #%d: %d %d\n", testCase, dist[1] - 1, ans - dist[1]);
    }
}
