#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

int fill(int x, int y, vector<vector<int> >& v, vector<vector<int> >& w, int &iFill) {
    if (w[x][y] != 0) return w[x][y];
    int iDir = -1;
    int iVal = 100000;
    
    for (int i = 0; i < 4; i++) {
        int xx = x + dir[i][0];
        int yy = y + dir[i][1];
        if (xx >= 0 && yy >= 0 && xx < v.size() && yy < v[0].size()) {
            if (v[x][y] > v[xx][yy]) {
                if (v[xx][yy] < iVal) {
                    iDir = i;
                    iVal = v[xx][yy];
                }        
            }
        }
    }
    if (iDir == -1) {
        w[x][y] = iFill;
        iFill++;
        return w[x][y];
    }
    else {
        return w[x][y] = fill(x + dir[iDir][0], y + dir[iDir][1], v, w, iFill);
    }
}

int main() {
    int N, A, B;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ":" << endl;
        cin >> A >> B;
        vector<vector<int> > v(A, B);
        vector<vector<int> > w(A, B);
        for (int i = 0; i < A; i++)
           for (int j = 0; j < B; j++) cin >> v[i][j];
           
        int iFill = 1;
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < B; j++) {
                if (w[i][j] == 0) {
                    fill(i, j, v, w, iFill);            
                }    
            }
        }
        for (int i = 0; i < A; i++) {
            cout << char(w[i][0] + 'a' - 1);
            for (int j = 1; j < B; j++) {
                cout << " " << char(w[i][j] + 'a' - 1);
            }
            cout << endl;
        }        
    }
}
