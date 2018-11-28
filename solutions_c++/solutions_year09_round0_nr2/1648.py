#include <assert.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <limits>
#include <utility>
#include <stdlib.h>

using namespace std;

static const size_t MAX_H = 200;
static const size_t MAX_W = 200;
static const int    MM = numeric_limits<int>::max();

struct Status
{
    vector<Status*> from;
    Status*         sink;
    char            label;

    Status()
    {
        Reset();
    }

    void Reset()
    {
        from.resize(0);
        sink = NULL;
        label = 0;
    }

};

int themap[MAX_W+2][MAX_H+2];

void fill(Status sinks[MAX_W+2][MAX_H+2], Status* curr, Status* sink)
{
    curr->sink = sink;
    for (size_t i=0; i<curr->from.size(); ++i)
        fill(sinks, curr->from[i], sink);
}

void solve(size_t w, size_t h)
{
    Status  result[MAX_W+2][MAX_H+2];
    vector<Status*> sinks;

    for (size_t y=1; y<=h; ++y)
    {
        for (size_t x=1; x<=w; ++x)
        {
            int low = themap[x][y];
            Status* to = NULL;

            if (low > themap[x][y-1])
            {
                low = themap[x][y-1];
                to = &result[x][y-1];
            }

            if (low > themap[x-1][y])
            {
                low = themap[x-1][y];
                to = &result[x-1][y];
            }

            if (low > themap[x+1][y])
            {
                low = themap[x+1][y];
                to = &result[x+1][y];
            }

            if (low > themap[x][y+1])
            {
                low = themap[x][y+1];
                to = &result[x][y+1];
            }

            if (!to)
            {
                sinks.push_back(&result[x][y]);
            } else
            {
                to->from.push_back(&result[x][y]);
            }
        }
    }

    for (size_t i=0; i<sinks.size(); ++i)
    {
        fill(result, sinks[i], sinks[i]);
    }

    char label = 'a';
    for (size_t y=1; y<=h; ++y)
    {
        for (size_t x=1; x<=w; ++x)
        {
            if (!result[x][y].sink->label)
                result[x][y].sink->label = label++;

            cout << result[x][y].sink->label << " ";
        }
        cout << endl;
    }
}

int main(int argc, const char* argv[])
{
    clog.rdbuf(NULL);

    fstream fs(argv[1]);

    if (!fs)
        return 1;

    string line;

    size_t caseCount;

    fs >> caseCount;
    getline(fs,line);

    clog << "CaseCount: " << caseCount << endl;

    for (size_t caseNum=1; caseNum<=caseCount; ++caseNum)
    {
        size_t w, h;
        fs >> h >> w;
        getline(fs, line);

        clog << "width:" << w << " height:" << h << endl;

        for (size_t y=0; y<MAX_H; ++y)
        {
            for (size_t x=0; x<MAX_W; ++x)
            {
                themap[x][y] = MM;
            }
        }

        for (size_t y=1; y<=h; ++y)
        {
            for (size_t x=1; x<=w; ++x)
            {
                fs >> themap[x][y];
            }
            getline(fs, line);
        }

        cout << "Case #" << caseNum << ": " << endl;
        solve(w, h);
    }

    return 0;
}
