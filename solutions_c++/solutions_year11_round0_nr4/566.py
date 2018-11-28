#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;

class GoroSorter {
    vector<int> m_integers;
public:
    GoroSorter(int num) {
        m_integers.reserve(num);
    }

    void push(int num) {
        m_integers.push_back(num);
    }

    double sort() const {
        int numEquals = count_if(m_integers.begin(), m_integers.end(), IsEquals());

        return numSorts(m_integers.size() - numEquals);
    }
private:
    struct IsEquals {
        int m_current;

        IsEquals() : m_current(0) { }
        bool operator()(int value) {
            return ++m_current == value;
        }
    };

    double numSorts(int residual) const {
        if (residual == 0) {
            return 0.0;
        }
        if (residual == 2) {
            return 2.0;
        }
        if (residual == 3) {
            return 3.0;
        }
        return 2.0 + numSorts(residual - 2);
    }
};

void goroSort(istream& in, ostream& out) {
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        in >> N;

        GoroSorter goro(N);
        for (int j = 0; j < N; ++j) {
            int integer;
            in >> integer;
            goro.push(integer);
        }
        out << "Case #" << (i + 1) << ": " << fixed << setprecision(6) << goro.sort() << endl;
    }
}

int main(int argc, char** argv) {
  ifstream ifs(argv[1], ifstream::in);
  ofstream ofs(argv[2], ofstream::out);
  goroSort(ifs, ofs);
  return 0;
}
