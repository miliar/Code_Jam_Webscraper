#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int
main(int agrc, char *argv[]) {
    int **p;
    int num;
    int line = 0;

    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int dummy;
    fin >> dummy;

    while (fin) {
        fin >> num;
        if (fin.fail())
            break;

        string str;
        p = new int*[num];
        for (int j = 0; j < num; ++j)
        p[j] = new int[num];

        for (int i = 0; i < num; ++i) {
            fin >> str;

            for (int j = 0; j < num; ++j) {
                switch (str[j]) {
                case '.':
                    p[i][j] = -1;
                    break;
                case '1':
                    p[i][j] = 1;
                    break;
                case '0':
                    p[i][j] = 0;
                    break;

                default:
                    cerr << "error input" << endl;
                }
            }
        }

        double *p1 = new double[num];
        double *p2 = new double[num];
        double *p3 = new double[num];

        for (int i = 0; i < num; ++i) {
            double w = 0.0f;
            double l = 0.0f;

            for (int j = 0; j < num; ++j) {
                if (p[i][j] == 1)
                    w += 1.0f;
                else if (p[i][j] == 0)
                    l += 1.0f;
            }

            p1[i] = w / (w + l);
        }

        for (int i = 0; i < num; ++i) {
            double x = 0.0f;
            int y = 0;

            for (int j = 0; j < num; ++j) {

                double l = 0.0f;
                double w = 0.0f;

                if (p[i][j] != -1) {
                    for (int k = 0; k < num; ++k) {
                        if (k == i)
                            continue;

                        if (p[j][k] == 1)
                            w += 1.0f;
                        else if (p[j][k] == 0)
                            l += 1.0f;
                    }

                    x += w / (w + l);
                    ++y;
                }
            }
            if (y > 0)
                x /= (double) y;

            p2[i] = x;
        }

        for (int i = 0; i < num; ++i) {
            double x = 0.0f;
            int y = 0;

            for (int j = 0; j < num; ++j) {
                if (p[i][j] != -1) {
                    x += p2[j];
                    ++y;
                }
            }
            if (y > 0)
                x /= (double) y;

            p3[i] = x;
        }

        fout << "Case #" << ++line << ":" << endl;
        for (int i = 0; i < num; ++i) {
            fout.precision(12);
            // fout << p1[i] << ' ' << p2[i] << ' ' << p3[i] << endl;
            fout << 0.25f * p1[i] + 0.50f * p2[i] + 0.25f * p3[i];
            fout << endl;
        }

        for (int j = 0; j < num; ++j) {
            delete [] p[j];
        }
        delete [] p;
        delete [] p1;
        delete [] p2;
        delete [] p3;
    }
    fin.close();
    fout.close();

    return 0;
}
