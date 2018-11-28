#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

const int DX[4] = {0, -1, -1, -1};
const int DY[4] = {-1, -1, 0, 1};

typedef vector<int> VI;
typedef vector<VI> VVI;

int T, N, M;
vector<string> board;
VVI b;
vector<VVI> c;

int main()
{
    ifstream input("A-large.in");
    ofstream output("A-large.out");
    input >> T;
    for (int casenum = 0; casenum < T; casenum++)
    {
        input >> N >> M;
        board.resize(N);
        for (int i = 0; i < N; i++) input >> board[i];
        b.resize(N);
        for (int i = 0; i < N; i++)
        {
            b[i].resize(N);
            for (int j = 0; j < N; j++)
                if (board[N-1-j][i] == '.')
                    b[i][j] = 0;
                else if (board[N-1-j][i] == 'R')
                    b[i][j] = 1;
                else
                    b[i][j] = -1;
        }
        
        for (int j = 0; j < N; j++)
        {
            VI col;
            for (int i = N-1; i >= 0; i--) 
                if (b[i][j] != 0) col.push_back(b[i][j]);
            while (col.size() < N) col.push_back(0);
            for (int i = 0; i < N; i++) b[N-1-i][j] = col[i];
        }
        
        c.resize(N);
        bool winred = false;
        bool winblue = false;
        for (int i = 0; i < N; i++)
        {
            c[i].resize(N);
            for (int j = 0; j < N; j++) c[i][j].resize(4);
            for (int j = 0; j < N; j++)
                if (b[i][j] != 0)
                    for (int k = 0; k < 4; k++)
                    {
                        int ni = i + DX[k];
                        int nj = j + DY[k];
                        if (ni >= 0 && ni < N && nj >= 0 && nj < N && b[ni][nj] == b[i][j]) 
                            c[i][j][k] = c[ni][nj][k]+1;
                        else
                            c[i][j][k] = 1;
                        if (c[i][j][k] >= M)
                        {
                            if (b[i][j] > 0)
                                winred = true;
                            else
                                winblue = true;
                        }
                    }
        }
        output << "Case #" << casenum+1 << ": ";
        if (winred)
            if (winblue)
                output << "Both" << endl;
            else
                output << "Red" << endl;
        else
            if (winblue)
                output << "Blue" << endl;
            else
                output << "Neither" << endl;
    }
    input.close();
    output.close();
    return 0;
}
