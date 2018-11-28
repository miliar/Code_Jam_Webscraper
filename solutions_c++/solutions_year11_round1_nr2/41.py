#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x)

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

struct entry {
    string word;
    int index;
};

ostream& operator<<(ostream& os, const entry& e) {
    return os << e.word << "@" << e.index;
}

void findbest(const vector<entry>& dict, const string& seq, int wrong,
        int pos, int bitmask, int& bestwrong, int& bestindex, int d) {
    for (int i = 0; i < d; i++) D(cerr << "  ");
    D(cerr << "findbest: " << dict << " wrong=" << wrong << " pos=" << pos << endl);

    if (dict.size() == 1) {
        if ((wrong > bestwrong) ||
                (wrong == bestwrong && dict[0].index <  bestindex)) {
            bestwrong = wrong;
            bestindex = dict[0].index;
            for (int i = 0; i < d; i++) D(cerr << "  ");
            D(cerr << "-found " << dict[0] << " with " << bestwrong << " wrong, idx " << bestindex << endl);
        }
        return;
    }

    map<string, vector<entry> > cases;

    vector<bool> occurs(26);

    for (int i = 0; i < dict.size(); i++) {
        for (int j = 0; j < dict[i].word.length(); j++) {
            int c = dict[i].word[j] - 'a';
            occurs[c] = true;
        }
    }

    while (!occurs[seq[pos]-'a']) {
        pos++;
    }

    int c = seq[pos] - 'a';
    bitmask |= (1<<c);
    for (int i = 0; i < d; i++) D(cerr << "  ");
    D(cerr << "bitmask=" << hex << bitmask << dec << endl);

    for (int i = 0; i < dict.size(); i++) {
        string w = dict[i].word;
        for (int j = 0; j < w.length(); j++) {
            if ((bitmask & (1<<(w[j]-'a'))) == 0) w[j] = '#';
        }
        cases[w].push_back(dict[i]);
    }

    for (map<string, vector<entry> >::iterator it = cases.begin();
            it != cases.end(); it++) {
        const string& w = it->first;
        const vector<entry>& entries = it->second;

        bool guessedwrong = true;
        for (int j = 0; j < w.length(); j++) {
            if (w[j] == seq[pos]) guessedwrong = false;
        }
        for (int i = 0; i < d; i++) D(cerr << "  ");
        D(cerr << "-guessed " << (guessedwrong?"wrong":"right") << " on " << seq[pos] << " in " << w << endl);
        findbest(entries, seq, guessedwrong ? (wrong+1) : wrong,
                pos+1, bitmask, bestwrong, bestindex, d+1);
    }

}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int N,M;
        cin >> N >> M;

        vector<entry> dict(N);
        map<int, vector<entry> > bylength;
        for (int i = 0; i < N; i++) {
            cin >> dict[i].word;
            dict[i].index = i;
            bylength[dict[i].word.length()].push_back(dict[i]);
        }

        vector<string> results;
        for (int i = 0; i < M; i++) {
            string seq;
            cin >> seq;

            int bestwrong = 0, bestindex = 0;
            for (map<int, vector<entry> >::iterator it = bylength.begin();
                    it != bylength.end(); it++) {
                findbest(it->second, seq, 0, 0, 0, bestwrong, bestindex, 0);
            }

            if (bestindex == -1) {
                cerr << "ERROR" << endl;
                return 1;
            }
            results.push_back(dict[bestindex].word);
        }

        cout << "Case #" << testCase << ":";
        for (int i = 0; i < M; i++) {
            cout << " " << results[i];
        }
        cout << endl;
    }
}

