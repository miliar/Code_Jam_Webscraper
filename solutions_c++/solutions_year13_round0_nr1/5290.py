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
public:
    void Solve(const string& input_file, const string& output_file) {
        ifstream input(input_file.c_str());
        ofstream output(output_file.c_str());

        int case_number;
        input >> case_number;
        for (int i = 0; i < case_number; ++i) {
            vector<string> area;
            for (int l = 0; l < 4; ++l) {
                string s;
                input >> s;
                area.push_back(s);
            }
            WriteCaseResult(i+1, output, SolveProblem(area));
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

    bool CheckWin(const vector<string>& area, char player)
    {
        int d_v = 0;
        int d_t = 0;
        int d_v1 = 0;
        int d_t1 = 0;
        for (int j =0; j < 4; ++j) {
            int c_v = 0;
            int c_t = 0;
            for (int i = 0; i < 4; ++i) {
                if ((i + j) == 3) {
                    if (area[j][i] == player) {
                        ++d_v1;
                    }
                    if (area[j][i] == 'T') {
                        ++d_t1;
                    }

                }
                if (i == j) {
                    if (area[j][i] == player) {
                        ++d_v;
                    }
                    if (area[j][i] == 'T') {
                        ++d_t;
                    }
                }
                if (area[j][i] == player) {
                    ++c_v;
                }
                if (area[j][i] == 'T') {
                    ++c_t;
                }
            }
            if (c_v == 4 || (c_v == 3 && c_t == 1))
                return true;
        }
        if (d_v == 4 || (d_v == 3 && d_t == 1))
            return true;
        if (d_v1 == 4 || (d_v1 == 3 && d_t1 == 1))
            return true;
        
        for (int j =0; j < 4; ++j) {
            int c_v = 0;
            int c_t = 0;
            for (int i = 0; i < 4; ++i) {
                if (area[i][j] == player) {
                    ++c_v;
                }
                if (area[i][j] == 'T') {
                    ++c_t;
                }
            }
            if (c_v == 4 || (c_v == 3 && c_t == 1))
                return true;
        }
        return false;
    }
    string SolveProblem(const vector<string>& area) {
        if (CheckWin(area, 'X'))
            return "X won";
        if (CheckWin(area, 'O'))
            return "O won";
        for (int i = 0; i < 4; ++i) {
            if (area[i].find('.') != string::npos)
                return "Game has not completed";
        }
        return "Draw";
    }
    void WriteCaseResult(int case_num, ofstream& output_stream, string res) {
        output_stream << "Case #" << case_num << ": " << res << std::endl;
    }
};


int main() {
    CodeJame1  t;

    t.Solve("d:\\Sources\\CodeJam-2012\\input\\task1.txt", "d:\\Sources\\CodeJam-2012\\input\\task1_out.txt");

    return 0;
}