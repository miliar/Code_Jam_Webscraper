#include <stdio.h>
#include <map>
#include <queue>
#include <iostream>
#define FOR(q,n) for(int q=0; q<n; q++)

using namespace std;
class Node;

class Node {
    public: map<string, Node*> subdirectories;
};

int totalcnt;

void AddToTree(queue<string> &data, Node* root){
    if (data.empty()) return;

    string s = data.front(); data.pop();
    if (root->subdirectories.find(s)==root->subdirectories.end()) {
//        printf("creating node for %s\n", s.c_str());
        root->subdirectories[s]=new Node();
        totalcnt++;
    }
    AddToTree(data, root->subdirectories[s]);
}

static queue<string> tmpq;

queue<string>& tokenize(string s) {
    string tmp;
    unsigned int pos=1;
    while (pos!=s.size()) {
        if (s[pos]=='/') {
            pos++;
            tmpq.push(tmp);
            tmp="";
        }
        tmp+=s[pos++];
    }
    tmpq.push(tmp);

    return tmpq;
}



void solve(int _case) {
    Node *root = new Node();
    int n,m;
    scanf("%d %d",&n,&m);
    FOR(q,n) {
        string s;
        cin >> s;
        AddToTree(tokenize(s),root);
    }
    totalcnt =0;
    FOR(q,m) {
        string s;
        cin >> s;    
        AddToTree(tokenize(s),root);
    }
    printf("Case #%d: %d\n",_case,totalcnt);
}


int main() {
    int t;
    scanf("%d", &t);
    FOR(q,t) solve(q+1);


}
