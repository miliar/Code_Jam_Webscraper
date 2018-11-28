#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main(int argc, char** argv)
{
    fstream in, out;
    in.open("a.in", ios_base::in);
    out.open("a.out", ios_base::out);
    int T;
    in >> T;
    for (int t = 0; t < T; t++) {
        int R, C;
        in >> R >> C;
        vector<string> m;
        for (int i = 0; i < R; i++) {
            string s;
            in >> s;
            m.push_back(s);
        }
        bool bOk = true;
        for (int i = 0; bOk && i < R - 1; i++) {
            for (int j = 0; bOk && j  < C - 1; j++) {
                if (m[i][j] == '#') {
                    if (m[i+1][j] == '#' && m[i][j+1] == '#' && m[i+1][j+1] == '#') {
                        m[i][j] = m[i+1][j+1] = '/';
                        m[i][j+1] = m[i+1][j] = '\\';
                    } else {
                        bOk = false;
                    }
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (m[i][j] == '#') {
                    bOk = false;
                }
            }
        }
        out << "Case #" << t + 1 << ":" << endl;
        if (bOk) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    out << m[i][j];
                }
                out << endl;
            }
        } else {
            out << "Impossible" << endl;
        }
    }
    in.close();
    out.close();
	return 0;
}

