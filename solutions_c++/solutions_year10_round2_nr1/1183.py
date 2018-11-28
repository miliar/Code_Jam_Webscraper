#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

const int MAX_LEVEL = 1000;
const int MAX_N = 150;

struct Tree {
    string data;
    Tree* next;
    vector<Tree*> childs;
    Tree(string d) : data(d), next(NULL) {};
};

void output(Tree* p) {
    if (!p)
        return;
    cout << p->data << " ";
    output(p->next);
    cout << endl;
    for (int i = 0; i < p->childs.size(); i++) {
        output(p->childs[i]);
    }
}

int main() {
    string dir;
    ifstream cin("in.txt");
    ofstream cout("outA.txt");
    int T, n, m; 
    
    cin >> T;
    for (int i = 0; i < T; i++) {
        Tree* root = new Tree("/");
        cout << "Case #" << i+1 << ": ";
        cin >> n >> m;
        for (int j = 0; j < n; j++) {
            cin >> dir;
            int k = 1;
            Tree* p = root;
            while (k < dir.size()) {
                string s = "";
                while (k < dir.size() && dir[k] != '/') {
                    s += dir[k];
                    k++;
                }
                k++;
                bool found = false;
                Tree* foundTt = NULL;
                for (int i = 0; i < p->childs.size(); i++) {
                    if ((p->childs[i])->data == s) {
                        found = true;
                        foundTt = p->childs[i];
                        break;
                    }
                }
                if (!found) {
                   // cout << "Pushed " << s << endl;
                    Tree* tt = new Tree(s);
                    p->childs.push_back(tt);
                    p = tt;
                } else {
                    p = foundTt;
                }
            }
        }
        
        //output(root);

        int cnt = 0;
        for (int j = 0; j < m; j++) {
            cin >> dir;
            int k = 1;
            Tree* p = root;
            while (k < dir.size()) {
                string s = "";
                while (k < dir.size() && dir[k] != '/') {
                    s += dir[k];
                    k++;
                }
                k++;
                bool found = false;
                Tree* foundTt = NULL;
                for (int i = 0; i < p->childs.size(); i++) {
                    if ((p->childs[i])->data == s) {
                        found = true;
                        foundTt = p->childs[i];
                        break;
                    }
                }
                if (!found) {
                    //cout << "Pushed " << s << endl;
                    Tree* tt = new Tree(s);
                    p->childs.push_back(tt);
                    p = tt;
                    cnt++;
                } else {
                    p = foundTt;
                }
            }
        }

        cout << cnt << endl;
        

       
    }

}