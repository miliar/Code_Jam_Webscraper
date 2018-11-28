#include <string>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <set>
#include <cstring>
using namespace std;

ifstream in;

struct node {
    string name;
    double current;
    node *left, *right;
};

node *root;
int lll;
string total;

void read_space(int &lo) {
    while (lo < lll && total[lo] == ' ')
        ++lo;
}

#include <iostream>
double read_value(int &lo) {
    double d = 0;
    while (total[lo] != '.') {
        d = d * 10 + total[lo] - '0';
        ++lo;
    }
    ++lo;
    double p = 0.1;
    while (total[lo] >= '0' && total[lo] <= '9') {
        d += p * (total[lo] - '0');
        p /= 10;
        ++lo;
    }

    cout << d << endl;

    read_space(lo);

    return d;
}

string read_name(int &lo) {
    string s = "";

    while (total[lo] >= 'a' && total[lo] <= 'z')
        s += total[lo++];

    cout << s << endl;

    read_space(lo);

    return s;
}

node *get_rec(string &total, int &lo) {

    read_space(lo);

    node *a = new node;

    if (total[lo] == '(') {
        ++lo;
        read_space(lo);
        a->current = read_value(lo);
        a->name = read_name(lo);
        if (a->name != "") {
            a->left = get_rec(total, lo);
            a->right = get_rec(total, lo);
        } else
            a->left = a->right = NULL;
        ++lo;
    } else {
        a->current = read_value(lo);
        a->name = "";
        a->left = a->right = NULL;
    }

    read_space(lo);

    cout << a->current << " XXX ";

    return a;
}
void read_tree() {
    root = NULL;

    int L;
    char line[85];
    in >> L;
    in.ignore(1);
    total = "";
    for (int i = 0; i < L; ++i) {
        in.getline(line, 85);
        total = total + " " + string(line);
    }

    int pp = 0;
    lll = total.size();
    root = get_rec(total, pp);

}

double find_value(double p, node *root, const set <string> &f) {
    p *= root->current;
    if (root->left == NULL)
        return p;
    if (f.find(root->name) != f.end())
        return find_value(p, root->left, f);
    else
        return find_value(p, root->right, f);
}


int main(int argc, char **argv) {

    in.open(argv[1]);
    ofstream out(argv[2]);

    int T;
    in >> T;
    out << setprecision(6);
    for (int i = 1; i <= T; ++i) {
        out << "Case #" << i << ":\n";
        read_tree();
        int animals;
        in >> animals;
        for (int j = 0; j < animals; ++j) {
            string tmp; int c;
            in >> tmp >> c;
            set <string> f;
            for (int k = 0; k < c; ++k) {
                in >> tmp;
                f.insert(tmp);
            }
            out << find_value(1, root, f) << "\n";
        }
    }

    return 0;
}
