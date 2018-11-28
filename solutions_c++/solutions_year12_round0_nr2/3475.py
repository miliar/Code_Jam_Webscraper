#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <ctime>

#include <mach/mach.h>
#include <mach/mach_time.h>

using namespace std;

int maxscore_unsurprise[31];
int maxscore_surprise[31];
int total_points[101];

void init()
{
    for (int i=0; i<=30; ++i)
    {
        if (i % 3 == 0)
        {
            maxscore_unsurprise[i] = i / 3;
            maxscore_surprise[i] = i / 3 + 1;
            if (maxscore_surprise[i] >= i)
            {
                maxscore_surprise[i] = -1;
            }
        }
        else if (i % 3 == 1)
        {
            maxscore_unsurprise[i] = i / 3 + 1;
            maxscore_surprise[i] = i / 3 + 1;
            if (maxscore_surprise[i] >= i)
            {
                maxscore_surprise[i] = -1;
            }
        }
        else if (i % 3 == 2)
        {
            maxscore_unsurprise[i] = i / 3 + 1;
            maxscore_surprise[i] = i / 3 + 2;
            if (maxscore_surprise[i] > i)
            {
                maxscore_surprise[i] = -1;
            }
        }
        else
        {
            assert(0);
        }
    }
    maxscore_surprise[30] = -1;
    maxscore_surprise[29] = -1;

    for (int i=0; i<= 30; ++i)
    {
        cout << i;
        cout << ": " << maxscore_unsurprise[i];
        cout << " " << maxscore_surprise[i];
        cout << endl;
    }
}

void parse(const string& line, ostream& out)
{
    int googlers, surprises, p;
    stringstream ss(line);
    ss >> googlers >> surprises >> p;
    int i=0;
    while (ss >> total_points[i++]);
    assert(i <= 101);
    
    int accum_all = 0, accum_s_only = 0, accum_u_only = 0, accum_none = 0;
    for (i=0; i<googlers; ++i)
    {
        if (maxscore_surprise[total_points[i]] >= p)
        {
            if (maxscore_unsurprise[total_points[i]] >= p)
            {
                ++accum_all;
            }
            else
            {
                ++accum_s_only;
            }
        }
        else if (maxscore_unsurprise[total_points[i]] >= p)
        {
            ++accum_u_only;
        }
        else
        {
            ++accum_none;
        }
    }
    
    int result = 0;
    if (accum_s_only >= surprises)
    {
        result = surprises + accum_all + accum_u_only;
    }
    else
    {
        result += accum_s_only;
        surprises -= accum_s_only;
        if (accum_all >= surprises)
        {
            result += accum_all + accum_u_only;
        }
        else
        {
            result += accum_all;
            surprises -= accum_all;
            if (accum_none >= surprises)
            {
                result += accum_u_only;
            }
            else
            {
                surprises -= accum_none;
                assert(accum_u_only - surprises >= 0);
                result += accum_u_only - surprises;
            }
        }
    }
    if (result < 0)
        result = 0;
    out << result << endl;
}

int main(int argc, const char * argv[])
{
    cout << "Running..." << endl;
    
    // See http://developer.apple.com/library/mac/#qa/qa1398/_index.html for the time measuring code
    uint64_t start;
    uint64_t end;
    uint64_t elapsed;
    uint64_t elapsedNano;
    static mach_timebase_info_data_t sTimebaseInfo;
    start = mach_absolute_time();
    getpid();
    
    init();
    ifstream is("/Users/manuel/Desktop/B-large.in", ifstream::in);
    ofstream os("/Users/manuel/Desktop/out.txt", ifstream::out);
    string line;
    int t;
    if (getline(is, line))
    {
        stringstream ss(line);
        ss >> t;
        assert(!ss.fail());
    }
    else
    {
        assert(0);
    }
    
    for (int i=0; i<t; ++i)
    {
        os << "Case #" << i+1 << ": ";
        getline(is, line);
        parse(line, os);
    }
    
    end = mach_absolute_time();
    elapsed = end - start;
    if ( sTimebaseInfo.denom == 0 ) {
        (void) mach_timebase_info(&sTimebaseInfo);
    }
    elapsedNano = elapsed * sTimebaseInfo.numer / sTimebaseInfo.denom;
    cout << "Done in " <<  elapsedNano/1000000.0 << " ms" << endl;
    
    return 0;
}

