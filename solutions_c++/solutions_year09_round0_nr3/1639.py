#include <assert.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <set>
#include <limits>
#include <utility>
#include <stdlib.h>
#include <iomanip>

using namespace std;

typedef deque<size_t>   Pos;
typedef map<char, Pos>  PosMap;
typedef vector<Pos>     CharPos;

typedef map<pair<size_t, size_t>, size_t>   Cache;
Cache cache;

long long count(CharPos&charPos, size_t idx, size_t posBegin)
{
    if (idx >= charPos.size())
        return 1;

    Pos&    pos = charPos[idx];

    long long result = 0;
    for (Pos::iterator it = pos.begin();
         it != pos.end();
         ++it)
    {
        if (*it < posBegin)
            continue;

        if (cache.count(make_pair(idx, *it)))
        {
            result += cache[make_pair(idx, *it)];
        } else
        {
            long long r = count(charPos, idx+1, *it+1);
            result += r;
            cache[make_pair(idx, *it)] = r;
        }
    }

    return result;
}

long long solve(PosMap& posMap)
{
    string  str = "welcome to code jam";
    vector<Pos> charPos;
    cache.clear();

    for (size_t i=0; i<str.size(); ++i)
    {
        charPos.push_back(posMap[str[i]]);
    }

    for (size_t i=0; i<charPos.size(); ++i)
    {
        Pos&    pos = charPos[i];

        if (i > 0)
        {
            size_t low = charPos[i - 1].front();

            while (!pos.empty() && (pos.front() <= low))
                pos.pop_front();
        }

        if (pos.empty())
            return 0;
    }

    size_t i=str.size() - 2;
    do
    {
        Pos&    pos = charPos[i];
        size_t high = charPos[i+1].back();

        while (!pos.empty() && (pos.back() >= high))
            pos.pop_back();

        if (pos.empty())
            return 0;
    } while (i-- > 0);

    return count(charPos, 0, 0);
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
        PosMap  posMap;
        getline(fs, line);

        for (size_t i=0; i<line.size(); ++i)
        {
            posMap[line[i]].push_back(i);
        }

        long long result = solve(posMap);

        cout << "Case #" << caseNum << ": " << setw(4) << setfill('0') << (result % 10000) << endl;
    }

    return 0;
}
