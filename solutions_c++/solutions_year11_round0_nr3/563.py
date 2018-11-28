#include <fstream>
#include <numeric>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

class CandySplitter {
    vector<int> m_candies;
    vector<int> m_smalls;
    vector<int> m_bigs;
public:
    CandySplitter(int candies) {
        m_candies.reserve(candies);
    }

    void pushValue(int candy) {
        m_candies.push_back(candy);
    }

    void split() {
        vector<int>::iterator iter = min_element(m_candies.begin(), m_candies.end());
        m_smalls.push_back(*iter);
        m_candies.erase(iter);

        while (!m_candies.empty()) {
            m_bigs.push_back(m_candies.back());
            m_candies.pop_back();
        }
    }

    string bigValue() const {
        int bigValueXOR = accumulate(m_bigs.begin(), m_bigs.end(), 0, XOR());
        int smallValue = accumulate(m_smalls.begin(), m_smalls.end(), 0);
        if (bigValueXOR != smallValue) {
            return "NO";
        }
        stringstream ss;
        ss << accumulate(m_bigs.begin(), m_bigs.end(), 0);
        return ss.str();
    }

    struct XOR {
        int operator()(int lhs, int rhs) const {
            return lhs ^ rhs;
        }
    };
};

void splitCandy(istream& in, ostream& out) {
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        in >> N;
        CandySplitter cs(N);
        for (int j = 0; j < N; ++j) {
            int value;
            in >> value;
            cs.pushValue(value);
        }
        cs.split();
        out << "Case #" << (i + 1) << ": " << cs.bigValue() << endl;
    }
}

int main(int argc, char** argv) {
  ifstream ifs(argv[1], ifstream::in);
  ofstream ofs(argv[2], ofstream::out);
  splitCandy(ifs, ofs);
  return 0;
}
