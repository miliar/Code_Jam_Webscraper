#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
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
#include <iomanip>

using std::cin;
using std::cout;
using std::endl;
using std::set;
using std::map;
using std::max;
using std::min;
using std::stringstream;

using std::ifstream;
using std::ofstream;
using std::stack;
using std::string;
using std::vector;
using std::numeric_limits;

//class CodeJame1 {
//public:
//    void Solve(const string& input_file, const string& output_file) {
//        ifstream input(input_file.c_str());
//        ofstream output(output_file.c_str());
//
//        int case_number;
//        input >> case_number;
//
//        for (int i = 0; i < case_number; ++i) {
//            int r;
//            input >> r;
//            int c;
//            input >> c;
//            vector<string> values;
//            for (int t = 0; t < r; ++t) {
//                string str;
//                input >> str;
//                values.push_back(str);
//            }
//            bool res = SolveProblem(values);
//            WriteCaseResult(i+1, output, res, values);
//        }
//        input.close();
//        output.close();
//    }
//private:
//    bool SolveProblem(vector<string>& values) {
//
//
//    for (int i = 0; i < values.size(); ++i) 
//        for (int j = 0; j < values[0].size(); ++j) 
//            if (values[i][j] == '#') 
//                for (int i1 = i; i1 <= i + 1; ++i1)  
//                    for (int j1 = j; j1 <= j + 1; ++j1) 
//                        if (i1 >= values.size() || j1 >= values[0].size() || values[i1][j1] != '#') return false; 
//                        else values[i1][j1] = ((i1 - i + j1 - j) % 2? '\\' : '/') ;
//    
//    return true;
//
//    }
//    void WriteCaseResult(int case_num, ofstream& output_stream, bool res, vector<string>& values) {
//        output_stream << "Case #" << case_num << ":" << std::endl;
//        if (!res) {
//            output_stream << "Impossible" << std::endl;
//        } else {
//            for (int i = 0; i < values.size(); ++i) {
//                output_stream << values[i] << std::endl;
//            }
//        }
//    }
//};

class CodeJame1 {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;

        for (int i = 0; i < case_number; ++i) {
            int n;
            input >> n;
            int l;
            input >> l;
            int h;
            input >> h;

            vector<int> values;
            for (int t = 0; t < n; ++t) {
                int val;
                input >> val;
                values.push_back(val);
            }
            int res = SolveProblem(l, h,values);
            WriteCaseResult(i+1, output, res);
        }
        input.close();
        output.close();
    }
private:
    int SolveProblem(int l, int h, vector<int>& values) {
        for (int j_freq = l; j_freq <= h; ++j_freq) {
            bool is_res = true;
            for (int i = 0; i < values.size(); ++i) {
                if ((j_freq != 0 && values[i] % j_freq == 0) || (values[i] != 0 &&  j_freq % values[i]== 0)) {
                } else {
                    is_res = false;
                }
            }
            if (is_res) {
                return j_freq;
            }
        }
        return -1;
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, int res) {
        if (res == -1) {
            output_stream << "Case #" << case_num << ": NO" << std::endl;
        } else {
            output_stream << "Case #" << case_num << ": " << res << std::endl;
        }
    }
};


int main() {
    CodeJame1  t;
    
    t.Solve("c:\\Sources\\CodeJam\\CodeJam\\input\\task1.txt", "c:\\Sources\\CodeJam\\CodeJam\\input\\task1_out.txt");

    return 0;
}