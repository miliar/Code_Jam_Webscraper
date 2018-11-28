#include <algorithm>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
fstream inp, out;
const int oo = 1000000;
struct Edge{
    int from;
    int to;
    int cap;
    int flow;
    Edge(int from, int to, int cap)
    {
        this->from = from;
        this->to   = to;
        this->cap  = cap;
        this->flow = 0;
    }
};

template <int N>
struct Network{
    vector<int> adj[N];
    vector<Edge> edges;
    int source, sink;
    int was[N];// label
    int pv[N]; // previous vertex 
    int pe[N]; // previous edge
    int mark;
    void add_edge(int v1, int v2, int c1, int c2)
    {
        adj[v1].push_back(edges.size());
        edges.push_back(Edge(v1, v2, c1));
        adj[v2].push_back(edges.size());
        edges.push_back(Edge(v2, v1, c2));
    }
    bool augment()
    {
        queue<pair<int, int> > qu;
        ++mark;
        int v = source, d = oo;
        was[v] = mark;
        qu.push(make_pair(v, d));
        while (!qu.empty())
        {
            v = qu.front().first;
            d = qu.front().second;
            qu.pop();
            if (v == sink) break;
            for (int j = 0; j < (int)adj[v].size(); ++j)
            {
                int e  = adj[v][j];
                int nd = edges[e].cap - edges[e].flow;
                int nv = edges[e].to;
                if (nd && was[nv] != mark)
                {
                    qu.push(make_pair(nv, min(d, nd)));
                    was[nv] = mark;
                    pv[nv] = v;
                    pe[nv] = e;
                }
            }
        }
        if (v != sink) return 0;
        while (v != source)
        {
            edges[pe[v]    ].flow += d;
            edges[pe[v] ^ 1].flow -= d;
            v = pv[v];
        }
        return d;
    }
    int max_flow()
    {
        memset(was, 0, sizeof(was));
        mark = 1;
        while (augment());
        int res = 0;
        for (int j = 0; j < (int)adj[source].size(); ++j) res += edges[adj[source][j]].flow;
        return res;
    }
};

bool a[100][100];

int main(int argc, char *argv[])
{
    if (argc != 2) { cout << "specify input/output" << endl; return -1;}
    inp.open ((string(argv[1]) + string(".in")).c_str(), fstream::in);
    out.open ((string(argv[1]) + string(".out")).c_str(), fstream::out);
    int T;
    inp >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        cout << "processing case " << cs << endl;
        int n, k;
        inp >> n >> k;
        vector<vector<int> > price;
        memset(a, 0, sizeof(a));
        for (int i = 0; i < n; ++i)
        {
            vector <int> p;
            for (int j = 0; j < k; ++j)
            {
                int x; inp >> x;
                p.push_back (x);
            }
            price.push_back(p);
        }
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
        {
            bool lower = true;
            for (int h = 0; h < k; ++h)
                if (price[i][h] >= price[j][h]) lower = false;
            a[i][j] = lower;
        }
        Network <100 + 100 + 2> net;
        net.source = 2*n;
        net.sink   = net.source + 1;
        for (int i = 0; i < n; ++i)
        {
            net.add_edge(net.source, i, 1, 0);
            net.add_edge(n+i, net.sink, 1, 0);
        }
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (a[i][j]) 
            {
                net.add_edge(i, n + j, 1, 0);
            }
        int m = net.max_flow();  
        cout << m << endl;  
        out << "Case #" << cs << ": " << (n - m) << endl; 
    }
    return 0;
}