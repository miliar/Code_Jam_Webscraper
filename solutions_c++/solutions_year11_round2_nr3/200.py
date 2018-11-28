#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i) 

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

int N;

struct UV
{
    int u, v;
    UV(int u, int v) : u(u - 1), v(v - 1) { }
};

vector<UV> uv;
char arr[10][10];

int next(int to, int from) {
    int ret = (to+1) % N;
    for (int i = (to + 2) % N; i != from; i = (i+1) % N)
        if (arr[to][i])
            ret = i;
    return ret;
}

set<int> rooms;

void fill(int from, int to) {
    int mask = 0;
    int p;
    vector<int> borders;
    borders.push_back(from);
    borders.push_back(to);
 
    while ((p = next(to, from)) != borders[0]) {
        borders.push_back(p);
        from = to;
        to = p;
    }

    foreach(jt, borders)
        mask |= (1 << *jt);
    rooms.insert(mask);
}

void getRooms()
{
    rooms.clear();
    foreach(it, uv) {
        fill(it->u, it->v);
        fill(it->v, it->u);
    } 
}

int diff(int *colors)
{
    static int count[5];
    memset(count, 0, sizeof(count));
    for (int i = 0; i < N; i++)
        count[colors[i]] = 1;
    int ret = 0;
    for (int i = 0; i < 5; i++)
        ret += count[i];
    return ret;
}

vector< vector<int> > realRooms;
bool isvalid(int *colors, int d)
{
    foreach(it, realRooms) {
        int mask = (1 << d) - 1;
        for (int j = 0; j < it->size(); j++)
            mask &= ~(1 << colors[(*it)[j]]);
        if (mask)
            return false;
    }
    return true;
}

void solve()
{
    memset(arr, 0, sizeof(arr));
    foreach(it, uv)
        arr[it->u][it->v] = arr[it->v][it->u] = 1;
    getRooms();
    //int best = 99999999;
    int best = 1;
    realRooms.clear();
    foreach(it, rooms) {
        int x = *it;
        vector<int> indices;
        int c = 0;
        while(x) {
            if (x & 1)
                indices.push_back(c);
            c++;
            x >>= 1;
        }
        realRooms.push_back(indices);
        //best = min<size_t>(best, indices.size());
        //foreach(jt, indices)
        //    cout << *jt << ' ';
        //cout << endl;
    }

    int colors[8];
    int bestColors[8];
    colors[0] = 0;
    for (int realM = 0; realM < 78125; realM++) {
        int m = realM;
        int d = 0;
        for (int j = 1; j < 8; j++) {
            colors[j] = m % 5;
            d = max(colors[j], d);
            m /= 5;
        }
        ++d;

        if (d <= best || diff(colors) < d)
            continue;
        if (isvalid(colors,d)) {
            best = d;
            memcpy(bestColors, colors, sizeof(colors));
        }

    }
    cout << best << endl;
    for (int i = 0; i < N; i++)
        cout << (bestColors[i] + 1) << ' ';
    cout << endl;
}

int main(int argc, const char* argv[])
{
	int T;
    cin >> T;
    int M;
    for (int i = 0; i < T; i++) {
        int t;
        vector<int> u;
        uv.clear();
        cin >> N >> M;
        for (int j = 0; j < M; j++) {
            cin >> t;
            u.push_back(t);
        }
        for (int j = 0; j < M; j++) {
            cin >> t;
            uv.push_back(UV(u[j], t));
        }
        cout << "Case #" << (i+1) << ": ";
        solve();
    }

    return 0;
}
