#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long long int64;

#define maxn (1 << 11)

std::vector<int> g[maxn];
int n, m, u[maxn], v[maxn];

std::vector<std::vector<int> > rooms;

bool lies_between(int m, int l, int r) {
    if(r - l >= 0)
        return (l < m) && (m <= r);
    return (m <= r) || (m > l);
}

void find_rooms(int l, int r) {
    //fprintf(stderr, "[%d, %d]\n", l, r);
    std::vector<int> room;
    room.push_back(r);
    for(int i = l; i != r; ) {
        //Eo(i);
        int m = -1;
        for(int j = 0; j < g[i].size(); j++)
            if((i != l || g[i][j] != r) && lies_between(g[i][j], i, r) && (m == -1 || lies_between(g[i][j], m, r)))
                m = g[i][j];
        //Eo(m);
        room.push_back(i);
        if(m != -1) {
            find_rooms(i, m);
            i = m;
        } else {
            i = (i+1) % n;
        }
    }
    rooms.push_back(room);
    //fprintf(stderr, ">>>>>>>>>\n");
}

int k, degree[maxn], ind[maxn], color[maxn];

inline bool cmp(int i, int j) {
    return degree[i] > degree[j];
}

bool paint(int v) {
    if(v == n) return true;
    if(degree[ind[v]] <= 1) {
        assert(degree[ind[v]] == 1);
        int ocol[16];
        memcpy(ocol, color, sizeof(ocol));
        for(int r = 0; r < rooms.size(); ++r) {
            int cls[16] = {0}, j = 0;
            for(int i = 0; i < rooms[r].size(); i++)
                if(color[rooms[r][i]] >= 0)
                    cls[color[rooms[r][i]]] = 1;
            for(int i = 0; i < rooms[r].size(); i++)
                if(color[rooms[r][i]] < 0) {
                    for(; j < k-1 && cls[j]; ++j);
                    color[rooms[r][i]] = j;
                    cls[j] = 1;
                    if(j < k-1) j++;
                }
            for(int i = 0; i < k; i++)
                if(!cls[i]) {
                    memcpy(color, ocol, sizeof(ocol));
                    return false;
                }
        }
        return true;
    }
    int cnt = 0;
    std::set<int> cls[16];
    for(int r = 0; r < rooms.size(); ++r)
        if(std::find(rooms[r].begin(), rooms[r].end(), ind[v]) != rooms[r].end()) {
            ++cnt;
            for(int j = 0; j < rooms[r].size(); j++)
                if(color[rooms[r][j]] >= 0)
                    cls[color[rooms[r][j]]].insert(r);
        }
    for(int c = 0; c < k; c++)
        if(cls[c].size() < k) {
            color[ind[v]] = c;
            if(paint(v+1)) return true;
            color[ind[v]] = -1;
        }
    return false;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++) g[i].clear();
        for(int i = 0; i < m; i++) 
            scanf("%d", u+i);
        for(int i = 0; i < m; i++)
            scanf("%d", v+i);

        //for(int i = 0; i < n; i++) {
        //    g[i].push_back((i+1) % n);
        //    g[i].push_back((i-1+n) % n);
        //}
        for(int i = 0; i < m; i++) {
            u[i]--; v[i]--;
            g[u[i]].push_back(v[i]);
            g[v[i]].push_back(u[i]);
        }
        for(int i = 0; i < n; i++)
            std::sort(g[i].begin(), g[i].end());

        rooms.clear();
        for(int i = 0; i < n; i++)
            if(g[i].size() > 0) {
                find_rooms(i, g[i][0]);
                find_rooms(g[i][0], i);
                break;
            }
        //for(int i = 0; i < rooms.size(); i++, printf("\n"))
        //    for(int j = 0; j < rooms[i].size(); j++)
        //        printf("%d ", rooms[i][j]);
        memset(degree, 0, sizeof(degree));
        for(int i = 0; i < rooms.size(); i++)
            for(int j = 0; j < rooms[i].size(); j++)
                degree[rooms[i][j]]++;
        for(int i = 0; i < n; i++) ind[i] = i;
        std::sort(ind, ind+n, cmp);
        //for(int i = 0; i < n; i++) fprintf(stderr, "%d ", ind[i]); fprintf(stderr, "\n");

        //printf("!!!!!!!!!\n");
        memset(color, -1, sizeof(color));
        for(k = n; k > 0; --k)
            if(paint(0)) {
                printf("%d\n", k);
                for(int j = 0; j < n; j++)
                    printf("%s%d", (j == 0 ? "" : " "), color[j]+1);
                break;
            }
        printf("\n");
	}
	return 0;
}
