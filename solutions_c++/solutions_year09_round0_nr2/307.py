#include <fstream>
#include <iostream>
#include <stack>
#include <map>
#include <vector>
#include <list>
#include <queue>
using namespace std;

int dx[5] = {-1,0,0,1,0};
int dy[5] = {0,-1,1,0,0};
typedef pair<int,int> pii;

int main(){
    ofstream DEB("debug.txt");
    int Casos;
    cin >> Casos;
    for (int caso = 1; caso <= Casos; caso++){
        int N, M;
        cin >> N >> M;
        vector<vector<int> > H(N, vector<int> (M));
        vector<vector<int> > donde(N, vector<int> (M, 4));
        vector<vector<int> > color(N, vector<int> (M, 0));
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                cin >> H[i][j];
        int colores = 1;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++){
                for(int k = 0; k < 4; k++)
                    if (i+dx[k] >= 0 && i+dx[k] < N)
                    if (j+dy[k] >= 0 && j+dy[k] < M)
                    if (H[i+dx[k]][j+dy[k]] < H[i+dx[donde[i][j]]][j+dy[donde[i][j]]])
                        donde[i][j] = k;
                if (donde[i][j] == 4)
                    color[i][j] = colores++;
            }
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++){
                int x = i, y = j;
                stack<pii> st;
                while(!color[x][y]){
                    st.push(pii(x,y));
                    int xx = x+dx[donde[x][y]], yy = y+dy[donde[x][y]];
                    x = xx, y = yy;
                }
                int col = color[x][y];
                while(!st.empty()){
                    pii P = st.top(); st.pop();
                    x = P.first, y = P.second;
                    color[x][y] = col;
                }
            }
        cout << "Case #" << caso << ":\n";
        map<int, int> E;
        int c = 'a';
        DEB << "Caso numero " << caso << endl;
        DEB << "Original:" << endl;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++) DEB << H[i][j] << ' ';
            DEB << endl;
        }
        DEB << "Mapeado:" << endl;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if (!E.count(color[i][j]))
                    E[color[i][j]] = c++;
                DEB << char(E[color[i][j]]) << ' ';
            }
            DEB << endl;
        }
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M-1; j++){
                if (!E.count(color[i][j]))
                    E[color[i][j]] = c++;
                cout << char(E[color[i][j]]) << ' ';
            }
            if (!E.count(color[i][M-1]))
                E[color[i][M-1]] = c++;
            cout << char(E[color[i][M-1]]) << endl;
        }
    }
    return 0;
}
