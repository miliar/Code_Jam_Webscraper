#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>

#define LOG(x)  //x

using namespace std;

int64_t solve(const string& line)
{
    vector<int64_t> digits;
    map<char,int64_t> c2d;
    set<int64_t> unused;
    for (int i = 0; i < 100; ++i) {
        unused.insert(i);
    }
    int64_t base = 0;

    digits.push_back(1);
    c2d[line[0]] = 1;
    unused.erase(1);
    base = 2;

    for (int i = 1; i < line.size(); ++i) {
        if (c2d.count(line[i])) {
            digits.push_back(c2d[line[i]]);
        } else {
            int64_t act = *unused.begin();
            c2d[line[i]] = act;
            unused.erase(act);
            digits.push_back(act);
            if (base <= act)
                base = act+1;
        }
    }
    
    int64_t result = 0;
    for (int i = 0; i < digits.size(); ++i) {
        result *= base;
        result += digits[i];
    }
    return result;
}

void test(istream& input, ostream& output)
{
    int numcases;
    input >> numcases;
    
     for (int i = 0; i < numcases; ++i) {
        string line;
        input >> line;
        
        output << "Case #" << i+1 << ": " << solve(line) << endl;
     } 

    std::string line;
}

void run_test_data(void)
{
    string testdatadir = "../../test_data/";
    string basename = "A-large-2.in";
    string input_path = testdatadir+basename+".txt";
    ifstream input;
    input.exceptions(input.failbit | input.badbit);
    input.open(input_path.c_str());
    string output_path = testdatadir+basename+".output.txt";
    ofstream output;
    output.exceptions(output.failbit | output.badbit);
    output.open(output_path.c_str(),std::ios::out|std::ios::trunc);
    
    test(input,output);
}

int main (int argc, char * const argv[]) {
    // insert code here...
    try {
        run_test_data();
        return 0;
    } catch (exception& err) {
        cerr << "Exception cathed:" << endl;
        cerr << err.what() << endl;
    } catch(...) {
        cerr << "Unkown exception catched" << endl;
        cerr << endl;
    }
    cerr << "Some error occured!\n";
    return 1;
}
