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

int P, p, M[2000];
bool must[3000];

int solve()
{
    memset(must, 0, sizeof(must));
    for(int i = 0; i < p; i++){
        int cnt = M[i] + 1;
        int ind = p + i;
        //cout << endl;
        while(ind){
            //cout << "! " << ind << " " << cnt << endl;
            if(!cnt){
                must[ind] = 1;
            }
            else{
                cnt--;
            }
            ind /= 2;
        }
    }
    int res = 0;
    FOR(i, 0, p * 2 + 1){
        res += must[i];
    }
    return res;
}

int main()
{
    ifstream fin("B-small.in");
    ofstream fout("B-small.out");
    int testCnt;
    fin >> testCnt;
    for(int testInd = 1; testInd <= testCnt; testInd++){
        // input
        fin >> P;
        //cout << P << endl;
        p = (1 << P);
        FOR(i, 0, p){
            fin >> M[i];
        }
        FOR(i, 1, p){
            int tmp;
            fin >> tmp;
        }
        fout << "Case #" << testInd << ": " << solve() << endl;
    }
}










