#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; i++)

int pack(int x, int y) {
    return x*100 + y;
}

class uni {
    vector<int> p, rank;
public:
    int elements;
    uni(int size) {
        p.assign(size, -1); rank.assign(size, 0);
        elements = 0;
    }
    void makeSet(int val) {
        p[val] = val;
        elements += 1;
    }
    int findSet(int val) {
        if (p[val] < 0) return p[val]; // element not found
        if (val != p[val])
            p[val] = findSet(p[val]);
        return p[val];
    }
    void merge(int x, int y) {
        x = findSet(x), y = findSet(y);
        if (x == y) return;
        if (rank[x] > rank[y])
            p[y] = x;
        else {
            p[x] = y;
            if (rank[x] == rank[y]) rank[y] += 1;
        }
    }
};

void debug(uni &u, int h, int w) {
    rep(i,h) {
        rep(j,w) printf("%d ", u.findSet(pack(i,j)));
        puts("");
    }
    puts("");
}

int main()
{
    int t;
    cin >> t;
    rep(I,t) {
        int h, w;
        cin >> h >> w;
        int map[100][100], ans[100][100];
        uni u(10000);
        rep(i,h) rep(j,w) cin >> map[i][j];
        while (u.elements < h*w) {
            int mx = -1, X, Y;
            rep(i,h) rep(j,w) if (u.findSet(pack(i,j)) < 0) {
                if (map[i][j] > mx) {
                    X = i; Y = j; mx = map[i][j];
                }
            }
            u.makeSet(pack(X,Y));
            int dh[] = {-1,0,0,1},  dw[] = {0,-1,1,0};
            for (;;) {
                //printf("X,Y = %d,%d\n", X, Y);
                int mn = map[X][Y], mni;
                rep(i,4) {
                    if (X+dh[i] >= h || X+dh[i] < 0 || Y+dw[i] >= w || Y+dw[i] < 0) continue;
                    //printf("searching X,Y = %d,%d\n", X+dh[i], Y+dw[i]);
                    if (map[X+dh[i]][Y+dw[i]] < mn) {
                        mn = map[X+dh[i]][Y+dw[i]];
                        mni = i;
                    }
                }
                int newX = X+dh[mni], newY = Y+dw[mni];
                if (mn == map[X][Y]) break; // sink
                if (u.findSet(pack(newX, newY)) < 0) u.makeSet(pack(newX, newY));
                u.merge(pack(newX, newY), pack(X,Y));
                X = newX, Y = newY;
            }
            //debug(u,h,w);
            
        }
        std::map<int,char> m;
        char cur = 'a';
        rep(i,h) rep(j,w) {
            if (m.find(u.findSet(pack(i,j))) == m.end()) {
                m.insert(make_pair(u.findSet(pack(i,j)), cur++));
            }
        }
        printf("Case #%d:\n", I+1);
        rep(i,h) rep(j,w) printf("%c%s", m[u.findSet(pack(i,j))], (j == w-1) ? "\n" : " ");
    }
    return 0;
}
