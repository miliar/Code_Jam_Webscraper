#include <iostream>
#include <vector>
#include <algorithm>
#define MAX_INT 2000000000
using namespace std;

struct node {
    int op;
    bool ischange;
    int value;
    bool ischild;
    node(int op, bool ischange) {
        this->op = op;
        this->ischange = ischange;   
        this->ischild = false;
    }
    node(int value) {
        this->value = value;  
        this->ischild=true; 
    }

};

int needToBe(vector<node>& tree, int n, int value) {
    if (tree[n].ischild) return (tree[n].value != value)?-1:0;
    int mi = MAX_INT;
    int tmp1, tmp2;

    int bias = 0;
    int op = tree[n].op;
    
    if ((op == 1 && value==1) || (op !=1 && value==0)) {
        tmp1 = needToBe(tree, n*2, value);
        tmp2 = needToBe(tree, n*2+1, value);
        if (tmp1 != -1 && tmp2 != -1)
            mi = min(mi, tmp1+tmp2+bias);
    } 
    
    if ((op == 1 && value==0) || (op!=1 && value==1)){
        tmp1 = needToBe(tree, n*2, value);
        tmp2 = needToBe(tree, n*2+1, value);
        if (tmp1 != -1) 
            mi = min(mi, tmp1+bias);
        if (tmp2 != -1)
            mi = min(mi, tmp2+bias);
    }
    
    if (tree[n].ischange) {
        op = (op==1?0:1);
        bias = 1;
        if ((op == 1 && value==1) || (op !=1 && value==0)) {
            tmp1 = needToBe(tree, n*2, value);
            tmp2 = needToBe(tree, n*2+1, value);
            if (tmp1 != -1 && tmp2 != -1)
                mi = min(mi, tmp1+tmp2+bias);
        } 
        
        if ((op == 1 && value==0) || (op!=1 && value==1)){
            tmp1 = needToBe(tree, n*2, value);
            tmp2 = needToBe(tree, n*2+1, value);
            if (tmp1 != -1) 
                mi = min(mi, tmp1+bias);
            if (tmp2 != -1)
                mi = min(mi, tmp2+bias);
        }
      
    }


    if (mi == MAX_INT) mi = -1;
        
    return mi;   
}

int main() {
    int T;
    cin >> T;
    for(int t=0; t<T; t++) {
        int M, V;
        cin >> M >> V;
        vector<node> tree;
        tree.push_back(node(V));
        int t1, t2;
        for(int i=0; i < (M-1)/2; i++) {
            cin >> t1 >> t2;
            tree.push_back(node(t1, t2==1));
        }
        for(int i=0; i< (M+1)/2; i++) {
            cin >> t1;
            tree.push_back(node(t1));   
        }
        int minc = needToBe(tree, 1, V);
        if (minc != -1) 
            cout << "Case #" << t+1 << ": " << minc << endl;
        else
            cout << "Case #" << t+1 << ": IMPOSSIBLE"<< endl;
    }
}
