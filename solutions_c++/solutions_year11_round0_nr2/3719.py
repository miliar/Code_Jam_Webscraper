#define FILENAME "B-small-attempt0"
/* -------------------------------------------------------------------------- */
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>

#define INPUT_EXT ".in"
#define OUTPUT_EXT ".out"
#define MAX_T 100
#define MAX_C 36
#define MAX_D 28
#define MAX_N 100

using namespace std;

int main(int argc, char** argv)
{
    fstream input(FILENAME INPUT_EXT);
    ofstream output(FILENAME OUTPUT_EXT, ios_base::out);

    int T = 0; // Test cases
    int C = 0; // Combining
    int D = 0; // Deleting
    int N = 0; // Length of string

    input >> T;
    for (int i=0; i<T; i++) {
        map<char, vector<char> > opposing;   // lists of opposing characters for
                                             // each character
        map<char, vector<pair<char, char> > > combining;
                                             // list of character sequences able
                                             // to combine
        char str[MAX_N];                     // string to investigate
        vector<char> result;                 // result caracters

        input >> C;
        for (int j=0; j<C; j++) {
            char comb[4];        // length of 3 + '\0'
            input >> comb;
            char from = comb[0];
            char with = comb[1];
            char to   = comb[2];
            if (combining.find(from) == combining.end()) {
                // No opposers yet;
                vector<pair<char, char> > vec_to;
                vec_to.push_back(pair<char, char>(with, to));
                combining.insert(pair<char, vector<pair<char, char> > >(from, vec_to));
            } else {
                // Found opposers
                combining.at(from).push_back(pair<char, char>(with, to));
            }

            if (from != with) {
                from = comb[1];
                with = comb[0];

                if (combining.find(from) == combining.end()) { // Copy-paste is baad
                    // No opposers yet;
                    vector<pair<char, char> > vec_to;
                    vec_to.push_back(pair<char, char>(with, to));
                    combining.insert(pair<char, vector<pair<char, char> > >(from, vec_to));
                } else {
                    // Found opposers
                    combining.at(from).push_back(pair<char, char>(with, to));
                }
            }
        }

        input >> D;
        for (int j=0; j<D; j++) {
            char opp[3];        // length of 2 + '\0'
            input >> opp;
            char from = opp[0];
            char to = opp[1];
            if (opposing.find(from) == opposing.end()) {
                // No opposers yet;
                vector<char> vec_to;
                vec_to.push_back(to);
                opposing.insert(pair<char, vector<char> >(from, vec_to));
            } else {
                // Found opposers
                opposing.at(from).push_back(to);
            }

            to = opp[0];
            from = opp[1];

            if (opposing.find(from) == opposing.end()) { // Really. It's evil.
                // No opposers yet;
                vector<char> vec_to;
                vec_to.push_back(to);
                opposing.insert(pair<char, vector<char> >(from, vec_to));
            } else {
                // Found opposers
                opposing.at(from).push_back(to);
            }
        }

        input >> N;

        input >> str;

        result.push_back(str[0]);
        // Begin processing
        for (int j=1; j<N; j++) { // From j=1, because 0th character is useless
                                  // now.
            bool leave_as_is = true;
            if (combining.find(str[j]) != combining.end()) {
                vector<pair<char, char> > &v = combining.at(str[j]);
                for (unsigned int k=0; k<v.size(); k++) {
                    if (result[result.size()-1] == v[0].first) {
                        // Combining!
//                        cout << "combining " << str[j]  << " with " << v[0].first << " to: " << v[0].second << endl;
                        result.erase(result.end()-1);
                        result.push_back(v[0].second);
                        leave_as_is = false;
                    }
                }
            }

            if (leave_as_is == true && opposing.find(str[j]) != opposing.end()) {
                vector<char > &v = opposing.at(str[j]);
                for (unsigned int l=0; l<v.size(); l++) {
//                    cout << "opposing with " << str[j] << ": " << v.at(l) << endl;
                    for (unsigned int k=0; k<result.size(); k++) {
                        if (result.at(k) == v.at(l)) {
//                            cout << "erasing because " << v.at(l) << " " << result.at(k) << endl;
                            result.clear();
                            leave_as_is = false;
                        }
                    }
                }
            }

            if (leave_as_is == true) {
                result.push_back(str[j]);
            }
        }

        ostringstream res_out;
        res_out << "Case #" << i+1 << ": [";
        if (result.size() > 0) {
            res_out << result.at(0);
        }
        for (unsigned int j=1; j<result.size(); j++) {
            res_out << ", " << result.at(j);
        }
        res_out << "]" << endl;
//        cout << res_out.str();
        output << res_out.str();
    }

    output.close();
    input.close();

    return 0;
}
