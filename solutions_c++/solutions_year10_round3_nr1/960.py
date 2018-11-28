#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <stdio.h>
#include <math.h>

using namespace std;

string intToStr(int n) {
    stringstream ss;
    string sOut;

    ss << n;
    ss >> sOut;

    return sOut;
}

int strToInt(string s) {
    stringstream ss;
    int iOut;

    ss << s;
    ss >> iOut;

    return iOut;
}

int strToInt(char c) {
    stringstream ss;
    int iOut;

    ss << c;
    ss >> iOut;

    return iOut;
}

int main() {
    ifstream fin("a.in");
    ofstream fout("a.out");
    long T, N;
    vector <pair <long, long> > points;
    pair <long, long> p, cur;
    long count = 0;

    fin >> T;

    for (unsigned int i = 0; i < T; i++) {
        fin >> N;
        count = 0;
        points.clear();

        for (unsigned int k = 0; k < N; k++) {
            fin >> p.first >> p.second;
            points.push_back(p);
        }

        for (unsigned int k = 0; k < N; k++) {
            cur = points[k];
            for (unsigned int j = 0; j < N; j++) {
                if (k == j)
                    continue;

                p = points[j];
                if (cur.first < p.first) {
                    if (cur.second > p.second) {
                        count++;
                    }
                }
            }
        }

        fout << "Case #" << (i + 1) << ": " << count << endl;
    }

    return 0;
}
