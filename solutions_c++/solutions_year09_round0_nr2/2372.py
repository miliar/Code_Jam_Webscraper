#include <iostream>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

const int INF = 100*1000;
const int SIZE = 101;
char basins[SIZE][SIZE];
vector< pair<int,int> > Adj[SIZE][SIZE];

void DFS(int,int,int,int,char);

bool check(int i, int j, int H, int W) {
    return (i>=0 && i<H && j>=0 && j<W);
}

int main()
{
    ifstream fin("B.in");
    ofstream fout("B.out");

    int RowDir[4] = { -1, 0, 0, 1 };
    int ColDir[4] = { 0, -1, 1, 0 };

    int T; fin>>T;
    for(int x=1; x<=T; x++) {
        int H,W; fin>>H>>W;
        int M[SIZE][SIZE];

        for(int i=0; i<H; i++)
            for(int j=0; j<W; j++) {
                fin>>M[i][j];
                basins[i][j]='0';
                Adj[i][j].clear();
            }


        for(int i=0; i<H; i++) {
            for(int j=0; j<W; j++) {
                int min=INF;
                pair<int,int> minNeighbor(-1, -1);
                for(int k=0; k<4; k++) {
                    int r=i+RowDir[k], c=j+ColDir[k];
                    if(check(r,c,H,W) && M[r][c]<min) {
                        minNeighbor.first = r;
                        minNeighbor.second = c;
                        min = M[r][c];
                    }
                }
                if(M[i][j]>min) {
                    Adj[i][j].push_back(minNeighbor);
                    Adj[minNeighbor.first][minNeighbor.second].push_back(make_pair(i,j));
                }
/*                else if(M[i][j]==min) {
                    for(int k=0; k<4; k++) {
                        if(check(i+RowDir[k],j+ColDir[k],H,W) && M[i+RowDir[k]][j+ColDir[k]]<M[i][j]) {
                            Adj[i][j].push_back(make_pair(i+RowDir[k],j+ColDir[k]));
                            Adj[i+RowDir[k]][j+ColDir[k]].push_back(make_pair(i,j));
                        }
                    }
                }*/
            }
        }

        char basin = 'a';
        for(int i=0; i<H; i++) for(int j=0; j<W; j++) {
            if(basins[i][j]=='0') {
                DFS(i,j,H,W,basin);
                basin++;
            }
        }

        fout<<"Case #"<<x<<":"<<endl;
        for(int i=0; i<H; i++) {
            fout<<basins[i][0];
            for(int j=1; j<W; j++) {
                fout<<" "<<basins[i][j];
            }
            fout<<endl;
        }
    }

    fin.close();
    fout.close();
    return 0;
}

void DFS(int i, int j, int H, int W, char basin)
{
    bool Visited[SIZE][SIZE];
    for(int i=0; i<H; i++) for(int j=0; j<W; j++) Visited[i][j]=false;

    int Stack[SIZE*SIZE][2]; int cnt=0;
    Stack[0][0]=i; Stack[0][1]=j;
    cnt++;

    while(cnt>0) {
        cnt--;
        int r=Stack[cnt][0], c=Stack[cnt][1];

        basins[r][c] = basin;

        for(int i=0; i<Adj[r][c].size(); i++) {
            int r1=Adj[r][c][i].first, c1=Adj[r][c][i].second;
            if(Visited[r1][c1]) continue;
            Stack[cnt][0]=r1;
            Stack[cnt][1]=c1;
            Visited[r1][c1] = true;
            cnt++;
        }
    }
}