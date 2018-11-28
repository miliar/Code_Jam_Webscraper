#include <cstdlib>
#include <iostream>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {
    int count, i;
    string line;
    istringstream is;
    char dummy;
    
    char alphabet[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    string * lines;
    
    getline(cin, line);
    is.str(line);
    is >> count;

    lines = new string[count];
    
   // read
    for (i=0; i<count; i++) {
        is.clear();
        noskipws(is);
        getline(cin, line);
        is.str(line);
        
        is.get(dummy);
        while(!is.eof()) {
            if (dummy < 'a' || dummy > 'z') {
                lines[i] += dummy;
            } else {
                lines[i] += alphabet[dummy-'a'];
            }
            is >> dummy;
        }
    }

   // out
    for (i=0; i<count; i++) {
        cout << "Case #" << (i+1) << ": " << lines[i] << endl;;
    }
    
    delete [] lines;
    
    return 0;
}
