#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
using namespace std;

#define LOG(x)  //x

string dcset(char* data)
{
    string result = "{";
    for (char ch = 'a'; ch != 'z'; ch++) {
        if (data[ch]) {
            result += string(&ch,1);
        }
    }
    return result + "}";
}

int solve(const set<string>& dict, string& w, int l)
{
    set<string> candidates = dict;

    cerr << endl << "Case: " << w << endl << endl;
    int pos = 0;
    for (int i = 0; i < w.size(); ++i) {
        char cset[256] = {0};
        if (w[i] != '(') {
            cset[w[i]] = true;
            pos++;
        } else {
            ++i;
            while(w[i] != ')') {
                cset[w[i]] = true;
                ++i;
            }
            pos++;
        }
        LOG(cerr << "pos:" << pos << dcset(cset) << endl);
//        set<string>::iterator prev = candidates.begin();
        set<string>::iterator i = candidates.begin();
        while(i != candidates.end()) {
            bool erase = (i->size() < pos) || (!cset[(*i)[pos-1]]);
            LOG(cerr << "testing:" << *i << endl);
            if (erase) {
                set<string>::iterator next = i;
                ++next;
                LOG(cerr << "erasing:" << *i << " pos " << pos <<  dcset(cset) << string(&((*i)[pos-1]),1) << " " << candidates.size() << endl);
                //bool wasbegin = (i ==  candidates.begin());
                candidates.erase(i);
                //if (wasbegin) 
                //    i = candidates.begin();
                //else
                i = next;
#if 0
                if (i == candidates.end())
                    break;
#endif
            } else {
                ++i;
            }
//            prev = i;
        }
    }
    //return candidates.size();
    
    LOG(cerr << endl << "solutions" << endl);
    int result =0;
    for(set<string>::iterator i = candidates.begin(); i != candidates.end(); ++i) {
        if (i->size() == pos) {
            ++result;
            LOG(cerr << *i <<endl);
        }
        
    }
    
    LOG(std::cerr << "result:" << result <<std::endl);
    return result;
}

void test(istream& input, ostream& output)
{
    int numcases;
    int l,d;
    input >> l >> d >> numcases;
    
    string line;
    getline(input,line);
    set<string> dictionary;
    for (int j = 0; j < d; ++j) {
        getline(input,line);
        cout << "Words:" << line << endl;
        dictionary.insert(line);
    }
    for (int i = 0; i < numcases; ++i) {
        getline(input,line);
        cout << "Data:" << line << endl;
        string word = line;
        output << "Case #" << i+1 << ": " << solve(dictionary,word,l) << endl;
     }

}

void run_test_data(void)
{
    string testdatadir = "../../test_data/";
    string dataname = "A-small-attempt0.in";
    dataname = "small_input";
    dataname = "A-large-1.in";
    string input_path = testdatadir+dataname+".txt";
    ifstream input;
    input.exceptions(input.failbit | input.badbit);
    input.open(input_path.c_str());
    string output_path = testdatadir+dataname+".generated.txt";
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
