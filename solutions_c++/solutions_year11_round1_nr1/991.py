#include <fstream>
using namespace std;

class FreeCell {
    long long m_n;
    int m_pd, m_pg;
public:
    FreeCell(long long n, int pd, int pg) : m_n(n), m_pd(pd), m_pg(pg){

    }

    bool possible() const {
        if (m_pg == 100)
            return m_pd == 100;
        if (m_pg == 0)
            return m_pd == 0;

        return minGames() <= m_n;
    }

    int minGames() const {
        return 100 / gcd(100, m_pd);
    }

    static int gcd(int m, int n) {
        while (m != n) {
            if (m > n)
                m -= n;
            else
                n -= m;
        }
        return m;
    }
};

void freeCell(istream& in, ostream& out) {
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        long long N;
        int Pd, Pg;
        in >> N >> Pd >> Pg;
        FreeCell f(N, Pd, Pg);
        out << "Case #" << (i + 1) << ": " <<
               (f.possible() ? "Possible" : "Broken") << endl;
    }
}

int main(int argc, char** argv) {
  ifstream ifs(argv[1], ifstream::in);
  ofstream ofs(argv[2], ofstream::out);
  freeCell(ifs, ofs);
  return 0;
}
