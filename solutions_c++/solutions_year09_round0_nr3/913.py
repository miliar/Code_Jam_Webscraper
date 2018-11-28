#include <iostream>
#include <string>
#include <list>
#include <set>
#include <map>

using namespace std;

enum role {
    w, e1, l, c1, o1, m1, e2, space1, t, o2, space2, c2, o3, d, e3, space3, j, a, m2
};

void updateCounts(map<role, int>& counts, role r) {
    if (r == w) {
        counts[w]++;
    } else {
        int ways = counts[(role)(r-1)];
        counts[r] = (counts[r] + ways) % 10000;
    }
}

void doCase(int num) {
    map<role, int> counts;

    string line;
    getline(cin, line);

    string::const_iterator it;
    for (it = line.begin(); it != line.end(); it++) {
        switch (*it) {
            case 'w':
                updateCounts(counts, w);
                break;
            case 'e':
                updateCounts(counts, e1);
                updateCounts(counts, e2);
                updateCounts(counts, e3);
                break;
            case 'l':
                updateCounts(counts, l);
                break;
            case 'c':
                updateCounts(counts, c1);
                updateCounts(counts, c2);
                break;
            case 'o':
                updateCounts(counts, o1);
                updateCounts(counts, o2);
                updateCounts(counts, o3);
                break;
            case 'm':
                updateCounts(counts, m1);
                updateCounts(counts, m2);
                break;
            case ' ':
                updateCounts(counts, space1);
                updateCounts(counts, space2);
                updateCounts(counts, space3);
                break;
            case 't':
                updateCounts(counts, t);
                break;
            case 'd':
                updateCounts(counts, d);
                break;
            case 'j':
                updateCounts(counts, j);
                break;
            case 'a':
                updateCounts(counts, a);
                break;
        }
    }

    cout << "Case #" << num << ": ";
    printf("%04d", counts[m2] % 10000);
    cout << endl;
}

int main() {
    int N;

    cin >> N;

    // Eat the endl
    string tmp;
    getline(cin, tmp);

    for (int i = 0; i < N; i++) {
        doCase(i + 1);
    }
}
