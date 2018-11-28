#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main() {
    ifstream fin("B-small-attempt1.in");
    ofstream fout("B-small.out");

    int t;
    fin >> t;
    int total = t;
    fin.get();
    while (t) {
        string temp;
        vector<int> n;
        getline(fin, temp);
        for (int i = 0; i < temp.length(); i++)
            n.push_back(temp[i] - '0');
        vector<int> o = n;
        sort(n.begin(), n.end());
        do {
            if (o == n) {
                if (next_permutation(n.begin(), n.end())) {
                    fout << "Case #" << total - t + 1 << ": ";
                    copy(n.begin(), n.end(), ostream_iterator<int>(fout, ""));
                    fout << endl;
                    break;
                }
                else {
                    n.push_back(0);
                    sort(n.begin(), n.end());
                    while (!n[0])
                        next_permutation(n.begin(), n.end());
                    fout << "Case #" << total - t + 1 << ": ";
                    copy(n.begin(), n.end(), ostream_iterator<int>(fout, ""));
                    fout << endl;
                    break;
                }
            }
        } while (next_permutation(n.begin(), n.end()));
        t--;
    }
}
