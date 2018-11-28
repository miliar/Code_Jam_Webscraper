#include "magickaParser.h"
#include "magicka.h"
#include <vector>
#include <iostream>


using std::cerr;
using std::cout;
using std::endl;
using std::vector;

int main(int argc, char **argv)
{
    vector<MagickaProblem> ps = MagickaParser::parse(argv[1]);

    int i = 0;
    vector<MagickaProblem>::iterator p;
    for(p = ps.begin(); p != ps.end(); p++) {
        ++i;
        vector<char> res = p->processElements();

        cerr << "Case #" << i << ": [";
        vector<char>::iterator e = res.begin();
        if(e != res.end()) {
            cerr << *e;
            e++;
        }
        for(e; e != res.end(); e++) {
            cerr << ", " << *e;
        }
        cerr << "]" << endl;
    }


    return 0;
}
