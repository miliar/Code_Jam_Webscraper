#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

double WP(string s) {
    int sum = 0, count = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '1') {
            sum++;
            count++;
        }
        if (s[i] == '0') {
            count++;
        }
    }
    return 1. * sum / count;
}

double OWP(string s, int me) {
    int sum = 0, count = 0;
    for (int i = 0; i < s.size(); i++) {
        if (i == me)
            continue;
        if (s[i] == '1') {
            sum++;
            count++;
        }
        if (s[i] == '0') {
            count++;
        }
    }
    return 1. * sum / count;
}

int main(int argc, char *argv[])
{
    fstream fin, fout;
    fin.open("a.in",ios_base::in);
    fout.open("a.out",ios_base::out);
    int T;
    fin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        fin >> N;
        vector<string> match;
        for (int n = 0; n < N; n++) {
            string l;
            fin >> l;
            /*for (int i = 0; i < N; i++) {
                char c;
                fin >> c;
                l += c;
            }*/
            match.push_back(l);
        }
        vector<double> wp, owp, oowp;
        for (int i = 0; i < N; i++) {
            wp.push_back(WP(match[i]));
        }
        for (int i = 0; i < N; i++) {
            double sum = 0;
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (j == i)
                    continue;
                if (match[i][j] != '.') {
                    sum += OWP(match[j], i);
                    count++;
                }
            }
            owp.push_back(sum/count);
        }
        for (int i = 0; i < N; i++) {
            double sum = 0;
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (j == i)
                    continue;
                if (match[i][j] != '.') {
                    sum += owp[j];
                    count++;
                }
            }
            oowp.push_back(sum/count);
        }
        fout << "Case #" << t + 1 << ":" << endl;
        for (int i = 0; i < N; i++) {
            fout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
