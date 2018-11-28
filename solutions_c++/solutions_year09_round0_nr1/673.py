#include <vector>
#include <string>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

int L, D, N;
vector <string> dict;

bool match(const string &w, const string &p) {
    int pos = 0;

    for (size_t i = 0; i < w.size(); ++i, ++pos)
        if (w[i] == p[pos])
            continue;
        else
            if (p[pos] == '(') {
                bool found = false;
                char ch = w[i];

                while (p[pos] != ')') {
                    if (p[pos] == ch)
                        found = true;
                    ++pos;
                }

                if (!found)
                    return false;

            } else {
                return false;
            }

    return true;
}

int count(const string &pattern) {
    int ret = 0;

    for (int i = 0; i < D; ++i)
        ret += match(dict[i], pattern);

    return ret;
}


int main(int argc, char **argv) {

    in.open(argv[1]);
    out.open(argv[2]);

    in >> L >> D >> N;
    dict.resize(D);
    for (int i = 0; i < D; ++i)
        in >> dict[i];

    for (int i = 1; i <= N; ++i) {
        string pattern;
        in >> pattern;
        out << "Case #" << i << ": " << count(pattern) << "\n";
    }

    in.close();
    out.close();

    return 0;
}
