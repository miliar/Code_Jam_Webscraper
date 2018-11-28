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

//-------------------------------------------------------------------------
bool testPattern(const vector<string>& _pattern, const string& _word, unsigned _ndx = 0)
{
    if (_ndx >= _pattern.size())
        return true;

    char cw = _word[_ndx];
    for (unsigned i = 0; i < _pattern[_ndx].length(); ++i)
    {
        char cp = _pattern[_ndx][i];
        if (cp == cw && testPattern(_pattern, _word, _ndx+1))
            return true;
    }

    return false;
}

//-------------------------------------------------------------------------
unsigned checkDictionary(const vector<string>& _dictionary, const vector<string>& _pattern)
{
    unsigned ret = 0;
    for (unsigned i = 0; i < _dictionary.size(); ++i)
    {
        if (testPattern(_pattern, _dictionary[i]))
            ++ret;
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
    
    vector<string> dictionary;  // Dictionary
    dictionary.reserve(5000);
    
    unsigned L, D, N;
    fin >> L >> D >> N;
    for (unsigned i = 0; i < D; ++i)
    {
        char str[15];
        fin >> str;
        dictionary.push_back(str);
    }

    for (unsigned i = 0; i < N; ++i)
    {
        // Parser
        vector<string> pattern;
        for (unsigned l = 0; l < L; ++l)
        {
            char c;
            fin >> c;
            if (c == '(')
            {
                pattern.push_back("");
                fin >> c;
                while (c != ')')
                {
                    pattern.back() += c;
                    fin >> c;
                }
            }
            else
            {
                pattern.push_back("");
                pattern.back() += c;
            }
        }

        fout << "Case #" << i+1 << ": " << checkDictionary(dictionary, pattern) << endl;
    }

    fout.close();

    return 0;
}
