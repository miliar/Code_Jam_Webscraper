#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>

typedef long long int64;

using namespace std;

class CodeJame1 {
    map<char, char> g_n_dic;
public:
    void Solve(const string& input_file, const string& output_file) {
        vector<string> g_sources;
        vector<string> sources;
        g_sources.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
        g_sources.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
        g_sources.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

        sources.push_back("our language is impossible to understand");
        sources.push_back("there are twenty six factorial possibilities");
        sources.push_back("so it is okay if you want to just give up");

        g_n_dic['a'] = 'y';
        g_n_dic['o'] = 'e';
        g_n_dic['z'] = 'q';
        g_n_dic['q'] = 'z';
        
        for (int i = 0; i < sources.size(); ++i) 
        {
            for (int t = 0; t < sources[i].size(); ++t)
            {
                g_n_dic[g_sources[i][t]] = sources[i][t];
            }
        }

        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;
        string g_string;
        getline(input, g_string);
        for (int i = 0; i < case_number; ++i) {
            getline(input, g_string);
            WriteCaseResult(i+1, output, SolveProblem(g_string));
        }
        input.close();
        output.close();
    }
private:
    string SolveProblem(const string& g_string) {
        string res;
        for (size_t i = 0; i < g_string.size(); ++i) {
            res.push_back(g_n_dic[g_string[i]]);
        }
        return res;
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, const string& res) {
        output_stream << "Case #" << case_num << ": " << res << std::endl;
    }
};


int main() {
    CodeJame1  t;

    t.Solve("d:\\Sources\\CodeJam-2012\\input\\task1.txt", "d:\\Sources\\CodeJam-2012\\input\\task1_out.txt");

    return 0;
}