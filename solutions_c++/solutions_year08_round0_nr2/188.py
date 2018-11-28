#include <iostream>
#include <fstream>
#include <map>
//#include <pair>

using namespace std;

struct Train
{
    unsigned dep;
    unsigned arr;
};

typedef multimap<unsigned, unsigned> Events;

inline bool isnum(const char c)
{
    return ('0' <= c) && (c <= '9');
}

istream& seekeoln(istream& is)
{
    char c;
    do
    {
        is.get(c);
    } while (c != '\n');
    return is;
}

void parse_tt(istream &is, Train &t)
{
    char buf[120];
    is.getline(buf, 100);

    unsigned c = 0;
    unsigned hh, mm;
    
    while (!isnum(buf[c])) ++c;
    hh = (buf[c] - '0') * 10 + buf[c + 1] - '0'; c += 3;
    mm = (buf[c] - '0') * 10 + buf[c + 1] - '0'; c += 2;
    t.dep = hh * 60 + mm;
    
    while (!isnum(buf[c])) ++c;
    hh = (buf[c] - '0') * 10 + buf[c + 1] - '0'; c += 3;
    mm = (buf[c] - '0') * 10 + buf[c + 1] - '0'; c += 2;
    t.arr = hh * 60 + mm;
}

int main()
{
    ifstream is("test.in");
    
    unsigned nTests;
    seekeoln(is >> nTests);
    
    for (unsigned i = 0; i < nTests; ++i)
    {
        unsigned T;
        seekeoln(is >> T);
        
        unsigned a, b;
        seekeoln(is >> a >> b);
        
        Events arr;
        Events dep;
        unsigned ans[2];
        unsigned cur[2];
        ans[0] = ans[1] = cur[0] = cur[1] = 0;
        
        for (unsigned j = 0; j < a; ++j)
        {
            Train t;
            parse_tt(is, t);
            dep.insert(pair<unsigned, unsigned>(t.dep, 0));
            arr.insert(pair<unsigned, unsigned>(t.arr + T, 1));
        }
        
        for (unsigned j = 0; j < b; ++j)
        {
            Train t;
            parse_tt(is, t);
            dep.insert(pair<unsigned, unsigned>(t.dep, 1));
            arr.insert(pair<unsigned, unsigned>(t.arr + T, 0));
        }
        
        Events::const_iterator arrit = arr.begin();
        for (Events::const_iterator depit = dep.begin(); depit != dep.end(); ++depit)
        {
            while (arrit != arr.end() && arrit->first <= depit->first) 
            {
                ++cur[arrit->second];
                ++arrit;
            }
            if (cur[depit->second] == 0) 
                ++ans[depit->second];
            else
                --cur[depit->second];
        }
        cout << "Case #" << (i + 1) << ": " << ans[0] << " " << ans[1] << endl;
    }
    
    return 0;
}
