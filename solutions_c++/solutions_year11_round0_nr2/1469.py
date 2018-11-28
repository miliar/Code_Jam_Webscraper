#include <fstream>
#include <vector>
#include <map>
#include <cstring>

using namespace std;

const int base[26] = {4, -1, -1, 6, 2, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 3, 5, -1, -1, -1, 1, -1, -1, -1};

void swap2(string str) {
    char temp = str[0];
    str[0] = str[1];
    str[1] = temp;
}


int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    int t = 0;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int c, d, n;
        char combine[8][8];
        bool oppose[8][8];
        int numbase[8];

        for (int i = 0; i != 8; ++i) {
            numbase[i] = 0;
            for (int j = 0; j != 8; ++j) {
                combine[i][j] = 0;
                oppose[i][j] = false;
            }
        }
        fin >> c;
        for (int i = 0; i != c; ++i) {
            char temp[4];
            fin >> temp;
            combine[base[temp[0] - 'A']][base[temp[1] - 'A']] = temp[2];
            combine[base[temp[1] - 'A']][base[temp[0] - 'A']] = temp[2];
        }
        fin >> d;
        for (int i = 0; i != d; ++i) {
            char temp[3];
            fin >> temp;
            oppose[base[temp[0] - 'A']][base[temp[1] - 'A']] = true;
            oppose[base[temp[1] - 'A']][base[temp[0] - 'A']] = true;
        }

        fin >> n;
        char invoke[n + 1];
        fin >> invoke;
        char result[n + 1];
        memset(result, sizeof(result), 0);
        int presult = 0;

        for (int i = 0; i < n; ++i) {
            if (presult > 0) {
                if (base[result[presult - 1] - 'A'] != -1 && combine[base[invoke[i] - 'A']][base[result[presult - 1] - 'A']]) {
                    --numbase[base[result[presult - 1] - 'A']];
                    result[presult - 1] = combine[base[invoke[i] - 'A']][base[result[presult - 1] - 'A']];
                }
                else {
                    bool isoppose = false;
                    for (int j = 0; j != 8; ++j) {
                        if (numbase[j] && oppose[j][base[invoke[i] - 'A']]) {
                            presult = 0;
                            result[presult] = '\0';
                            isoppose = true;
                            for (int i = 0; i != 8; ++i) {
                                numbase[i] = 0;
                            }
                            break;
                        }
                    }

                    if (isoppose) {
                        continue;
                    }
                    else {
                        result[presult] = invoke[i];
                        result[++presult] = '\0';
                        ++numbase[base[invoke[i] - 'A']];
                    }
                }
            }
            else {
                result[presult] = invoke[i];
                ++numbase[base[invoke[i] - 'A']];
                result[++presult] = '\0';
            }
        }

        fout << "Case #" << cont << ": [";
        for (int i = 0; i != presult; ++i) {
            if (i) fout << ", ";
            fout << result[i];
        }
        fout << "]" << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
