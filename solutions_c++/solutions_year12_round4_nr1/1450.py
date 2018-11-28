#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <map>

using namespace std;
typedef long long myint;
typedef std::map<std::pair<myint, unsigned>, int> memo_t;

bool
dfs(myint pos, unsigned vine, std::vector<myint> const& d, std::vector<myint> const& l, myint D, memo_t& memo)
{
    if (pos > D) return false;
    if (pos < 0) return false;

    unsigned nVines = d.size();

    memo_t::const_iterator it = memo.find(std::make_pair(pos,vine));
    if (it != memo.end())
    {
        return false;
    }

    myint r = d[vine] - pos;
    myint swing_length = r*2;

    if (r == 0)
        return false;

    // can reach
    if (pos + swing_length >= D)
    {
        return true;
    }

    //memo[std::make_pair(pos,vine)] = 2;

    for (unsigned iVine = 0; iVine < nVines; ++iVine)
    {
        bool bHit(false);

        if (iVine == vine) continue;

        if (swing_length >= 0 && pos < d[iVine] && pos + swing_length >= d[iVine])
            bHit = true;

        if (swing_length < 0 && pos > d[iVine] && pos + swing_length <= d[iVine])
            bHit = true;

        if (bHit)
        {
            myint newpos;
            if (swing_length > 0)
            {
                if (d[iVine] >= d[vine])
                {
                    newpos = max(d[vine],d[iVine] - l[iVine]);
                }
                else
                {
                    newpos = min(d[vine],d[iVine] + l[iVine]);
                }
            }
            else
            {
                if (d[iVine] >= d[vine])
                {
                    newpos = max(d[vine],d[iVine] - l[iVine]);
                }
                else
                {
                    newpos = min(d[vine],d[iVine] + l[iVine]);
                }
            }
            if (dfs(newpos,iVine,d,l,D, memo))
            {
                return true;
            }
        }
    }
    memo[std::make_pair(pos,vine)] = false;

    return false;
}

int main (int argc, char *argv)
{
    unsigned T;
    cin >> T;

    for (unsigned iCase = 1; iCase <= T; ++iCase)
    {
        unsigned N;
        cin >> N;
        std::vector<myint> d(N, 0);
        std::vector<myint> l(N, 0);

        for (unsigned i = 0; i < N; ++i) {cin >> d[i]; cin >> l[i]; }

        myint D;
        cin >> D;

        memo_t memo;
        if (dfs(0,0,d,l,D, memo))
        {
            std::cout << "Case #" << iCase << ": YES" << std::endl;
        }
        else
        {
            std::cout << "Case #" << iCase << ": NO" << std::endl;
        }
    }
}

