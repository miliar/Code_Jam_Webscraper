//SS helper v2.2
#include <iostream>
#include <iomanip>
#include <fstream>
#include <iterator>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <math.h>
#include <cassert>

using namespace std;

typedef vector<string>      VS;
typedef vector<int>         VI;
typedef vector<double>      VD;
typedef vector<float>       VF;
typedef vector<char>        VC;

namespace Utils
{
#define CLR(x) memset((x), 0, sizeof(x))
#define ALL(x) (x).begin(), (x).end()
    
#define FOR(i, s, n) for(int i = (int)(s), cn = (int)(n); i < cn; ++i)
#define RFOR(i, s, n) for(int i = (int)(n) - 1, cs = (int)(s); i >= cs; --i)
    
#define FORN(i, n) FOR(i, 0, n)
#define RFORN(i, n) RFOR(i, 0, n)
    
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define RFORI(it, x) for (__typeof((x).rbegin()) it = (x).rbegin(); it != (x).rend(); it++)
    
    
#define FILL_VECTOR(vec, values)                        \
{                                                       \
const int size = sizeof(values) / sizeof(values[0]);    \
vec.resize(size);                                       \
cout << size << endl;                                   \
FORN(i, size)                                           \
vec[i] = values[i];                                     \
}    
    
    void split_string(string& data, VS& result)
    {
        result.clear();
        //add apendix tab for normal parsing
        data += " ";
        int start_pos = 0, end_pos = 0;
        while ((end_pos = data.find(" ", start_pos)) != string::npos)
        {
            result.push_back(data.substr(start_pos, end_pos - start_pos));
            start_pos = end_pos + 1;
        }
    }
    
    VS split_string(string data)
    {
        VS result;
        //add apendix tab for normal parsing
        data += " ";
        int start_pos = 0, end_pos = 0;
        while ((end_pos = data.find(" ", start_pos)) != string::npos)
        {
            result.push_back(data.substr(start_pos, end_pos - start_pos));
            start_pos = end_pos + 1;
        }
        
        return result;
    }
    
    template <typename T> inline string to_str(const T& a) 
    { 
        ostringstream os(""); 
        os << a; 
        return os.str(); 
    }
    
    template <typename T> inline string to_str(const vector<T> &a) 
    { 
        ostringstream os(""); 
        FORN(i, a.size())
        {
            os << a[i];
            if (i != a.size() - 1)
                os << " ";
        }
        return os.str(); 
    }
    
    template <typename T> inline T sum(const vector<T> &a)
    {
        T result = 0;
        FORN(i, a.size())
        result += a[i];
        return result;
    }
    
    template <typename T> inline void dump(const vector<T> &a)
    {
        FORN(i, a.size())
        cerr << a[i] << "  ";
        cerr << endl;
    }    
};
//------------------------------------------------------------------------------------------------

VI d(10000, 0), l(10000, 0);


bool try_reach(int i, int dd, int D, int N)
{
    int maxl = d[i] + min(dd, l[i]);
    if (maxl >= D)
        return true;
    int j = i + 1;
    while (j <= N && d[j] <= maxl)
    {
        j++;
    }
    j--;
    
    for (; j > i; j--)
    {
        if (try_reach(j, d[j] - d[i], D, N))
            return true;
    }
    return false;
}

int main (int argc, const char * argv[])
{
    VS lines;
    ifstream dat ("test.in");
    if (dat.is_open())
    {
        string line;
        while (dat.good())
        {
            getline (dat, line);
            if (line.empty())
                continue;
            lines.push_back(line);
        }
        dat.close();
    }  
    const int T = atoi(lines[0].c_str());
    cout << "Loaded " << T << " cases" << endl;
    
    int index = 1;
    ofstream res("test.out");
    FORN(t, T)
    {
        res  << "Case #" << t + 1 << ": ";
        VS data = Utils::split_string(lines[index++]);
        int N = atoi(data[0].c_str());
        d.assign(10000, 0);
        l.assign(10000, 0);
        FORN(i, N)
        {
            data = Utils::split_string(lines[index++]);
            d[i] = atoi(data[0].c_str());
            l[i] = atoi(data[1].c_str());
        }
        int D = atoi(lines[index++].c_str());
        //adjust 1split_string
        l[0] = d[0];
        if (try_reach(0, d[0], D, N))
            res << "YES" << endl;
        else
            res << "NO" << endl;
    }
    res.close();
    
    return 0;
}


