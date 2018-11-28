#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define pb push_back
#define pii pair<int, int>
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

int r, c, k;
char board[55][55];
string newboard[55];

static int dr[] = {1, 0, 1, 1};
static int dc[] = {0, 1, 1, -1};

bool valid(int i, int j)
{
    return (i >= 0 && i < r && j >= 0 && j < c);
}

bool wins(char color)
{
    FOR(i, 0, r)
        FOR(j, 0, c) if(newboard[i][j] != '.'){
            
            FOR(dir, 0, 4) {
                bool ok = true;
                FOR(s, 0, k){
                    if(!valid(i + s*dr[dir], j + s*dc[dir]) || newboard[i + s*dr[dir]][j + s*dc[dir]] != color){
                        ok = false;
                        break;
                    }
                }
                if(ok) return true;
            }
        }
    return false;
}

string solve()
{
    FOR(i, 0, r){
        string row = "";
        FOR(j, 0, c){
            if(board[i][j] != '.') row += board[i][j];
        }
        newboard[i] = "";
        FOR(t, 0, (c - SZ(row))) newboard[i] += '.';
        newboard[i] += row;
    }

    bool redwins = wins('R');
    bool bluewins = wins('B');

    if(bluewins && redwins) return "Both";
    if(bluewins) return "Blue";
    if(redwins) return "Red";
    return "Neither";
}

int main()
{
    int cases;
    scanf("%d", &cases);
    FOR(testcase, 0, cases){
        scanf("%d %d", &r, &k); getchar();
        c = r;
        FOR(i, 0, r) fgets(board[i], 55, stdin);
        printf("Case #%d: %s\n", testcase + 1, solve().c_str());
    }

}

