#include <iostream>
#include <cstdio>

using namespace std;

class Node {
public:
    Node* children;
    Node* next;
    string name;

    Node() {
        name = "";
        children = 0;
        next = 0;
    }
};

int T;
int n, m;
int ans;

Node *root;

string getDir(string& path) {
    int ind = path.find('/');
    string res;
    if(ind == string::npos) {
        res = path;
        path = "";
    }
    else {
        res = path.substr(0, ind);
        path = path.substr(ind+1);
    }
    return res;
}

int create(Node *cur, string path) {
    if(path.size() == 0) {
        return 0;
    }
    
    string dir = getDir(path);
    Node *p = cur->children;
    while(p != 0) {
        if(p->name == dir) {
            break;
        }
        p = p->next;
    }
    if(p == 0) {
        Node *c = new Node();
        c->name = dir;
        c->next = cur->children;
        
        cur->children = c;

        return create(c, path) + 1;
    }
    else {
        return create(p, path);
    }
}

int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        root = new Node();
        
        cin >> n >> m;
        
        for(int i = 0; i < n; i++) {
            string line;
            cin >> line;
            line = line.substr(1);
            
            create(root, line);
        }

        ans = 0;
        
        for(int i = 0; i < m; i++) {
            string line;
            cin >> line;
            line = line.substr(1);
            
            ans += create(root, line);
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
