#include <cstdio>
#include <string>
#include <vector>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

vector< vector<int> > rooms;

int pos(int A, vector<int>& room) {
    for (int i = 0;i < room.size();++i)
        if (room[i] == A)
            return i;
    return -1;
}

int U[10];
int V[10];
int C[10];
int n;
int cc;
int best;
int solution[10];
bool enough = false;
bool debug() {
    return C[0] == 0 && C[1] == 1 && C[2] == 0 && C[3] == 2;
}

void func(int step) {
    if (step == n) {
        bool use[10];
        memset(use, false, sizeof use);
        int num = 0;
        for (int i = 0;i < n;++i)
            use[C[i]] = true;
        for (int i = 0;i < n;++i)
            if (use[i])
                ++num;
        if (best >= num)
            return;
        bool bad = false;
        for (int i = 0;i < rooms.size();++i) {
            memset(use, false, sizeof use);
            int num2 = 0;
            for (int j = 0;j < rooms[i].size();++j)
                use[C[rooms[i][j]]] = true;
            for (int j = 0;j < n;++j)
                if (use[j])
                    ++num2;
            if (num != num2) {
                bad = true;
                break;
            }
        }

        if (bad) return;
        best = num;
        memcpy(solution, C, sizeof solution);

        return;
    }
    for (int i = 0;i < n;++i) {
        C[step] = i;
        func(step + 1);
    }
}

int main() {

    int t;
    int m;

    vector<int> poses;

    scanf("%d", &t);

    for (int test = 1;test <= t;++test) {

        scanf("%d%d", &n, &m);

        rooms.clear();
        vector<int> first;

        for (int i = 0;i < n;++i)
            first.push_back(i);

        rooms.push_back(first);

        for (int i = 0;i < m;++i)
            scanf("%d", U + i),
            --U[i];
        for (int i = 0;i < m;++i)
            scanf("%d", V + i),
            --V[i];

        for (int i = 0;i < m;++i) {
            for (int j = 0;j < rooms.size();++j) {
                int a = pos(U[i], rooms[j]);
                int b = pos(V[i], rooms[j]);
                if (a == -1 || b == -1) continue;
                int c = min(a, b);
                int d = max(a, b);
                vector<int> nn;
                for (int k = c;k <= d;++k)
                    nn.push_back(rooms[j][k]);
                rooms.push_back(nn);
                rooms[j].erase(rooms[j].begin() + c + 1, rooms[j].begin() + d);
                break;
            }
        }


        best = 0;
        func(0);
        printf("Case #%d: %d\n", test, best);
        for (int i = 0;i < n;++i)
            printf("%d ", solution[i] + 1);
        puts("");
    }

    return 0;
}
