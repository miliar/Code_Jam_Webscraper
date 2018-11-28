#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for (int i = a; i < b; i++)

vector<vector<int> > board;
vector<vector<bool> > taken;
int dp[100][100][100];

int find_ans (int dim, int m, int n, int d);
int check_chess (int i, int j, int dim, int m, int n, int d);

int main() {
    int t, m, n, hexint, k, dim, d, count;
    vector<int> ans;
    char hex;

    cin >> t;
    REP(z,t) {
        cin >> m >> n;

        d = min(m,n);
        board.clear(); board.resize(m); taken.clear(); taken.resize(m); ans.clear(); ans.resize(d); REP(i,d+1) ans[i] = 0;
        REP(i,m) {
            board[i].resize(n); taken[i].resize(n); REP(j,n) taken[i][j] = false;
            REP(j,n/4) {
                cin >> hex;
                if (isdigit(hex)) hexint = hex - 0;
                else hexint = hex - 'A' + 10;
                for (k = 3; k >= 0; k--) {
                    board[i][j*4 + k] = hexint & 1;
                    hexint = hexint >> 1;
                }
            }
        }

 //       REP(i,m) {
 //           REP(j,n) cout << board[i][j] << ' ';
  //          cout << endl;
   //     }

        REP(i,100) REP(j,100) REP(p,100) dp[i][j][p] = -1;

        count = 0;
        for (dim = d; dim >= 1; dim--) {
            ans[dim] = find_ans (dim, m, n, d);
            if (ans[dim] != 0) count++;
        }
        cout << "Case #" << z+1 << ": " << count << endl;
        for (dim = d; dim >= 1; dim--) {
            if (ans[dim] != 0)
                cout << dim << ' ' << ans[dim] << endl;
        }

    }

    return 0;
}

int find_ans (int dim, int m, int n, int d) {
    int i, j, p, q, ret = 0;
    bool flag = false;
    for (i = 0; i + dim - 1 < m; i++) {
        p = i + dim - 1;
        for (j = 0; j + dim - 1 < n; j++) {
            q = j + dim - 1;

            flag = false;
            FOR(k,i,p+1) {
                FOR(l,j,q+1) {
                    if(taken[k][l] == true)
                        flag = true;
                }
            }

      //      cout << "\nhere " << i << j << " flag = " << flag << endl;
            if(!flag) {
                if( check_chess (i, j, dim, m, n, d) ) {
                    FOR(k,i,i+dim) {
                        FOR(l,j,j+dim) {
                            taken[k][l] = true;
                        }
                    }
                    ret++;
                }
            }

        }
    }
    return ret;
}

int check_chess (int i, int j, int dim, int m, int n, int d) {
    int p, q;
    bool flag = true;
    if (dp[i][j][dim] != -1)
        return dp[i][j][dim];
    if (dim == 1) dp[i][j][dim] = 1;
    else {
        int p1,p2,p3,p4,dim1,dim2;
        p1 = p2 = p3 = p4 = 0;
        dim1 = dim/2;
        dim2 = dim - dim1;

        p1 = check_chess(i,j,dim1,m,n,d);
        p2 = check_chess(i,j+dim1,dim2,m,n,d);
        p3 = check_chess(i+dim1,j,dim2,m,n,d);
        p4 = check_chess(i+dim2,j+dim2,dim1,m,n,d);

        if (p1 & p2 & p3 & p4) {
            q = j+dim1-1;
            for(p = i; p < i+dim; p++)
                if (board[p][q] == board[p][q+1]) flag = false;
            q = j+dim2-1;
            for(p = i; p < i+dim; p++)
                if (board[p][q] == board[p][q+1]) flag = false;
            p = i+dim1-1;
            for(q = j; q < j+dim; q++)
                if (board[p][q] == board[p+1][q]) flag = false;
            p = i+dim2-1;
            for(q = j; q < j+dim; q++)
                if (board[p][q] == board[p+1][q]) flag = false;
        }
        if (flag & p1 & p2 & p3 & p4) dp[i][j][dim] = 1;
        else dp[i][j][dim] = 0;
    }
    return dp[i][j][dim];
}
