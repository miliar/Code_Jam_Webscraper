#include <string>
#include <fstream>
#include <cstring>
using namespace std;

const int MAX_LINE_LENGTH = 505;
const string target = "welcome to code jam";
const int targetL = 19;

ifstream in;
ofstream out;

char line[MAX_LINE_LENGTH];
int C[MAX_LINE_LENGTH][targetL];

int count_all() {
    int L = strlen(line);

    for (int i = 0; i < L; ++i)
        for (int j = 0; j < targetL; ++j) {
            C[i][j] = i > 0 ? C[i - 1][j] : 0;
            if (line[i] == target[j])
                if (i > 0)
                    if (j > 0)
                        C[i][j] += C[i - 1][j - 1];
                    else
                        C[i][j] += 1;
                else
                    if (j > 0)
                        C[i][j] += 0;
                    else
                        C[i][j] += 1;
            if (C[i][j] >= 10000)
                C[i][j] -= 10000;
        }

    return C[L - 1][targetL - 1];
}


int main(int argc, char **argv) {

    in.open(argv[1]);
    out.open(argv[2]);

    int N;
    in >> N;
    in.getline(line, MAX_LINE_LENGTH); // consume the first line

    for (int i = 1; i <= N; ++i) {
        in.getline(line, MAX_LINE_LENGTH);

        int sol = count_all();

        out << "Case #" << i << ": ";
        out << (sol / 1000) << (sol % 1000 / 100) << (sol % 100 / 10) << (sol % 10);
        out << "\n";
    }

    in.close();
    out.close();

    return 0;
}
