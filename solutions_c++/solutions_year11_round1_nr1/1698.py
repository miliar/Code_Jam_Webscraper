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
            long long n;
            long long first;
            long long second;

            ReadCase(input, n, first, second);
            WriteCaseResult(i+1, output, SolveProblem(n, first, second));
        }
        input.close();
        output.close();
    }
private:
    bool SolveProblem(long long n, long long first, long long second) {
        for (long long sum = 2; sum <= 1000000; ++sum) {
            for (long long d = 1; d <= n; ++d) {
                if (sum - d >= d) {
                    if ((first*d % 100 == 0)&& (second*sum % 100 == 0) && 
                        (sum - d) >= second*sum / 100 - first*d / 100 && first*d / 100 <= second*sum / 100) {
                            cout << d << " " << sum << std::endl;
                            cout << first*d/ 100 << " " << second*sum / 100 << std::endl;
                        return true;
                    }
                } else {
                    break;
                }
            }
        }
        return false;
    }

    void ReadCase(ifstream& input_stream, long long& n, long long& first, long long& second) {
        input_stream >> n;

        input_stream >> first;
        input_stream >> second;
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, bool possible) {
        if (possible) {
            cout << "Case #" << case_num << ": Possible" << std::endl;
            output_stream << "Case #" << case_num << ": Possible" << std::endl;
        } else {
            cout << "Case #" << case_num << ": Broken" << std::endl;
            output_stream << "Case #" << case_num << ": Broken" << std::endl;
        }
    }
};


int main() {
    CodeJame1  t;
    t.Solve("c:\\Sources\\CodeJam\\CodeJam\\input\\task1.txt", "c:\\Sources\\CodeJam\\CodeJam\\output\\task1.txt");

    return 0;
}