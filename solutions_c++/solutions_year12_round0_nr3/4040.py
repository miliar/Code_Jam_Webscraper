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
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;
        for (int i = 0; i < case_number; ++i) {
            int64 A, B;
            input >> A;
            input >> B;
            WriteCaseResult(i+1, output, SolveProblem(A, B));
        }
        input.close();
        output.close();
    }
private:
    string DoCycleShift(const string& str, int num) {
        if (str.size() == 1)
            return str;
        return str.substr(num) + str.substr(0, num);
    }
    string ToString(int64 value)
    {
        stringstream st;
        st << value;
        string res;
        st >> res;
        return res;
    }
    int64 ToNumber(const string& value)
    {
        stringstream st;
        st << value;
        int64 res;
        st >> res;
        return res;
    }

    int64 SolveProblem(int64 A, int64 B) {
        int64 res = 0;

        for (int64 n = A; n < B; ++n) {
            string num_str = ToString(n);
            set<string> eee;
            for (int i = 1; i < num_str.size(); ++i) {
                string res_str = DoCycleShift(num_str, i);
                if (num_str[0] == '0' || res_str[0] == '0' || (res_str.size() != num_str.size()))
                    continue;

                int64 res_v = ToNumber(res_str);
                if (res_v > n && res_v <= B && res_v > A) {
                    eee.insert(num_str + " " + res_str);
                }
            }
            res += eee.size();
        }
        return res;
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, int64 res) {
        output_stream << "Case #" << case_num << ": " << res << std::endl;
    }
};


int main() {
    CodeJame1  t;

    t.Solve("d:\\Sources\\CodeJam-2012\\input\\task1.txt", "d:\\Sources\\CodeJam-2012\\input\\task1_out.txt");

    return 0;
}