#include <fstream>

using namespace std;

double getdistance(int p[], int v[], int start, int end, int d, double *lmost, double *rmost) {
    int total = 0;
    int lp[end - start], lv[end - start];
    for (int i = start; i != end; ++i) {
        total += v[i];
        lp[i - start] = p[i];
        lv[i - start] = v[i];
    }

    int count = 1, ptr = 0;
    double min, max;
    min = lp[0] - 0;
    max = lp[0] - 0;
    --lv[0];

    while (count < total) {
        if (lv[ptr]) {
            int temp = lp[ptr] - count * d;
            if (min > temp) min = temp;
            if (max < temp) max = temp;
            --lv[ptr];
        }
        else {
            ++ptr;
            continue;
        }
        ++count;
    }
    *lmost = 0 + (max - (max - min) / 2);
    *rmost = (total - 1) * d + (max - (max - min) / 2);

    return (max - min) / 2;
}

int main()
{
    ifstream fin("B-small-attempt1.in");
    ofstream fout("B-small-attempt1.out");

    int t;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int c, d;
        fin >> c >> d;

        int p[c], v[c];
        double rmost[c];
        int prev[c];
        double dist[c];
        fin >> p[0] >> v[0];
        double prev_lmost;
        dist[0] = getdistance(p, v, 0, 1, d, &prev_lmost, &rmost[0]);

        for (int i = 0; i != c; ++i) {
            prev[i] = i;
        }

        for (int i = 1; i != c; ++i) {
            fin >> p[i] >> v[i];
            double lmost;
            dist[i] = getdistance(p, v, prev[i], i + 1, d, &lmost, &rmost[i]);
            while (prev[i] != 0 && lmost < rmost[prev[i] - 1]) {
                prev[i] = prev[prev[i] - 1];
                dist[i] = getdistance(p, v, prev[i], i + 1, d, &lmost, &rmost[i]);
            }
        }

        double max = dist[c - 1];
        for (int i = prev[c - 1]; i >= 0; i = prev[i] - 1) {
            if (max < dist[i]) max = dist[i];
        }

        fout << "Case #" << cont << ": " << max << endl;
    }


    fin.close();
    fout.close();
    return 0;
}
