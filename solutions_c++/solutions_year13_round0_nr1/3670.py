#include <iostream>
#include <vector>
#include <string>

using namespace std;

void  tomek(vector<string> grid);

int main () {
    int nEntries;
    string s;
    
    cin >> nEntries;
    
    for(int i=0;i<nEntries;i++) {
        vector<string> grid;
        for(int l=0; l<4;l++) {
            cin >> s;
            grid.push_back(s);
        }
        
        cout << "Case #" << i+1 << ": ";
        tomek(grid);
        cout << endl;
    }
    return 0;
}

int nEquals(vector<string> grid,char c,int y,int x,int yToAdd,int xToAdd) {
    if((x >= 4) || (y >= 4) || (y < 0)|| (x < 0) )
        return 0;
    
    if(grid[y][x] == '.')
        return 0;
    else if(grid[y][x] == 'T')
        return nEquals(grid, c, y+yToAdd, x+xToAdd, yToAdd, xToAdd) + 1;
    else {
        if(c == 'T') {
            return nEquals(grid, grid[y][x], y+yToAdd, x+xToAdd, yToAdd, xToAdd) + 1;
        } else {
            if(grid[y][x] == c)
                return nEquals(grid, c, y+yToAdd, x+xToAdd, yToAdd, xToAdd) + 1;
        }
    }
}

void tomek(vector<string> grid) {
    for(int x=0;x<4;x++) {
        if(nEquals(grid,grid[0][x],0,x,1,0) == 4) {
            char c;
            if(grid[0][x] != 'T')
                c = grid[0][x];
            else
                c = grid[1][x];
            cout << c << " won";
            return;
        }
    }
    
    for(int y=0;y<4;y++) {
        if(nEquals(grid,grid[y][0],y,0,0,1) == 4) {
            char c;
            if(grid[y][0] != 'T')
                c = grid[y][0];
            else
                c = grid[y][1];
            cout << c << " won";
            return;
        }
    }
    
    if(nEquals(grid,grid[0][0],0,0,1,1) == 4) {
        char c;
        if(grid[0][0] != 'T')
            c = grid[0][0];
        else
            c = grid[1][1];
        cout << c << " won";
        return;
    }
    
    if(nEquals(grid,grid[0][3],0,3,1,-1) == 4) {
        char c;
        if(grid[0][3] != 'T')
            c = grid[0][3];
        else
            c = grid[1][2];
        cout << c << " won";
        return;
    }
    
    bool theresPoints=false;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(grid[i][j] == '.')
                theresPoints=true;
                
    if(theresPoints)
        cout << "Game has not completed";
    else
        cout << "Draw";
}


















