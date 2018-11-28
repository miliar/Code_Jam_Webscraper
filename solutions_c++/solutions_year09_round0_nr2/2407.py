#include <iostream>
#include <string>

using namespace std;

struct coord
{
    int x;
    int y;
};

void printBasins(char *basins[], int H, int W)
{
    for(int x = 0; x < H; x++)
    {
        for(int y = 0; y < W; y++)
        {
            cout << basins[x][y];
            
            if(y != W - 1)
            {
                cout << " ";
            }
        }
        cout << endl;
    }
}

coord findMin(int *maps[], int H, int W, int x, int y)
{
    int xMin, yMin;
    coord cMin;
    //int N, E, S, We;
    
    /*if(x > 0)
    {
        N = x - 1;
    }
    else
    {
        N = x;
    }
    if(x < H)
    {
        S = x + 1;
    }
    else
    {
        S = x;
    }
    if(y > 0)
    {
        We = y - 1;
    }
    else
    {
        We = y;
    }
    if(y < W)
    {
        E = y - 1;
    }
    else
    {
        E = y;
    }*/
    xMin = x;
    yMin = y;
    
    /*for(int a = N + 1; a < S; a++)//PROBLEM
    {
        for(int b = W + 1; b < E; b++)
        {
            if(maps[a][b] < maps[xMin][yMin])
            {
                xMin = a;
                yMin = b;
            }
        }
    }*/
    
    if(x > 0 && maps[x - 1][y] < maps[xMin][yMin])
    {
        xMin = x - 1;
        yMin = y;
    }
    if(y > 0 && maps[x][y - 1] < maps[xMin][yMin])
    {
        xMin = x;
        yMin = y - 1;
    }
    if(y < W - 1 && maps[x][y + 1] < maps[xMin][yMin])
    {
        xMin = x;
        yMin = y + 1;
    }
    if(x < H - 1 && maps[x + 1][y] < maps[xMin][yMin])
    {
        xMin = x + 1;
        yMin = y;
    }
    
    cMin.x = xMin;
    cMin.y = yMin;
    
    return cMin;
}

void findBasin(int *maps[], char *basins[], int H, int W, int x, int y, int &currentLetter)
{
    if(basins[x][y] == '\0')
    {
        coord cMin = findMin(maps, H, W, x, y);
        
        if(x == cMin.x && y == cMin.y)
        {
            basins[x][y] = (char)currentLetter;
            currentLetter++;
        }
        else
        {
            findBasin(maps, basins, H, W, cMin.x, cMin.y, currentLetter);
            basins[x][y] = basins[cMin.x][cMin.y];
        }
    }
}

void handleCase(int *maps[], int caseNum, int H, int W)
{
    char *basins[H];
    
    for(int x = 0; x < H; x++)
    {
        basins[x] = new char[W];
        for(int y = 0; y < W; y++)
        {
            basins[x][y] = '\0';
        }
    }
    
    int currentLetter = 97; // ascii 'a'
    
    for(int x = 0; x < H; x++)
    {
        for(int y = 0; y < W; y++)
        {
            findBasin(maps, basins, H, W, x, y, currentLetter);
        }
    }
    
    cout << "Case #" << caseNum << ":" << endl;
    printBasins(basins, H, W);
}

int main(int argc, char *argv[])
{
    int T;
    
    cin >> T;
    
    int **maps[T];
    
    for(int x = 0; x < T; x++)
    {
        int H, W;
        
        cin >> H >> W;
        
        maps[x] = new int*[H];
        /*for(int y = 0; y < H; y++)
        {
            
        }*/
        
        for(int y = 0; y < H; y++)
        {
            maps[x][y] = new int[W];
            for(int z = 0; z < W; z++)
            {
                cin >> maps[x][y][z];
            }
        }
        
        handleCase(maps[x], x + 1, H, W);
    }
    
    return 0;
}
