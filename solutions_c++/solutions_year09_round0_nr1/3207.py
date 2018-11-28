
#include "Main.h"

class token {
public:
    static string const fileDirectory;

    explicit token(string);
    ~token();

    vector<string> getTokens(int count=1);

private:
    std::ifstream ifs;
};
string const token::fileDirectory = "C:\\C++\\CJam\\";

token::token(string fileName) {

    string fileLocation = fileDirectory + fileName;

    ifs.open( fileLocation.c_str(), ios_base::in);
}

token::~token() {
    ifs.close();
}

vector<string> token::getTokens(int count) {

    static char const wordDelimiters[] = { (char) 10,
                                           (char) 13,
                                           (char) 32};
    static char const wordDelimitersSize = sizeof(wordDelimiters);
    vector<string> vt;
    string stringTemp;
    char charTemp;

    int i;
    for(i=0; (i<count) && ifs.good();) {

        charTemp = (char) ifs.get();
        if( binary_search( wordDelimiters, wordDelimiters+wordDelimitersSize, charTemp) ) {

            if(!stringTemp.length())
                continue;

            vt.push_back( stringTemp );
            i++;

            stringTemp.clear();
        }
        else
            stringTemp.append( 1, charTemp);
    }

    return vt;
}

