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
using std::reverse;

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
            long long speed_number;
            input >> speed_number;
            long long time;
            input >> time;

            long long star_number;
            input >> star_number;

            long long c;
            input >> c;

            vector<long long> values(star_number, 0);

            for (int t = 0; t < c; ++t) {
                long long val;
                input >> val;

                for (long long k = 0; k <= star_number; ++k) {
                    long long index = k*c + t + 1;
                    if (index <= star_number) {
                        values[index - 1] = (2*val);
                    }
                }
            }
            int res = SolveProblem(speed_number,time, values);
            WriteCaseResult(i+1, output, res);
        }
        input.close();
        output.close();
    }
private:
    long long SolveProblem(long long speed_number, long long time, vector<long long>& values) {
        long long cur_time = 0;
        long long star_index = 0;

        while (cur_time < time && star_index < values.size()) {
            cur_time += values[star_index];
            ++star_index;
        }
        if (star_index == values.size()) {
            return cur_time;
        }
        star_index -- ;
        vector<long long> res_values;

        if (star_index == -1) {
            long long dist = values[star_index + 1] - time;
            res_values.push_back(dist);
            for (long long i = 1; i < values.size(); ++i) {
                res_values.push_back(values[i]);
            }
        } else {
            long long dist = 0;
            for (long long t = 0; t <= star_index; ++t) {
                dist += values[t];
            }
            res_values.push_back(dist - time);
            for (long long i = star_index + 1; i < values.size(); ++i) {
                res_values.push_back(values[i]);
            }
        }

        sort(res_values.begin(), res_values.end());
        reverse(res_values.begin(), res_values.end());

        long long res = 0;
        for (int i =0; i < res_values.size(); ++i) {
            if (i < speed_number) {
                res += res_values[i] / 2;
            } else {
                res += res_values[i] ;
            }
        }
        return time + res;
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