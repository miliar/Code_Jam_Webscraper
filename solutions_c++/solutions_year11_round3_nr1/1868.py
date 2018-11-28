#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <algorithm>

//#define DEBUG
//#define UNIT_TEST

// Algorithm:
// Maximize t, then c, sum s

// BUT if there's nothing in the deck, you need to maximize t, then s,  

struct Grid
{

typedef std::vector<char> row_t;
typedef row_t::iterator row_iter_t;
typedef std::vector<row_t> grid_t;
typedef grid_t::iterator grid_iter_t;

    Grid()
    {
    }

    void size(size_t r, size_t c)
    {
        R = r;
        C = c;
        mGrid.resize(r);
        for (grid_iter_t gIter = mGrid.begin(); 
             gIter != mGrid.end();
             ++gIter)
        {
            gIter->resize(c);
        }
    }

void replace_tiles()
{
    // greedy and dumb algorithm ... will it be enough?
    for (size_t r = 0; r < R; ++r)
    {
        for (size_t c = 0; c < C; ++c)
        {
            if (mGrid[r][c] == '#')
            {
                if (r+1 == R)
                    return;
                if (c+1 == C)
                    return;
                // forgot to check the rest were blue! Duh
                if (mGrid[r][c+1] != '#')
                    continue;
                if (mGrid[r+1][c] != '#')
                    continue;
                if (mGrid[r+1][c+1] != '#')
                    continue;
                mGrid[r][c] = '/';
                mGrid[r][c+1] = '\\';
                mGrid[r+1][c] = '\\';
                mGrid[r+1][c+1] = '/';
            }
        }
    }
}

bool has_any_blue()
{
    for (size_t r = 0; r < R; ++r)
    {
        for (size_t c = 0; c < C; ++c)
        {
            if (mGrid[r][c] == '#')
                return true;
//                std::cerr << mGrid[r][c];
        }
    }
    return false;
}

void print_result()
{
    replace_tiles();
    if (has_any_blue())
    {
        std::cout << "Impossible" << std::endl;
        return;
    }

    for (size_t r = 0; r < R; ++r)
    {
        for (size_t c = 0; c < C; ++c)
        {
            std::cout << mGrid[r][c];
        }
        std::cout << std::endl;
    }

}

    grid_t mGrid;
    size_t R;
    size_t C;
};


void output(Grid& result, size_t line)
{
    std::cout << "Case #" << line + 1 << ": " << std::endl;
    result.print_result();
}

int main()
{
#ifdef UNIT_TEST
#endif
    size_t numcases;
    std::cin >> numcases;
#ifdef DEBUG
    std::cout << numcases << " cases" << std::endl;
#endif
    for (size_t casex = 0; casex < numcases; ++casex)
    {
        size_t R, C;
        
        std::cin >> R >> C;
#ifdef DEBUG
        std::cout << "R: " << R << "C: " << C << std::endl;
#endif
        Grid g;
        g.size(R, C);

        for (size_t r = 0; r < R; ++r)
        {
            char val;
            for (size_t c = 0; c < C; ++c)
            {
                std::cin >> val;
                g.mGrid[r][c] = val;
            }
        }

        output(g, casex);
    }

    return 0;
}
