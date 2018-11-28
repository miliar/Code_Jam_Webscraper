#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>

using namespace std;

typedef struct node {
    double w;
    string feature;
    struct node *child1;
    struct node *child2;
} node;

void read_tree(node &n){
    char c;
    double w;
    string feat;

    do {
        cin >> c;
    } while (c != '(');

    cin >> w;
    n.w = w;

    do {
        cin >> c;
    } while (c == '\n' || c == ' ');

    if (c != ')'){
        cin.putback(c);
        cin >> feat;
        n.feature = feat;
    }else{
        n.feature = "";
        n.child1 = 0;
        n.child2 = 0;
        return;
    }

    n.child1 = new node;
    n.child2 = new node;

    read_tree(*n.child1);
    read_tree(*n.child2);

    do {
        cin >> c;
    } while (c != ')');
}

double visit(node &n, int n_features, string features[], double p){
    //cerr << "visiting " << &n << endl;
    if (n.feature == "")
        return p * n.w;
    else {
        for (int i = 0; i < n_features; i++)
            if (features[i] == n.feature)
                return visit(*n.child1, n_features, features, p * n.w);
        return visit(*n.child2, n_features, features, p * n.w);
    }
}

int main(){
    int n_cases;
    cin >> n_cases;

    for(int n_case = 1; n_case <= n_cases; n_case++){
        int L;
        cin >> L;

        node root;
        read_tree(root);

        int A;
        cin >> A;

        cout << "Case #" << n_case << ":" << endl;

        cerr << A << endl;


        for (int i = 0; i < A; i++){
            string name;
            string features[128];
            cin >> name;
            int n;
            cin >> n;
            for (int k = 0; k < n; k++)
                cin >> features[k];

            cout << visit(root, n, features, 1.0) << endl;
        }

    }

    return 0;
}
