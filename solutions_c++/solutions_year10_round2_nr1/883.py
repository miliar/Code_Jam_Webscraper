#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

struct Node {
    map<string, Node*> childs;
};

Node *root = 0;

void clear(Node *&ptr) {
    if (ptr == 0) return;
    map<string,Node*>::iterator first, last, iter;
    first = ptr->childs.begin();
    last = ptr->childs.end();
    for (iter = first; iter != last; iter++)
        clear(iter->second);
    delete ptr;
    ptr = 0;
}

int mkdir(vector<string> path) {
    int res = 0;
    Node *ptr = root;
    for (int i = 0; i < path.size(); i++) {
        string name = path[i];
        Node *&child = ptr->childs[name];
        if (child == 0) {
            ++res;
            child = new Node();
        }
        ptr = child;
    }
    return res;
}

int makeDirs(int n) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        string line; cin >> line;
        vector<string> path;
        istringstream in(line);
        in.ignore();
        string dir;
        while (getline(in, dir, '/')) {
            path.push_back(dir);
        }
        res += mkdir(path);
    }
    return res;
}

int main() {
    int T; cin >> T;
    for (int c = 1; c <= T; c++) {
        int N, M; cin >> N >> M;
        clear(root);
        root = new Node();
        makeDirs(N);
        int res = makeDirs(M);
        cout << "Case #" << c << ": " << res << '\n';
    }
    return 0;
}
