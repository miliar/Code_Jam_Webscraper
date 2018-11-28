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
#define P(a, b) make_pair((a), (b))
#define F first
#define S second
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { for(int _i = (x1); _i < (x2); _i++){ cout << a[_i] << " "; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << a[_i][_j] << " "; } cout << endl; } }

#define MAXV 100000

struct node
{
    string name;
    list<int> children;
};

node tree[MAXV];
int cnt;
int N, M;
string path[105];
int pCnt;

int res;
int mkdir;

void build(int tInd, int pInd)
{
    if(pInd >= pCnt){
        return;
    }
    TR(it, tree[tInd].children){
        if(tree[*it].name == path[pInd]){
            build(*it, pInd + 1);
            return;
        }
    }
    tree[cnt].name = path[pInd];
    tree[tInd].children.PB(cnt);
    cnt++;
    res += mkdir;
    build(cnt - 1, pInd + 1);
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int _T;
    fin >> _T;
    for(int _t = 1; _t <= _T; _t++){
        // reset
        FOR(i, 0, MAXV){
            tree[i].children = list<int>();
        }
        tree[0].name = "";
        cnt = 1;
        res = 0;
        mkdir = 0;

        // input
        fin >> N >> M;
        FOR(i, 0, N){
            string s;
            fin >> s;
            s += '/';
            int l = 0, r = 1;
            pCnt = 0;
            while(r < s.SZ){
                while(s[r] != '/'){
                    r++;
                }
                path[pCnt++] = s.substr(l + 1, r - l - 1);
                l = r;
                r++;
            }
            build(0, 0);
        }

        mkdir = 1;

        FOR(i, 0, M){
            string s;
            fin >> s;
            s += '/';
            int l = 0, r = 1;
            pCnt = 0;
            while(r < s.SZ){
                while(s[r] != '/'){
                    r++;
                }
                path[pCnt++] = s.substr(l + 1, r - l - 1);
                l = r;
                r++;
            }
            build(0, 0);
        }

        // output
        fout << "Case #" << _t << ": " << res << endl;
    }
    return 0;
}
