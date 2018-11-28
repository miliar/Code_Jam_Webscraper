#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <cassert>
#include <ctime>
#include <list>

#include <mach/mach.h>
#include <mach/mach_time.h>

using namespace std;

char dictionary[256];

void learn(const string& googlerese, const string& english)
{
    assert(googlerese.length() == english.length());
    for (int i=0; i<googlerese.length(); ++i)
    {
        assert(dictionary[googlerese[i]] == 0 || dictionary[googlerese[i]] == english[i]);
        dictionary[googlerese[i]] = english[i];
    }
}

void parse(const string& line, ostream& out)
{
    for (int i=0; i<line.length(); ++i)
    {
        out << dictionary[line[i]];
    }
    out << endl;
}

void init()
{
    bzero(dictionary, 256);
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
    ifstream is("/users/manuel/Downloads/A-small-attempt1.in", ifstream::in);
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
    
    learn("y qee", "a zoo");
    learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
    learn("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
    learn("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
    dictionary['z'] = 'q';
    parse("a b c d e f g h i j k l m n o p q r s t u v w x y z", cout);
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

