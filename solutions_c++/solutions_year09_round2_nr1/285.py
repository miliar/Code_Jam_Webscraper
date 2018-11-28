#include <iostream>
#include <string>
#include <map>

using namespace std;

struct node {
    double value;
    bool has;
    string ime;
    node *yes, *no;
};

map<string, bool> lastnosti;

void beri(node *root) {
    char znak;

    cin >> znak;
    if (znak != '(') { cout << "ERROR!!!\n" << znak << endl; return; };

    cin >> root->value;
    root->has = 0;

    cin >> znak;
    ungetc(znak, stdin);

    if (znak != ')') {

        cin >> root->ime;

        root->has = 1;

        root->yes = new node;
        beri(root->yes);

        root->no = new node;
        beri(root->no);

    }

    cin >> znak;
    if (znak != ')') { cout << "ERROR!!!\n" << znak << endl; return; };

}

void solve(node *root, double p) {
    if (!root->has) {
        printf("%0.8lf\n", p * root->value);
        return;
    }
    if (lastnosti[root->ime])
        solve(root->yes, p * root->value);
    else
        solve(root->no, p * root->value);
}

string niz;

int main() {

    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {

        int L;
        cin >> L;

        node *drevo = new node;
        beri(drevo);

        cout << "Case #" << t + 1 << ":\n";

        int A;
        cin >> A;
        for (int a = 0; a < A; a++) {
            cin >> niz;
            int N;
            cin >> N;
            for (int n = 0; n < N; n++) {
                cin >> niz;
                lastnosti[niz] = 1;
            }
            solve(drevo, 1);
            lastnosti.clear();
        }

    }

}
