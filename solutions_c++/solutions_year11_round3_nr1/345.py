#include<fstream>
#include<iostream>
#include<vector>
#include<iomanip>
#include<math.h>

using namespace std;

ifstream in("A-large.in");
ofstream out("output.txt");

int T;
vector<vector<char> > grid;

inline bool good_cell(int r, int c)
{
    return (r < grid.size() && c < grid[0].size() && grid[r][c]);
}

int main()
{
    in >> T;
    for(int test = 0; test < T; test++)
    {
        int R, C;
        in >> R >> C;
        grid = vector<vector<char> >(R, vector<char>(C));
        int blue = 0;
        for(int r = 0; r < R; r++)
            for(int c = 0; c < C; c++)
            {
                in >> grid[r][c];
                blue += (grid[r][c] == '#');
            }
        out << "Case #" << (test + 1) << ":" << endl;
        if(blue % 4 != 0)
            out << "Impossible" << endl;
        else if(blue == 0)
        {
            for(int r = 0; r < R; r++)
            {
                for(int c = 0; c < C; c++)
                    out << '.';
                out << endl;
            }
        }
        else
        {
            bool possible = true;
            for(int r = 0; r < R; r++)
                for(int c = 0; c < C; c++)
                    if(grid[r][c] == '#')
                    {
                        if(good_cell(r, c + 1)
                        && good_cell(r + 1, c)
                        && good_cell(r + 1, c + 1))
                        {
                            grid[r][c] = grid[r+1][c+1] = '/';
                            grid[r + 1][c] = grid[r][c + 1] = '\\';
                        }
                        else
                            possible = false;
                    }
            if(!possible)
                out << "Impossible" << endl;
            else
            {
                for(int r = 0; r < R; r++)
                {
                    for(int c = 0; c < C; c++)
                        out << grid[r][c];
                    out << endl;
                }
            }
        }
    }
    return 0;
}
