/*
 * Question: Find words matching the pattern
 * Author: Divye Kapoor
 * Date: 3 Sep 2009
 * 
 */
#include <iostream>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cassert>
#include <sstream>

using namespace std;

#define FOR(i, l, u) for(int i =(int)(l); i < (int)(u); ++i)
#define REP(i, u) FOR(i, 0, u)
#define LET(x, a) __typeof(a) x(a)
#define IFOR(it, b, e) for(LET(it,b); it != e; ++it)
#define SHIFTL(i, n) ((i) << (n))
#define SHIFTR(i, n) ((i) >> (n))
#define POW2(n) (1 << (n))

typedef vector<int> v_i;
typedef vector<string> v_s;
typedef set<int> set_i;
typedef set<string> set_s;
typedef map<string,int> map_si;
typedef pair<int,int> p_i;

#define INBOUNDS(x, l, u) ((x) >= (l) && (x) < (u))
#define MP(x, y) make_pair((x), (y))

int T, H, W;
int matrix[101][101];
int basin[101][101];
int count = 0;
map<int, char> mapping;
int path(int i, int j) {
    if(basin[i][j] != 0) return basin[i][j];
    
    int ocol[] = { 0, -1, 1, 0 }, orow[] = { -1, 0, 0, 1 };
    int minv = matrix[i][j], pos = -1;
    REP(k, 4) {
        int newi = i+orow[k], newj = j+ocol[k];
        if(INBOUNDS(newi, 0, H) && INBOUNDS(newj, 0, W) && matrix[newi][newj] < minv) {
            minv = matrix[newi][newj];
            pos = k;
        }
    }
    
    if(pos == -1) // sink
        return (basin[i][j] = ++::count);
    else return(basin[i][j] = path(i+orow[pos], j+ocol[pos]));
}
int main() {
    scanf("%d", &T);
    REP(cases, T) {
        scanf("%d %d", &H, &W);
        REP(i, H) REP(j, W) scanf("%d", &matrix[i][j]);
        REP(i, H) REP(j, W) basin[i][j] = 0;

        REP(i, H) REP(j, W) basin[i][j] = path(i, j);
        
        char c = 'a';
        REP(i, H) REP(j, W) if(mapping.find(basin[i][j]) == mapping.end()) mapping[basin[i][j]] = c++;
        
        printf("Case #%d: \n", cases+1);
        REP(i, H)  { 
            REP(j, W-1) cout << mapping[basin[i][j]] << ' ';
            cout << mapping[basin[i][W-1]] << endl;
        }
    }
	return 0;
}
