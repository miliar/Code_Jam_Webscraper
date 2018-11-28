#include <string>
#include <iostream>
#include <fstream>

using namespace std;

string Translate(string inpString)
{
    static const string G("zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
    static const string E("qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");
    string outString;

    for( string::iterator it(inpString.begin()); it < inpString.end(); it++ )
    {
        //cout << *it << endl;
        //cout << G.find(*it) << endl;
        //cout << E.at(G.find(*it)) << endl;
        outString.push_back(E.at(G.find(*it)));
    }
    return outString;
}

int main(int argc, char** argv)
{
    ifstream is;
    is.open(argv[1], ifstream::in);
    
    unsigned long numCases;
    is >> numCases;
    string x;
    getline(is, x);
    //cout << "Num cases: " << numCases << endl;
    
    for(int caseId = 0; caseId < numCases; caseId++)
    {
        getline(is, x);
        cout << "Case #" << caseId + 1 << ": " << Translate(x) << endl;
    }
    return 1;
}