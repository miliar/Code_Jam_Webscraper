#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector< vector<int> > adj;
vector< vector<int> > rooms;

int max_katnip;
vector<int> colour(8);

int next(int i = 0) {
    if (i == N)
        return false;
    colour[i]++;
    if (colour[i] == max_katnip) {
        colour[i] = 0;
        return next(i + 1);
    }
    return true;
}

int calc_dist(int from, int to) {
    if (from <= to)
        return to - from;
    else
        return to - from + N;
}

int colours_used() {
    vector<bool> seen(N);
    int c = 0;
    for (int i = 0; i < N; i++) {
        if (!seen[colour[i]]) {
            c++;
            seen[colour[i]] = true;
        }
    }
    return c;
}

bool room_valid(int i) {
    vector<int> histogram(N, 0);
    for (int j = 0; j < rooms[i].size(); j++)
        histogram[colour[rooms[i][j]]]++;
    for (int j = 0; j < N; j++)
        if (histogram[colour[j]] == 0)
            return false;
    return true;
}

bool rooms_valid() {
    for (int i = 0; i < rooms.size(); i++)
        if (!room_valid(i))
            return false;
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        adj.clear();
        rooms.clear();
        cin >> N >> M;
        adj.resize(N);
        for (int n = 0; n < N; n++)
            adj[n].push_back((n + 1) % N);
        vector<int> b(M), e(M);
        for (int m = 0; m < M; m++)
            cin >> b[m];
        for (int m = 0; m < M; m++)
            cin >> e[m];
        for (int m = 0; m < M; m++) {
            b[m]--; e[m]--;
            adj[b[m]].push_back(e[m]);
            adj[e[m]].push_back(b[m]);
        }
        for (int n = 0; n < N; n++)
            sort(adj[n].begin(), adj[n].end());

        for (int n = 0; n < N; n++) {
            if (adj[n].size() == 1)
                continue;

            for (int i = 0; i < adj[n].size(); i++) {
                vector<int> room;
                room.push_back(n);
                int x = adj[n][i];
                while (x != n) {
                    room.push_back(x);
                    int next = -1;
                    for (int j = 0; j < adj[x].size(); j++) {
                        int y = adj[x][j];
                        if (y != room[room.size() - 2] &&
                            (next == -1 || calc_dist(y, n) < calc_dist(next, n)))
                            next = y;
                    }
                    assert(next != -1);
                    x = next;
                }
                sort(room.begin(), room.end());
                rooms.push_back(room);
            }
        }
        sort(rooms.begin(), rooms.end());
        vector< vector<int> > tmp;
        tmp.push_back(rooms[0]);
        for (int i = 1; i < rooms.size(); i++)
            if (rooms[i] != tmp[tmp.size() - 1])
                tmp.push_back(rooms[i]);
        rooms = tmp;

        max_katnip = rooms[0].size();
        for (int i = 1; i < rooms.size(); i++)
            max_katnip = min(max_katnip, (int)rooms[i].size());

        for (int i = 0; i < N; i++)
            colour[i] = 0;

        int best = 0;
        vector<int> best_col;
        do {
            if (rooms_valid()) {
                int c = colours_used();
                if (c > best) {
                    best = c;
                    best_col = colour;
                }
            }
        } while(next());

        cout << "Case #" << t + 1 << ": " << best << endl;
        for (int i = 0; i < N; i++)
            cout << best_col[i] + 1 << ' ';
        cout << endl;
    }
}
