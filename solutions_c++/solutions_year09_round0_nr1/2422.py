#include <iostream>
#include <fstream>

using namespace std;

struct letters {
    char *c;
    int lgth;
    letters* next;
};

struct word {
    letters* first;
    int lgth;
};

int main() {
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int l, d, n;
    fin >> l >> d >> n;
    string temp, *dict = new string [d];
    for (int i = 0; i < d; i++) {
        fin >> temp;
        dict[i] = temp;
    }
    word* cases = new word [n];
    for (int i = 0; i < n; i++) {
        cases[i].lgth = 0;
        cases[i].first = NULL;
    }
    for (int i = 0; i < n; i++) {
        fin >> temp;
        for (int j = temp.length() - 1; j >= 0; j--) {
            if (temp[j] == ')') {
                for (int k = j - 1; k >= 0; k--) {
                    if (temp[k] == '(') {
                        letters* let = new letters;
                        let->c = new char [j - k - 1];
                        for (int m = k + 1; m < j; m++)
                            let->c[m - k - 1] = temp[m];
                        let->lgth = j - k - 1;
                        let->next = cases[i].first;
                        cases[i].first = let;
                        cases[i].lgth++;
                        j = k;
                        break;
                    }
                }
            }
            else {
                letters* let = new letters;
                let->c = new char [1];
                let->c[0] = temp[j];
                let->lgth = 1;
                let->next = cases[i].first;
                cases[i].first = let;
                cases[i].lgth++;
            }
        }
    }
    letters* p;
    bool* eliminate = new bool [d];
    int counter;

    for (int i = 0; i < n; i++) {
        counter = d;
        if (cases[i].lgth != l) {
            fout << "Case #" << i + 1 << ": 0\n";
            continue;
        }
        for (int j = 0; j < d; j++)
            eliminate[j] = true;
        p = cases[i].first;
        int loc = 0;
        while (p && counter) {
            for (int j = 0; j < d; j++) {
                if (!eliminate[j])
                    continue;
                int unmatch = 0;
                for (int k = 0; k < p->lgth; k++) {
                    if (dict[j][loc] == p->c[k])
                        break;
                    else
                        unmatch++;
                }
                if (unmatch == p->lgth) {
                    eliminate[j] = false;
                    counter--;
                }
            }
            loc++;
            p = p->next;
        }
        fout << "Case #" << i + 1 << ": " << counter << endl;
    }
}
