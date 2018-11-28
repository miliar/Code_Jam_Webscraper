#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <queue>
#include <list>
using namespace std;

const unsigned int num = 15;
const unsigned int def = 20;
const unsigned int line = (26+2)*15+2;

int main( int argc, char *argv[]) {

    //ifstream finput("in.txt");
    ifstream finput(argv[1]);
    ofstream foutput("out");

    char cn[num] = {0,};

    finput.getline(cn, num);

    istringstream iss(cn);
    string a, b, c;
    iss >> a >> b >> c;

    //cout << a << ":" << b << ":" << c << endl;
    unsigned int l = 0, d = 0, n = 0;

    for( int i = 0; i < a.length(); ++i ){ 
        l = l * 10 + a[i] - '0';
    }

    for( int i = 0; i < b.length(); ++i ){ 
        d = d * 10 + b[i] - '0';
    }

    for( int i = 0; i < c.length(); ++i ){ 
        n = n * 10 + c[i] - '0';
    }
    //cout << l << ":" << d << ":" << n << endl;
    
    // list
    vector<string> vs;

    for( int i = 0; i < d; ++i ) {
        char ln[def] = {0,};
        finput.getline(ln, def);
        vs.push_back(ln);
    }

    /*
    for(int i = 0; i < vs.size(); ++i )
        cout << vs[i] << endl;
        */
    for( int i = 0; i < n; ++i ) {
        char nln[line] = {0,};
        //list<string*> ls;
        vector<string*> ls1, ls2;

        for(int j = 0; j < vs.size(); ++j)
            ls1.push_back( &vs[j] );

        finput.getline(nln, line);

        string sn(nln);

        // cases
        vector< queue<char> > vqs(l);

        int k = 0;
        bool pa = false;
        for( int j = 0; j < sn.length(); ++j ) {
            if( sn[j] == '(' ) {
                pa = true;
                continue;
            }
            else if( sn[j] == ')' ) {
                pa = false;
                ++k;
                continue;
            }
            else {
                if( pa )
                    vqs[k].push( sn[j] );
                else {
                    vqs[k].push( sn[j] );
                    ++k;
                }
            }
        }

        /*
        for( int i = 0; i < l; ++i ) {
            while( !vqs[i].empty() ) {
                cout << vqs[i].front();
                vqs[i].pop();
            }
            cout << endl;
        }  */

        for( int j = 0; j < l; ++j ) {
            while( !vqs[j].empty() ) {
                char ch =  vqs[j].front();
                vqs[j].pop();
                for( vector< string* >::iterator t = ls1.begin(); t < ls1.end(); ++t) {
                    if( (**t)[j] == ch )
                        ls2.push_back(*t);
                }
            }
            ls1 = ls2;
            ls2.clear();
        }

        //cout << "Case #" << i+1 << ": " << ls1.size() << endl;
        foutput << "Case #" << i+1 << ": " << ls1.size() << endl;
    }

    return 0;
}
