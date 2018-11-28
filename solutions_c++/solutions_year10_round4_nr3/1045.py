
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int> >grid;
bool isAlive(){
    for(int i = 0; i < grid.size(); ++i){
        for(int j = 0; j < grid[0].size(); ++j){
            if(grid[i][j]) return true;
        }
    }
    return false;
}

void update(){
    vector<vector<int> > grid2 = grid;
    for(int i = 1; i < grid.size(); ++i){
        for(int j = 1; j < grid[0].size(); ++j){
            if(!(grid[i][j-1] || grid[i-1][j]) && grid[i][j]) grid2[i][j] = 0;
            else if(grid[i][j-1] && grid[i-1][j] && grid[i][j] == 0) grid2[i][j] = 1;
        }
    }
    grid = grid2;
}
int main()
{
    grid = vector<vector<int> >(101, vector<int>(101, 0));
    int T;
    cin >> T;
    for(int ii = 1; ii <= T; ++ii){
        int R;
        cin >> R;

        for(int i = 0; i < R; ++i){
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for(int j = x1; j <= x2; ++j){
                for(int k = y1; k <= y2; ++k){
                    grid[j][k] = 1;
                }
            }
        }
        int turns = 0;
        while (isAlive()){
            turns++;
            update();
        }
        cout << "Case #" << ii << ": " << turns << endl;
    }
    return 0;
}
