#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <utility>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; i++)

struct node {
    double val;
    double accval;
    bool has_child;
    string feature;
    node *true_node, *false_node;
};

node root;

int skip(string in, int start) {
    int i = start;
    while (isspace(in[i])) i++;
    return i;
}

int skipNum(string in, int start) {
    int i = start;
    while (isdigit(in[i]) || in[i] == '.') i++;
    return i;
}

int parse(string in, node &a, int pos) {
    pos = skip(in, pos);
    //cout << in[pos] << endl;
    pos++;
    pos = skip(in, pos);
    a.val = atof(in.c_str()+pos);
    pos = skipNum(in, pos);
    pos = skip(in, pos);
    if (in[pos] == ')') {
        a.has_child = false;
        //cout << pos << endl;
        //cout << "leaf with val:" << a.val << endl;
        return pos+1;
    } else {
        while (isalpha(in[pos])) {
            a.feature += in[pos++];
        }
        //cout << pos << endl;
        //cout << "feature: " << a.feature << " with val:" << a.val << endl;
        a.has_child = true;
        pos = skip(in, pos);
        node *tn = new node();
        pos = parse(in, *tn, pos);
        pos = skip(in, pos);
        node *fn = new node();
        pos = parse(in, *fn, pos);
        pos = skip(in, pos);
        //cout << in[pos] << endl;
        a.true_node = tn;
        a.false_node = fn;
        return pos+1;
    }
}

void calc(node *cur, double accp) {
    cur->accval = accp * cur->val;
    if (cur->has_child) {
        calc(cur->true_node, cur->accval);
        calc(cur->false_node, cur->accval);
    }
}

double rec(node *cur, vector<string> &fs) {
    if (cur->has_child) {
        if (binary_search(fs.begin(), fs.end(), cur->feature)) {
            //cout << "has feature: " << cur->feature << endl;
            return rec(cur->true_node, fs);
        } else {
            //cout << "doesn't have feature: " << cur->feature << endl;
            return rec(cur->false_node, fs);
        }
    } else {
        return cur->accval;
    }
}


int main() {
    int n, m;
    cin >> n;
    rep(I,n) {
        root.val = 0;
        root.feature = "";
        cout << "Case #" << I+1 << ":" << endl;
        cin >> m;
        string in, tmp;
        getline(cin, tmp); // trash
        rep(i,m) {
            getline(cin, tmp);
            in += tmp;
        }
        //cout << in << endl;
        parse(in, root, 0);
        calc(&root, 1.0);
        cin >> m;
        rep(i,m) {
            string name;
            int feat;
            vector<string> fs;
            cin >> name >> feat;
            rep(j,feat) {
                string tmp;
                cin >> tmp;
                fs.push_back(tmp);
            }
            sort(fs.begin(), fs.end());
            printf("%.7f\n", rec(&root, fs));
        }
    }
    return 0;
}