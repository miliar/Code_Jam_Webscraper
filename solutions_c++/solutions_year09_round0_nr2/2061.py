// CodeJam 2009 - Practice 1
// Autor: Benjamín de la Fuente Ranea

#include <Windows.h>
#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

//-------------------------------------------------------------------------
void log(const char* fmt, ...)
{
    const unsigned MAX_LINE_BUFFER = 512;
    char    buf[MAX_LINE_BUFFER];			// Is supposed that MAX_LINE_BUFFER characters are enough.
    va_list arg;
    va_start(arg, fmt);
    vsprintf_s<MAX_LINE_BUFFER>(buf, fmt, arg);
    va_end(arg);
    printf(buf);
    OutputDebugStr(buf);
}

static char g_label = 'a';

//-------------------------------------------------------------------------
pair<unsigned, unsigned> findBasin(unsigned _h, unsigned _w, const vector<vector<unsigned>>& _terrain, vector<vector<char>>& _basins)
{
    // Check the neighbours
    unsigned curHeight = _terrain[_h][_w];
    unsigned minHeight = curHeight;
    unsigned minH = _h;
    unsigned minW = _w;
    if (_h > 0)
    {
        // North
        unsigned northHeight = _terrain[_h-1][_w];
        if (northHeight < minHeight)
        {
            minHeight = northHeight;
            minH = _h-1;
            minW = _w;
        }
    }
    if (_w > 0)
    {
        // West
        unsigned westHeight = _terrain[_h][_w-1];
        if (westHeight < minHeight)
        {
            minHeight = westHeight;
            minW = _w-1;
            minH = _h;
        }
    }
    if (_w < _terrain[_h].size()-1)
    {
        // East
        unsigned eastHeight = _terrain[_h][_w+1];
        if (eastHeight < minHeight)
        {
            minHeight = eastHeight;
            minW = _w+1;
            minH = _h;
        }
    }
    if (_h < _terrain.size()-1)
    {
        // South
        unsigned southHeight = _terrain[_h+1][_w];
        if (southHeight < minHeight)
        {
            minHeight = southHeight;
            minH = _h+1;
            minW = _w;
        }
    }

    if (minHeight == curHeight && _basins[_h][_w] == 0)
    {
        // Base case (basin)
        _basins[_h][_w] = g_label++;
        return pair<unsigned, unsigned>(_h, _w);
    }

    // Check if already calculated
    char lastCalc = _basins[minH][minW];
    if (lastCalc != 0)
    {
        _basins[_h][_w] = lastCalc;
        return pair<unsigned, unsigned>(minH, minW);
    }
    else
    {
        pair<unsigned, unsigned> basinCoords = findBasin(minH, minW, _terrain, _basins);
        _basins[minH][minW] = _basins[basinCoords.first][basinCoords.second];
        return pair<unsigned, unsigned>(minH, minW);
    }
}

//-------------------------------------------------------------------------
void generateBasins(const vector<vector<unsigned>>& _terrain, vector<vector<char>>& _basins)
{
    for (unsigned h = 0; h < _terrain.size(); ++h)
    {
        for (unsigned w = 0; w < _terrain[h].size(); ++w)
        {
            pair<unsigned, unsigned> basinCoords = findBasin(h, w, _terrain, _basins);
            _basins[h][w] = _basins[basinCoords.first][basinCoords.second];
        }
    }
}

//-------------------------------------------------------------------------
int main(int argc, const char* argv[])
{
    if (argc != 3)
    {
        log("Error: Usage %s [INPUT_FILE] [OUTPUT_FILE]\n", argv[0]);
        return 1;
    }

    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    unsigned T;
    fin >> T;

    for (unsigned t = 0; t < T; ++t)
    {
        g_label = 'a';
        vector<vector<unsigned>>    terrain;
        vector<vector<char>>        basins;

        unsigned H, W;
        fin >> H >> W;

        // reserver memory
        terrain.reserve(H);
        basins.reserve(H);
        for (unsigned h = 0; h < H; ++h)
        {
            terrain.push_back(vector<unsigned>());
            basins.push_back(vector<char>());
            terrain.back().reserve(W);
            basins.back().reserve(W);
            for (unsigned w = 0; w < W; ++w)
            {
                unsigned height;
                fin >> height;
                terrain.back().push_back(height);
                basins.back().push_back(0);     // Initialize to 0
            }
        }

        generateBasins(terrain, basins);

        fout << "Case #" << t+1 << ":" << endl;
        for (unsigned h = 0; h < terrain.size(); ++h)
        {
            for (unsigned w = 0; w < terrain[h].size(); ++w)
            {
                fout << basins[h][w] << " ";
            }
            fout << endl;
        }
    }

    fout.close();

    return 0;
}
