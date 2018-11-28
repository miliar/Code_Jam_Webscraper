#include <fstream>
#include <vector>

using namespace std;

int sink_count;
int sink[101][101];
int map[102][102];

int get_sink_index(int x, int y)
{
    int dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
    int minl;
    int dirp;
    if(sink[x][y] > 0) return sink[x][y];
    
    minl = map[x][y];
    for(int i = 0; i < 4; i++)
    {
        if(map[x+dir[i][0]][y+dir[i][1]] < minl)
        {
            minl = map[x+dir[i][0]][y+dir[i][1]];
            dirp = i;
        }
    }
    if(minl == map[x][y])
    {
        sink_count++;
        sink[x][y] = sink_count;
    }
    else
    {
        sink[x][y] = get_sink_index(x+dir[dirp][0], y+dir[dirp][1]);
    }
    return sink[x][y];
}

int main(int argc, char** argv)
{
    ifstream fin("B.in");
    ofstream fout("B.out");
    int t;
    fin >> t;
    for(int i = 0; i < t; i++)
    {
        int H, W;
        fin >> H >> W;
        for(int h = 1; h <= H; h++)
        {
            for(int w = 1; w <= W; w++)
            {
                fin >> map[h][w];
                sink[h][w] = 0;
            }
        }
        for(int h = 0; h <= H+1; h++)
        {
            map[h][0] = map[h][W + 1] = 20000;
        }
        for(int w = 0; w <= W+1; w++)
        {
            map[0][w] = map[H+1][w] = 20000;
        }
        
        sink_count = 0;
        for(int h = 1; h <= H; h++)
        {
            for(int w = 1; w <= W; w++)
            {
                sink[h][w] = get_sink_index(h, w);
            }
        }
        
        fout << "Case #" << i + 1 << ":" << endl;
        for(int h = 1; h <= H; h++)
        {
            for(int w = 1; w <= W; w++)
            {
                fout << (char)(sink[h][w] - 1 + 'a') << " ";
            }
            fout << endl;
        }
    } 
    
    fin.close();
    fout.close();
}