#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small.out");

    int t;
    fin >> t;
    int total = t;
    while (t) {
        int p, q, temp;
        vector<int> release;
        fin >> p >> q;
        for (int i = 0; i < q; i++) {
            fin >> temp;
            release.push_back(--temp);
        }
        bool* empty = new bool [p];
        for (int i = 0; i < p; i++)
            empty[i] = false;
        sort(release.begin(), release.end());
        int gold = 10000000;
        do {
            int bribe = 0;
            for (int i = 0; i < p; i++)
                empty[i] = false;
            for (int i = 0; i < q; i++) {
                empty[release[i]] = true;
                for (int j = release[i] - 1; j >= 0; j--) {
                    if (!empty[j])
                        bribe++;
                    else
                        break;
                }
                for (int j = release[i] + 1; j < p; j++) {
                    if (!empty[j])
                        bribe++;
                    else
                        break;
                }
            }
            if (bribe < gold)
                gold = bribe;
        } while (next_permutation(release.begin(), release.end()));
        fout << "Case #" << total - t + 1 << ": " << gold << endl;
        delete [] empty;
        t--;
    }
}
