#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

struct tree {
    double w;
    string f;
    tree* lc;
    tree* rc;
};

int N;
int L;
tree* root;
int A;
string animal;
int n;
string feature[105];

char c;

tree* construct();
double findp(tree* t);
bool foundf(string f);
void deconstruct(tree* t);

int main() {
    cout.precision(7);

    cin >> N;
    for (int t = 1; t <= N; t++) {
        cout << "Case #" << t << ":" << endl;
        cin >> L;
        cin >> c;
        root = construct();

        cin >> A;
        for (int a = 0; a < A; a++) {
            cin >> animal;
            cin >> n;
            for (int i = 0; i < n; i++)
                cin >> feature[i];
            cout << fixed << findp(root) << endl;
        }
        
        deconstruct(root);
    }

    return 0;
}

tree* construct() {
    tree* t = new tree;
    cin >> t->w;
    t->f = "";
    cin >> c;
    if (c == ')') {
        t->lc = t->rc = NULL;
        return t;
    }

    while (c != '(') {
        t->f += c;
        cin >> c;
    }
    t->lc = construct();
    cin >> c;
    t->rc = construct();
    cin >> c;
    return t;
}

double findp(tree* t) {
    if (t->f == "")
        return t->w;
    if (foundf(t->f))
        return t->w * findp(t->lc);
    else
        return t->w * findp(t->rc);
}

bool foundf(string f) {
    for (int i = 0; i < n; i++)
        if (feature[i] == f)
            return true;
    return false;
}

void deconstruct(tree* t) {
    if (t == NULL)
        return;
    deconstruct(t->lc);
    deconstruct(t->rc);
    delete t;
}
