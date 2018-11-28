#include <iostream>
#include <vector>
using namespace std;

char label[100][100];
int board[100][100];
int movei[4] = {-1, 0, 0, 1}, movej[4] = {0, -1, 1, 0};
int c = 1;
int N, M;

int dfs(int i, int j)
{
    if (label[i][j] != 0) return label[i][j];
    
    pair<int, int> G[4];
    if (i != 0) G[0] = make_pair(board[i-1][j], 0); 
    else G[0] = make_pair(10001, 0);
    
    if (j != M-1) G[1] = make_pair(board[i][j+1], 2);
    else G[1] = make_pair(10001, 1);
    
    if (i != N-1) G[2] = make_pair(board[i+1][j], 3);
    else G[2] = make_pair(10001, 2);
    
    if (j != 0) G[3] = make_pair(board[i][j-1], 1);
    else G[3] = make_pair(10001, 3);
    
    sort(G, G + 4);
    
    if (G[0].first >= board[i][j]) return label[i][j] = c++;    
    return label[i][j] = dfs(i + movei[ G[0].second ], j + movej[ G[0].second ]);
}

int main()
{
    int T;
    cin >> T;
    for (int qq = 0; qq < T; qq++)
    {
        memset(label, 0, sizeof(label));
        c = 1;
        
        cin >> N >> M;
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++)
         cin >> board[i][j];
         
        for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) dfs(i, j);
        
        cout << "Case #" << qq+1 << ":\n";
        for (int i = 0; i < N; i++)
        {
            cout << (char)(label[i][0]+'a'-1);
            for (int j = 1; j < M; j++) cout << " " << (char)(label[i][j]+'a'-1);
            cout << endl;
        }
    }
    return 0;
    
}
