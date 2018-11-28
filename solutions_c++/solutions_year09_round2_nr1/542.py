#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

struct dec {
    string attr;
    double x;
    struct dec *left;
    struct dec *right;
};

set<string> atts;

struct dec *new_dec() {
    struct dec *foo = new struct dec;
    foo->x = 1.0;
    foo->attr = "";
    foo->left = NULL;
    foo->right = NULL;

    return foo;
}

void parse(string def, struct dec *curr) {
    cerr << "parse: " << def << endl;

    int kl;

    uint a, b;
    for (a = 0; def[a] != '('; a++) {}
    for (b = def.length()-1; def[b] != ')'; b--) {}

    uint i, j;
    for (i = a+1; i < def.length() && def[i] != '('; i++) {}
    if (i == def.length()) {
        stringstream ss(def.substr(a+1, b-a+1));
        ss >> curr->x;
        return;
    }

    string sx(def.substr(a+1, i-a+1));
    sscanf(sx.c_str(), "%lf", &curr->x);
    for (uint f = 0; f < sx.length(); f++) {
        if (isalpha(sx[f])) {
            curr->attr += sx[f];
        }
    }
    cerr << "attr: " << curr->attr << endl;
    kl = 0;
    j = i;
    while (j < def.length()) {
        if (def[j] == '(') kl++;
        if (def[j] == ')') kl--;
        if (kl == 0) break;
        j++;
    }
    curr->left = new_dec();
    parse(def.substr(i, j-i+1), curr->left);

    for (i = j; def[i] != '('; i++) {}
    kl = 0;
    j = i;
    while (j < def.length()) {
        if (def[j] == '(') kl++;
        if (def[j] == ')') kl--;
        if (kl == 0) break;
        j++;
    }
    curr->right = new_dec();
    parse(def.substr(i, j-i+1), curr->right);
}

double walk(struct dec *curr, double cute) {
    //fprintf(stderr, "walk: %lf %s\n", curr->x, curr->attr.c_str());
    cute *= curr->x;
    if (curr->attr != "") {
        if (atts.find(curr->attr) != atts.end()) {
            return walk(curr->left, cute);
        } else {
            return walk(curr->right, cute);
        }
    }
    return cute;
}

void del_dec(struct dec * curr) {
    // if (curr->left != NULL) del_dec(curr->left);
    // delete curr->left;
    // if (curr->right != NULL) del_dec(curr->left);
    // delete curr->right;
    curr = new_dec();
}

int main() {
    string line;
    int cases;
    cin >> cases;
    getline(cin, line);

    struct dec *root = new_dec();

    FOR(tcase, cases) {
        int lines;
        string def;
        cin >> lines;
        getline(cin, line);

        FOR(i, lines) {
            getline(cin, line);
            def += line;
        }

        del_dec(root);
        root->x = 1.0;
        root->attr = "";
        parse(def, root);

        int animals;
        cin >> animals;
        getline(cin, line);

        printf("Case #%d:\n", tcase+1);
        FOR(i, animals) {
            atts.clear();
            string name;
            int natt;
            cin >> name;
            cin >> natt;
            FOR(i, natt) {
                string att;
                cin >> att;
                atts.insert(atts.end(), att);
            }
            double cute = walk(root, 1.0);
            printf("%.10lf\n", cute);
        }
    }

    return 0;
}
