#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int d[111][111][111];
int qx[111111111],qy[111111111],qz[111111111];
int p[111];
char r[111];
int n,dau,cuoi;

int init() {
    cin>>n;
    int i,j;
    for (i=1; i <= n; i++) {
        cin>>r[i];
        cin>>p[i];
    }    
}

int push(int x, int y, int z) {
    cuoi++;
    if (cuoi > 111111111) cuoi = 1;
    qx[cuoi] = x;
    qy[cuoi] = y;
    qz[cuoi] = z;
}

int pop(int &x, int &y, int &z) {
    dau ++;
    if (dau > 111111111) dau = 1;
    x = qx[dau];
    y = qy[dau];
    z = qz[dau];
}

bool inside(int x, int y) {
    return ((x >= 1) && (x <= 100) && (y >= 1) && (y <= 100));
}

int solve() {
    int i,j,k;
    int x,y,z,tx,ty,tz,dx,dy;
    for (i = 0; i < 111; i++)
        for (j = 0; j < 111; j ++)
            for (k = 0; k < 111; k ++) d[i][j][k] = 11111111;
    dau = 0; cuoi = 0;
    d[1][1][1] = 0;
    push(1,1,1);
    while (dau != cuoi) {
        pop(x,y,z);
        if ((r[z] == 'B') && (p[z] == x)) {
            for (dy = -1; dy <= 1; dy++) {
                ty = y + dy; tx = x; tz = z+1;
                if (not inside(tx,ty)) continue;
                if (d[tx][ty][tz] > d[x][y][z] + 1) {
                    d[tx][ty][tz] = d[x][y][z] + 1;
                    push(tx,ty,tz);
                }
            }
        }
        if ((r[z] == 'O') && (p[z] == y)) {
            for (dx = -1; dx <= 1; dx++) {
                ty = y; tx = x + dx; tz = z+1;
                if (not inside(tx,ty)) continue;
                if (d[tx][ty][tz] > d[x][y][z] + 1) {
                    d[tx][ty][tz] = d[x][y][z] + 1;
                    push(tx,ty,tz);
                }
            }
        }
        for (dx = -1; dx <= 1; dx++) 
            for (dy = -1; dy <= 1; dy++) {
                tx = x + dx; ty = y + dy; tz = z;
                if (not inside(tx,ty)) continue;
                if (d[tx][ty][tz] > d[x][y][z] + 1) {
                    d[tx][ty][tz] = d[x][y][z] + 1;
                    push(tx,ty,tz);
                } 
            }            
    }
}

int out(int x) {
    int i,j,min;
    min = 111111111;
    for (i = 1; i <= 100; i ++)
        for (j = 1; j <= 100; j++)
            if (d[i][j][n+1] <min ) min = d[i][j][n+1];
    cout<<"Case #"<<x<<": "<<min <<"\n";
}

int main() {
   freopen("A-large.in", "rt", stdin);
   freopen("a.out", "wt", stdout);
    int t,i,j;
    cin>>t;
    for (i = 1; i <= t; i++) {
        init();
        solve();
        out(i);
    }
};
