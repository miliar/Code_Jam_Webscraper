#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <set>
#include <utility>
#include <string.h>
using namespace std;

const unsigned int num = 4;
const unsigned int line = 501;

const char * w = "welcome to code jam";
//string ww(w);

unsigned long count = 0;

void test( string s, int pos ) {
    for(;;) {
        string::size_type idx = s.find( w[pos] );
        if( idx == string::npos )
            break;
        else {
            //if( pos == (ww.length() - 1) )
            if( pos == (strlen(w) - 1) )
                ++count;
            string t = s.substr(idx+1);
            s = t;
            test( s, pos + 1);
        }
    }
}

int main( int argc, char *argv[]) {

    //ifstream finput("in.txt");
    ifstream finput(argv[1]);

    char n[num] = {0,};
    char l[line] = {0,};

    finput.getline(n, num);

    unsigned int nn = 0;
    char *p = &n[0];
    while( *p ){ 
        nn = nn * 10 + *p - '0';
        ++p;
    }

    cout << nn << endl;

    string ww(w);
    ofstream foutput("out");
    for( int i = 0; i < nn; ++i ) {
        finput.getline(l, line);
        //cout << l << endl;

        string ll(l);
        count = 0;
        test(ll, 0 );

        foutput << "Case #" << i+1 << ": " << setw(4) << setfill('0') << count % 10000 << endl;
    }

    return 0;
}
