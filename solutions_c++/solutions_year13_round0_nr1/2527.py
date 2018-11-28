#include <iostream>

using namespace std;

const size_t N = 4;

bool visited[N][N];
string lines[N];
int dir[][4] = {{0, 1}, {1, 1}, {1, 0}, {1, -1}};

bool check(size_t l, size_t c)
{
    for (int d = 0; d < 4; ++d)
    {
        // cout << l << ' ' << c << ' ' << d << '\n';
        int ll = l, cc = c, len = 1;
        int nl = ll + dir[d][0], nc = cc + dir[d][1];
        while (nl >= 0 && nl < N && nc >= 0 && nc < N &&
               (lines[nl][nc] == lines[l][c] || lines[nl][nc] == 'T')) 
        {
            ++len;
            ll = nl;
            cc = nc; 
            nl = ll + dir[d][0];
            nc = cc + dir[d][1];
        }
        if (len >= 4) return true;
    }
    return false;
}

int main()
{   
    size_t T;
    cin >> T;
             
    for (size_t casen = 1; casen <= T; ++casen)
    {
        for (int i = 0; i < N; ++i) {
            cin >> lines[i];       
            for (int j = 0; j < N; ++j) visited[i][j] = false;
        }
        bool isEmpty = false;
        char winner = '.';
        for (int l = 0; l < N; ++l)
            for (int c = 0; c < N; ++c) 
            {
                switch (lines[l][c]) {
                    case 'X' :
                    case 'O' :  if (check(l, c)) {
                                    winner = lines[l][c];
                                    goto end;
                                }
                                break;
                    case '.' :  isEmpty = true;  
                    default  : break;
                }
            }
        end:
        cout << "Case #" << casen << ": ";
        if (winner != '.') {
            cout << winner << " won\n";
        } else if (isEmpty) {
            cout << "Game has not completed\n";
        } else {
            cout << "Draw\n";
        }
    }
        
}