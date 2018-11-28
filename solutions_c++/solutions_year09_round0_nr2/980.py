#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

typedef pair<int, int> PII;
int arr[] = {-1,0,0,1};
int arr2[] = {0,-1,1,0};
const int INF = 1000000000;

bool is_sink(int x, int y, vector<vector<int> >& M) {
    for (int i = 0; i < 4; ++i) {
        if (x + arr[i] >= 0 and x + arr[i] < M.size() and y + arr2[i] >= 0 and y + arr2[i] < M[x].size()) {
            if (M[x + arr[i]][y + arr2[i]] < M[x][y]) return false;
        }
    }
    return true;
}

bool is_parent(int px, int py, int x, int y, vector<vector<int> >& M) {
    vector<int> alt(4);
    for (int i = 0; i < 4; ++i) {
        if (px + arr[i] >= 0 and px + arr[i] < M.size() and py + arr2[i] >=0 and py + arr2[i] < M[px].size()) {
            alt[i] = M[px + arr[i]][py + arr2[i]];
        }
        else alt[i] = INF;
    }
    int minimo = INF, pos;
    for (int i = 0; i < 4; ++i) {
        if (alt[i] < minimo) {
            minimo = alt[i];
            pos = i;
        }
    }
    if (minimo >= M[px][py]) return false;
    return px + arr[pos] == x and py + arr2[pos] == y;
}

int main() {
    int k, caso = 1;
    cin >> k;
    while (k--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int> > M(n, vector<int> (m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> M[i][j];
            }
        }
        queue<PII> sinks;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (is_sink(i, j, M)) sinks.push(PII(i,j));
            }
        }
        vector<vector<int> > num(n, vector<int> (m, -1));
        int act = 0;
        while (not sinks.empty()) {
            queue<PII> Q;
            PII temp = sinks.front();
            sinks.pop();
            Q.push(temp);
            num[temp.first][temp.second] = act;
            while (not Q.empty()) {
                PII nodo = Q.front();
                Q.pop();
                int x = nodo.first, y = nodo.second;
                for (int i = 0; i < 4; ++i) {
                    if (x + arr[i] >= 0 and x + arr[i] < n and y + arr2[i] >=0 and y + arr2[i] < m and num[x+arr[i]][y+arr2[i]] == -1 and is_parent(x+arr[i],y+arr2[i],x,y, M)) {
                        num[x+arr[i]][y+arr2[i]] = act;
                        Q.push(PII(x + arr[i],y + arr2[i]));
                    }
                }
            }
            ++act;
        }
        act = 0;
        vector<vector<char> > res(n, vector<char>(m));
        map<int, char> tabla;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (tabla.count(num[i][j])) {
                    res[i][j] = tabla[num[i][j]];
                }
                else {
                    tabla[num[i][j]] = 'a' + act;
                    act++;
                    res[i][j] = tabla[num[i][j]];
                }
            }
        }
        cout << "Case #" << caso++ << ":" << endl;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (j != 0) cout << " ";
                cout << res[i][j];
            }
            cout << endl;
        }
    }
}
