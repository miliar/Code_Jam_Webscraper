#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

typedef long long ll;

void go(int caseNo)
{
    int R, C;
    cin >> R >> C;
    char tiles[R][C], output[R][C];
    bool visited[R][C];
    memset(visited, false, sizeof(visited));
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> tiles[i][j];
        }
    }

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C;j++) {
            if(tiles[i][j] == '.')
            {
                output[i][j] = tiles[i][j], visited[i][j] = true;
                continue;
            }
            if(!visited[i][j])
            {
                if(i+1 < R && j+1 < C)
                    if(tiles[i][j] == '#' && tiles[i+1][j] == '#' && tiles[i][j+1] == '#' && tiles[i+1][j+1] == '#')
                    {
                        visited[i][j] = visited[i+1][j] = visited[i][j+1] = visited[i+1][j+1] = true;
                        output[i][j] = output[i+1][j+1] = '/';
                        output[i+1][j] = output[i][j+1] = '\\';
                    }
            }
        }
    }

    int flag = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if(!visited[i][j])
            {
                flag = 1; break;
            }
        }
    }

    if(flag)
        cout << "Case #" << caseNo << ":\n" << "Impossible\n";
    else
    {
        cout << "Case #" << caseNo << ":\n";
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                cout << output[i][j];
            }
            cout << endl;
        }
    }
}

int main(int argc, const char *argv[])
{
    int T;
    cin >> T;
    int caseNum = 1;
    while(T--)
    {
        go(caseNum);
        caseNum++;
    }
    
    return 0;
}
