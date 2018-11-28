#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

#define MAX 51

const char outfile[] = "tiles.out";

char Tiles[MAX][MAX];

void initTiles()
{
    for(int i = 0; i < MAX; ++i)
        for (int j = 0; j < MAX ; ++j)
            Tiles[i][j] = '\0';
}

bool replace(int r, int c)
{
    for (int i = 0 ; i < r - 1; ++i)
    {
        for (int j = 0; j < c - 1; ++j)
        {
            if (Tiles[i][j] == '#')
            {
                if ((Tiles[i + 1][j] == '#') && (Tiles[i + 1][j + 1] == '#') && (Tiles[i][j + 1] == '#'))
                {
                    Tiles[i][j] = '/';
                    Tiles[i + 1][j] = '\\';
                    Tiles[i + 1][j + 1] = '/';
                    Tiles[i][j + 1] = '\\';
                }
                else
                    return false;
            }
        }
    }
    for (int i = 0; i < r; ++i)
        for (int j = 0; j < c; ++j)
            if (Tiles[i][j] == '#')
                return false;
    return true;
}

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        return 1;
    }
    std::ifstream file(argv[1]);
    int nCases;
    file >> nCases;
    std::ofstream res(outfile);

    for (int index = 1; index <= nCases; ++index)
    {
        initTiles();
        res << "Case #" << index << ":" << std::endl;
        int r, c;
        file >> r >> c;

        for (int rc = 0; rc < r; ++rc)
        {
            for (int cc = 0; cc < c ; ++cc)
                file >> Tiles[rc][cc];
        }


        if (replace(r,c))
        {
            for (int i = 0; i < r; ++i)
            {
                for (int j = 0; j < c; ++j)
                    res << Tiles[i][j];
                res << std::endl;
            }
        }
        else
        {
            res << "Impossible" << std::endl;
        }
    }
    return 0;
}   