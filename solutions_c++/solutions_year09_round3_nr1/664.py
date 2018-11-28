// CodeJam 2009 - Round1C_A
// Autor: Benjamín de la Fuente Ranea

#include <Windows.h>
#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <string>
#include <algorithm>

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
set<char> countDifferentChars(const string& alienNumber)
{
    set<char> differentChars;
    for (unsigned i = 0; i < alienNumber.length(); ++i)
    {
        differentChars.insert(alienNumber[i]);
    }

    return differentChars;
}

//-------------------------------------------------------------------------
map<char, unsigned> mapChars(const string& alienNumber, char _first, char _second)
{
    map<char, unsigned> mapped;
    mapped[_first] = 1;
    if (_second != _first)
        mapped[_second] = 0;

    unsigned nextNumber = 2;
    for (unsigned i = 2; i < alienNumber.length(); ++i)
    {
        map<char, unsigned>::iterator iter = mapped.find(alienNumber[i]);
        if (iter == mapped.end())
        {
            mapped[alienNumber[i]] = nextNumber++;
        }
    }

    return mapped;
}

//-------------------------------------------------------------------------
unsigned long long countBase(map<char, unsigned>& mapped, const string& alienNumber, unsigned base)
{
    unsigned long long res = 0;
    for (unsigned i = 0; i < alienNumber.length(); ++i)
    {
        res += mapped[alienNumber[i]] * (unsigned long long)pow(long double(base), long double(alienNumber.length()-i-1));
    }

    return res;
}

//-------------------------------------------------------------------------
char findNext(unsigned pos, const string& alienNumber, char first)
{
    for (unsigned i = pos; i < alienNumber.length(); ++i)
    {
        if (alienNumber[i] != first)
            return alienNumber[i];
    }
    return first;
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
        string alienNumber;
        fin >> alienNumber;

        set<char> chars = countDifferentChars(alienNumber);
        map<char, unsigned> mapped = mapChars(alienNumber, alienNumber[0], findNext(1, alienNumber, alienNumber[0]));
        
        unsigned long long res = countBase(mapped, alienNumber, max(chars.size(), 2));
        fout << "Case #" << t+1 << ": " << res << endl;
    }

    fout.close();

    return 0;
}
