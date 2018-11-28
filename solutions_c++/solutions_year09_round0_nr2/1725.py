#include <algorithm>
#include <cassert>
#include <cctype>
#include <iostream>
#include <limits.h>
#include <string>

class Map
{
public:
    Map(int W, int H);
    ~Map();

    void parseInput();
    void computeBasins();
    void dumpBasins();

private:
    int getAltitude(int x, int y);
    char computeBasin(int x, int y);

    int mWidth;
    int mHeight;

    char mNextBasinLabel;

    int *mAltitudes;
    char *mBasins;
};

Map::Map(int W, int H)
    : mWidth(W)
    , mHeight(H)
    , mNextBasinLabel('a')
{
    mAltitudes = new int[mWidth * mHeight];
    memset(mAltitudes, INT_MAX, mWidth * mHeight * sizeof(int));

    mBasins = new char[mWidth * mHeight];
    memset(mBasins, '-', mWidth * mHeight * sizeof(char));
}

Map::~Map()
{
    if (mAltitudes != NULL)
    {
        delete[] mAltitudes;
        mAltitudes = NULL;
    }
    if (mBasins != NULL)
    {
        delete[] mBasins;
        mBasins = NULL;
    }
}

void Map::parseInput()
{
    for (int y = 0; y < mHeight; y++)
    {
        for (int x = 0; x < mWidth; x++)
        {
            std::cin >> mAltitudes[y*mWidth+x];
        }
    }
}

void Map::computeBasins()
{
    mNextBasinLabel = 'a';
    for (int y = 0; y < mHeight; y++)
    {
        for (int x = 0; x < mWidth; x++)
        {
            computeBasin(x, y);
        }
    }
}

void Map::dumpBasins()
{
    for (int y = 0; y < mHeight; y++)
    {
        for (int x = 0; x < mWidth; x++)
        {
            if (x > 0)
            {
                std::cout << " ";
            }
            std::cout << mBasins[y*mWidth+x];
        }
        std::cout << std::endl;
    }
}

char Map::computeBasin(int x, int y)
{
    assert(x >= 0);
    assert(y >= 0);
    assert(x < mWidth);
    assert(y < mHeight);

    // simply use the cached label if it has already been computed
    {
        const char cached_label = mBasins[y*mWidth+x];
        if (cached_label != '-')
        {
            return cached_label;
        }
    }

    const int current_altitude = getAltitude(x, y);
    const int north_altitude = getAltitude(x, y-1);
    const int west_altitude = getAltitude(x-1, y);
    const int east_altitude = getAltitude(x+1, y);
    const int south_altitude = getAltitude(x, y+1);

    const int lowest_altitude = 
        std::min(north_altitude,
        std::min(west_altitude,
        std::min(east_altitude, 
        std::min(south_altitude, current_altitude))));

    char basin_label = '-';
    if (lowest_altitude == current_altitude)
    {
        assert(std::isalpha(mNextBasinLabel));
        basin_label = mNextBasinLabel;
        mNextBasinLabel++;
    }
    else if (lowest_altitude == north_altitude)
    {
        basin_label = computeBasin(x, y-1);
    }
    else if (lowest_altitude == west_altitude)
    {
        basin_label = computeBasin(x-1, y);
    }
    else if (lowest_altitude == east_altitude)
    {
        basin_label = computeBasin(x+1, y);
    }
    else if (lowest_altitude == south_altitude)
    {
        basin_label = computeBasin(x, y+1);
    }

    // memoize the computed label
    mBasins[y*mWidth+x] = basin_label;

    return basin_label;
}

int Map::getAltitude(int x, int y)
{
    if (x < 0) return INT_MAX;
    if (y < 0) return INT_MAX;
    if (x >= mWidth) return INT_MAX;
    if (y >= mHeight) return INT_MAX;
    return mAltitudes[y*mWidth+x];
}

int main()
{
    int T;
    std::cin >> T; // number of maps

    for (int i = 0; i < T; i++)
    {
        int W, H;
        std::cin >> H;
        std::cin >> W;

        Map map(W, H);
        map.parseInput();
        map.computeBasins();

        std::cout << "Case #" << (i+1) << ":" << std::endl;
        map.dumpBasins();
    }

    return 0;
}

