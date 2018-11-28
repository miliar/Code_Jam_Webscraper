#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

#define MAX 26

struct node {
    node() {
        child.resize(MAX, 0);
    }

    ~node() {
        for (int i = 0; i < MAX; i++) {
            if (child[i] != 0) {
                delete child[i];
            }
        }            
    }
    
    vector<node*> child;
};

int L, D, N;

int calcFound(int iPos, vector<vector<int> >& v, node* root) {
    if (iPos == L) return 1;
    int iCnt = 0;
    for (int i = 0; i < v[iPos].size(); i++) {
        if (root->child[v[iPos][i]]) {
             iCnt += calcFound(iPos + 1, v, root->child[v[iPos][i]]);
        }
    }
    return iCnt;
}

int calcNumber(string& s, node* dicc) {
    vector<vector<int> > v(L);
    
    bool bInside = false;
    int iNow = 0;
    for (int i = 0; i < s.size(); i++) {
        if (isalpha(s[i])) {
            v[iNow].push_back(s[i] - 'a');
            if (! bInside) iNow++;
        }
        if (s[i] == '(') bInside = true;
        if (s[i] == ')') {
            bInside = false;
            iNow++;         
        }
    }
        
    return calcFound(0, v, dicc);
}

int main() {
    cin >> L >> D >> N;
    node dicc;
    while (D--) {
        string s;
        cin >> s;
        node* root = &dicc;
        for (int i = 0; i < L; i++) {
            if (root->child[s[i] -'a'] == 0) {
                root->child[s[i] -'a'] = new node;                     
            }
            root = root->child[s[i] -'a'];
        }     
    }
    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": " << calcNumber(s, &dicc) << endl;    
    }
}
