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

void parse(const string& line, ostream& out)
{
    stringstream ss(line);
    int A;
    int B;
    ss >> A >> B;
    string m;
    string n;
    int value = 0;
    for (int i=A+1; i<=B; ++i)
    {
        stringstream ss2;
        ss2.clear();
        ss2 << i;
        m = ss2.str() + ss2.str();
        for (int j=A; j<i; ++j)
        {
            stringstream ss3;
            ss3.clear();
            ss3 << j;
            n = ss3.str();
            //cout << n << " " << m << endl;
            if (m.find(n) != string::npos)
            {
                ++value;
            }
        }
    }
    out << value << endl;
}

void init()
{
}

int main(int argc, const char * argv[])
{
    // See http://developer.apple.com/library/mac/#qa/qa1398/_index.html for the time measuring code
    uint64_t start;
    uint64_t end;
    uint64_t elapsed;
    uint64_t elapsedNano;
    static mach_timebase_info_data_t sTimebaseInfo;
    start = mach_absolute_time();
    getpid();
    
    init();
    ifstream is("/users/manuel/Downloads/C-small-attempt0.in", ifstream::in);
    ofstream os("/users/manuel/Downloads/out.txt", ifstream::out);
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

