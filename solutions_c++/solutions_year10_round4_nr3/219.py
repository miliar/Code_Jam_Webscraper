#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
using namespace std;

#define SZ size()
#define PB push_back
#define B begin()
#define E end()
#define SORT(a) sort((a).B, (a).E)
#define REV(a) reverse((a).B, (a).E)
#define UNQ(a) (a).resize(unique((a).B, (a).E) - (a).B)
#define SUM(a) accumulate((a).B, (a).E, 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(__typeof(a.B) i = a.B; i != a.E; i++)
#define SQR(x) ((x) * (x))
#define EUCL(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))
#define MANH(x1, y1, x2, y2) (abs((x1) - (x2)) + abs((y1) - (y2)))
#define CROSS(x1, y1, x2, y2) ((x1) * (y2) - (y1) * (x2))
#define CROSS2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((y2) - (y0)) - ((y1) - (y0)) * ((x2) - (x0)))
#define DOT(x1, y1, x2, y2) ((x1) * (x2) + (y1) * (y2))
#define DOT2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((x2) - (x0)) + ((y1) - (y0)) * ((y2) - (y0)))
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { for(int _i = (x1); _i < (x2); _i++){ cout << a[_i] << " "; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << a[_i][_j] << " "; } cout << endl; } }

struct rect
{
    int x1, y1, x2, y2;
};

int R;
rect a[1005];
bool G[1005][1005], used[1005];
stack<rect> S;
int X, Y;

void dfs(int ind)
{
    X >?= a[ind].x2;
    Y >?= a[ind].y2;
    S.push(a[ind]);
    used[ind] = ind;
    for(int i = 0; i < R; i++){
        if(!used[i] && G[ind][i]){
            dfs(i);
        }
    }
}

bool touch(int i, int j)
{
    //cout << a[i].x1 << " " << a[i].y1 << " " << a[i].x2 << " " << a[i].y2 << endl;
    //cout << a[j].x1 << " " << a[j].y1 << " " << a[j].x2 << " " << a[j].y2 << endl;


    if(a[i].x2 + 1 == a[j].x1 && a[i].y2 + 1 == a[j].y1){
        return 0;
    }
    if(a[j].x2 + 1 == a[i].x1 && a[j].y2 + 1 == a[i].y1){
        return 0;
    }
    if(a[i].x2 + 1 < a[j].x1 || a[j].x2 + 1 < a[i].x1){
        return 0;
    }
    if(a[i].y2 + 1 < a[j].y1 || a[j].y2 + 1 < a[i].y1){
        return 0;
    }
    //cout << "1" << endl;
    return 1;


    /*if(a[i].x2 + 1 == a[j].x1 && a[i].y2 + 1 >= a[j].y1 && a[j].y1 >= a[i].y1){
    cout << "1" << endl;
        return 1;
    }
    if(a[j].x2 + 1 == a[i].x1 && a[j].y2 + 1 >= a[i].y1 && a[i].y1 >= a[j].y1){
    cout << "1" << endl;
        return 1;
    }
    if(a[i].x2 < a[j].x1 || a[i].x1 > a[j].x2){
        cout << "0" << endl;
        return 0;
    }
    if(a[i].y2 < a[j].y1 || a[i].y1 > a[j].y2){
        cout << "0" << endl;
        return 0;
    }
    cout << "1" << endl;
    return 1;*/
}

int solve()
{
    memset(G, 0, sizeof(G));
    for(int i = 0; i < R; i++){
        for(int j = i + 1; j < R; j++){
            if(touch(i, j)){
                G[i][j] = G[j][i] = 1;
            }
        }
    }
    //DEBUG2D(G, 0, R, 0, R);

    int res = 0;
    memset(used, 0, sizeof(used));
    for(int i = 0; i < R; i++){
        if(!used[i]){
            S = stack<rect>();
            X = 0;
            Y = 0;
            dfs(i);
            //cout << X << " " << Y << endl;
            int dist = 0;
            while(!S.empty()){
                dist >?= 1 + abs(S.top().x1 - X) + abs(S.top().y1 - Y);
                S.pop();
            }
            res >?= dist;
        }
    }

    return res;
}

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    int testCnt;
    fin >> testCnt;
    for(int testInd = 1; testInd <= testCnt; testInd++){
        // input
        fin >> R;
        for(int i = 0; i < R; i++){
            fin >> a[i].x1 >> a[i].y1 >> a[i].x2 >> a[i].y2;
            if(a[i].x1 > a[i].x2){
                swap(a[i].x1, a[i].x2);
            }
            if(a[i].y1 > a[i].y2){
                swap(a[i].y1, a[i].y2);
            }
            //cout << a[i].x1 << " " << a[i].y1 << " " << a[i].x2 << " " << a[i].y2 << endl;
        }
        fout << "Case #" << testInd << ": " << solve() << endl;
    }
}










