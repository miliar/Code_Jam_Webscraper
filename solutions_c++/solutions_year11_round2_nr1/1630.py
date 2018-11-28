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

class CodeJame1 {
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;

        for (int i = 0; i < case_number; ++i) {
            int n;
            // ReadCase(input, n, first, second);
            input >> n;
            vector<string> values;
            for (int t = 0; t < n; ++t) {
                string str;
                input >> str;
                values.push_back(str);
            }
            WriteCaseResult(i+1, output, SolveProblem(values));
        }
        input.close();
        output.close();
    }
private:
    vector<float> SolveProblem(vector<string>& values) {
        vector<float> wp(values.size(), 0);
        for (int i = 0 ; i < values.size(); ++i) {
            int game_count = 0;
            int win = 0;
            for (int j = 0 ; j < values[0].size(); ++j) {
                if (values[i][j] == '0' || values[i][j] == '1') {
                    game_count++;
                }
                if (values[i][j] == '1') {
                    ++win;
                }
            }
            if (game_count > 0) {
                wp[i] = (float)win / (float)game_count;
            }
        }
        vector<float> owp(values.size(), 0);
        vector<float> opponent_counts(values.size(), 0);

        for (int c = 0 ; c < values.size(); ++c) {
            int opponent_count = 0;
            float sum_wp = 0;

            for (int i = 0; i < values.size(); ++i) {
                if (c == i) {
                    continue;
                }
                if (values[i][c] == '.') {
                    continue;
                }
                ++opponent_count;

                int game_count = 0;
                int win = 0;

                for (int j = 0 ; j < values[0].size(); ++j) {
                    if (c != j && (values[i][j] == '0' || values[i][j] == '1')) {
                        game_count++;
                    }
                    if (c != j && values[i][j] == '1') {
                        win++;
                    }
                }

                if (game_count > 0) {
                    sum_wp += (float)win / (float)game_count;
                }
            }
            if (opponent_count > 0) {
                owp[c] = sum_wp / (float)opponent_count ;
                opponent_counts[c] = opponent_count;
            }
        }
        vector<float> oowp(values.size(), 0);
        for (int c = 0 ; c < values.size(); ++c) {
            float sum_oowp = 0;
            for (int i = 0; i < values.size(); ++i) {
                if (values[c][i] == '.') {
                    continue;
                }
                if (c != i) {
                    sum_oowp += owp[i];
                }
            }
            if (opponent_counts[c] > 0) {
                oowp[c]= sum_oowp / opponent_counts[c];
            }
        }
        vector<float> rpi(values.size(), 0);
        for (int i = 0; i < values.size(); ++i) {
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i];
        }
        return rpi;
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, vector<float>& res) {
        output_stream << "Case #" << case_num << ":" << std::endl;
        for (int i = 0; i < res.size(); ++i) {
            output_stream << std::setprecision (9) << res[i] << std::endl;
        }

    }
};

int main() {
    CodeJame1  t;
    
    t.Solve("c:\\Sources\\CodeJam\\CodeJam\\input\\task1.txt", "c:\\Sources\\CodeJam\\CodeJam\\output\\task1.txt");

    return 0;
}