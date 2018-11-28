// CGJ1C.1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <map>

using namespace std;

int s[1001], e[1001];
vector <vector <int>> g(1001);
int time;
int cur_time = 0;
string ans;

void dfs(int u) {
    ++time;
    s[u] = time;
    int mins = 0;
    for (auto v = g[u].begin(); v != g[u].end(); ++v) {
        if (s[*v] == 0) {
            dfs(*v);
        } else {
            ans = "Yes";
        }
    }
}

string getans()
{
    int n;
    cin >> n;
    ans = "No";
    fill(s, s + 1000, 0);
    fill(e, e + 1000, 0);
    time = 0;
    for (int i = 0; i < n; ++i) {
        g[i].clear();
        int m;
        cin >> m;
        g[i].reserve(m);
        for (int j = 0; j < m; ++j) {
            int f;
            cin >> f;
            g[i].push_back(f - 1);
            e[f - 1]++;
        }
    }
    for (int i = 0; i < n; ++i) {
        if (e[i] == 0) {
            fill(s, s + 1000, 0);
            cur_time = time;
            dfs(i);
        }
    }

    return ans;
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;
    for (int t = 1 ; t <= T; ++t) {

        cout << "Case #" << t << ": " << getans() << endl;
    }
	return 0;
}

