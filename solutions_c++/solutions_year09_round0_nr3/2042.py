// CodeJam 2009 - P3
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

//-------------------------------------------------------------------------
unsigned countCombinations(vector<vector<unsigned> >& _locations, unsigned _ndx = 0, int _pos = -1)
{
    if (_ndx >= _locations.size())
        return 1;

    unsigned ret = 0;
    vector<unsigned>& positions = _locations[_ndx];
    for (unsigned i = 0; i < positions.size(); ++i)
    {
        int curPos = (int)positions[i];
        if (curPos > _pos)
            ret += countCombinations(_locations, _ndx+1, curPos);
    }
    
    return ret;
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
    
    unsigned N;
    fin >> N;
    fin.ignore();

    string welcome = "welcome to code jam";

    for (unsigned n = 0; n < N; ++n)
    {
        char str[500];
        fin.getline(str, 500);
        string text = str;

        vector<vector<unsigned> > locations;
        locations.reserve(welcome.length());
        for (unsigned i = 0; i < welcome.length(); ++i)
        {
            locations.push_back(vector<unsigned>());
            locations.back().reserve(text.length());
            char c = welcome[i];

            for (unsigned j = 0; j < text.length(); ++j)
            {
                if (c == text[j])
                    locations.back().push_back(j);
            }
        }

        unsigned count = countCombinations(locations);
        count %= 10000;
        fout << "Case #" << n+1 << ": ";
        fout.width(4);
        fout.fill('0');
        fout << internal << count  << endl;
    }

    fout.close();

    return 0;
}
