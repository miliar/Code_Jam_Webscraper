#include <fstream>
#include <vector>
using namespace std;

string separate(const string& s) {
    if (s.length() <= 1)
        return s;
    return s.substr(0, 1) + ", " + separate(s.substr(1));
}

class Magicka {
    string m_elements;
    vector<string> m_combines;
    vector<string> m_opposed;
public:
    void pushCombine(const string& combine) {
        m_combines.push_back(combine);
    }

    void pushOpposed(const string& opposed) {
        m_opposed.push_back(opposed);
    }

    void invoke(char c) {
        if (m_elements.size() < 1) {
            m_elements.insert(m_elements.end(), c);
            return;
        }

        for (int i = 0; i < m_combines.size(); ++i) {
            if (combinable(m_combines[i], c)) {
                m_elements.replace(m_elements.end() - 1, m_elements.end(),
                                   1, m_combines[i][2]);
                return;
            }
        }

        for (int i = 0; i < m_opposed.size(); ++i) {
            if (isOpposed(m_opposed[i], c)) {
		m_elements.clear();
                return;
            }
        }
        m_elements.insert(m_elements.end(), c);
    }

    string toString() const {
        return "[" + separate(m_elements) + "]";
    }
private:
    bool combinable(const string& combine, char c) const {
        return (combine[0] == *(m_elements.end() - 1) && combine[1] == c) ||
                (combine[1] == *(m_elements.end() - 1) && combine[0] == c);
    }

    bool isOpposed(const string& opposed, char c) const {
        return (m_elements.find(opposed[0]) != string::npos && opposed[1] == c) ||
                (m_elements.find(opposed[1]) != string::npos && opposed[0] == c);
    }
};

void magicka(istream& in, ostream& out)
{
    int T;
    in >> T;
    for (int i = 0; i < T; ++i) {
        Magicka m;
        int C, D, N;
        in >> C;
        for (int j = 0; j < C; ++j) {
            string combine;
            in >> combine;
            m.pushCombine(combine);
        }

        in >> D;
        for (int j = 0; j < D; ++j) {
            string opposed;
            in >> opposed;
            m.pushOpposed(opposed);
        }

        in >> N;
        for (int j = 0; j < N; ++j) {
            char c;
            in >> c;
            m.invoke(c);
        }

        out << "Case #" << (i + 1) << ": " << m.toString() << endl;
    }
}

int main(int argc, char** argv) {
  ifstream ifs(argv[1], ifstream::in);
  ofstream ofs(argv[2], ofstream::out);
  magicka(ifs, ofs);
  return 0;
}
