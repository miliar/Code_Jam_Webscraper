// GCJ '08 R3
// Question C
// Solution by sql_lall
#include <map>
#include <cmath>
#include <queue>
#include <deque>
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

vector<string> grid;
int rows, cols;
int MASK;
int cache[11][11][1 << 12];
bool seen[11][11][1 << 12];

int rec(int at, int row, int flag){
    //cout << at << " " << cols << " " << row << " " << flag << endl;
    if(row == -1) return 0;
    if(at == cols) return rec(0, row - 1, flag);
    if(flag & 1 || grid[row][at] == 'x') return rec(at + 1, row, flag / 2);
    
    
    int& c = cache[at][row][flag];
    bool& s = seen[at][row][flag];
    
    if(s) return c; s = true;
    
    // try not here:
    c = rec(at + 1, row, flag / 2);
    
    // try here:
    int M = MASK;
    if(at == 0) M -= (1 << (cols - 2));
    if(at == cols - 1) M -= 1 + (1 << cols);
    c = max(c, 1 + rec(at + 1, row, (flag / 2) | M));
    return c;
}

int solve(){
    cin >> rows >> cols;
    grid = vector<string>(rows);
    for(int r = 0; r < rows; r++) cin >> grid[r];
    MASK = 1 + 5 * (1 << (cols - 2));
    int ub = 1 << 12;
    
    for(int r = 0; r < 11; r++) for(int c = 0; c < 11; c++) for(int u = 0; u <= ub; u++){
        seen[c][r][ub] = false;
        cache[c][r][ub] = 0;
    }
    
    int ans = rec(0, rows - 1, 0);
    return ans;
}


int main(){
    int nCases; cin >> nCases;
    for(int c = 1; c <= nCases; c++)
        cout << "Case #" << c << ": " << solve() << endl;
}

/*
The following was used to break the input into single cases and run each:

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

ifstream in("C.in2");

int main(){
    vector<int> ans;
    int nCases; in >> nCases;
    for(int i = 0; i < nCases; i++){
        //cout << " case " << i << " of " << nCases << endl;
        int r, c;
        in >> r >> c;
        vector<string> lines(r);
        
        for(int R = 0; R < r; R++) in >> lines[R];
        //stringstream OT; OT << "C.in" << i;
        ofstream out("C.in");
        out << 1 << endl << r << " " << c << endl;
        for(int R = 0; R < r; R++) out << lines[R] << endl;
        out.flush(); out.close();
        stringstream comms; comms << "./C < C.in." << i << " > C.out";
        //system(comms.str().c_str());
        system("./C < C.in > C.out");
        ifstream T("C.out");
        string a,b; int z;
        T >> a >> b >> z;
        cout << "Case #" << i+1 << ": " << z << endl;
    }
}
*/
