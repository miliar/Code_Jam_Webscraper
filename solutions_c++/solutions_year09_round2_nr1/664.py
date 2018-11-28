
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

typedef struct _node {
    string feature;
    double prob;
    struct _node *left;
    struct _node *right;
} node;

node* readnode(string fulltree, int start, int &end) {
    node *root = new node();

    int s1, s2, s3;
    s1 = s2 = s3 = -1;
    for(int i = start; i < fulltree.length(); i++) {
        if( fulltree[i] == '(' ) {
            if( s1 == -1 ) s1 = i;
            else if( s2 == -1 ){
                s2 = i;
                break;
            }
        }
        else if( fulltree[i] == ')' ) {
            s3 = i;
            break;
        }
    }

    if( s2 == -1 ) {
        root->left = NULL;
        root->right = NULL;
        root->feature = "";

        double p;
        string probstr = fulltree.substr(s1+1, s3-s1-1);
        istringstream iss(probstr, istringstream::in);
        iss >> p;
        root->prob = p;

        end = s3;
        return root;
    }

    string probfeat = fulltree.substr(s1+1, s2-s1-1);
    double p;
    istringstream iss(probfeat, istringstream::in);
    iss >> p;
    root->prob = p;
    string feature;
    iss >> feature;
    root->feature = feature;

    int firstend, secend;
    root->left = readnode(fulltree, s2, firstend);
    root->right = readnode(fulltree, firstend+1, secend);

    for(int i = secend+1; i < fulltree.length(); i++) {
        if(fulltree[i] == ')') {
            end = i;
            break;
        }
    }

    return root;
}

double findprob(node *root, vector<string> feats) {
    if( root == NULL ) return 1.0;

    string feature = root->feature;
    if( feature.length() == 0 ) return root->prob;

    int left = 0;
    for(int i = 0; i < feats.size(); i++) {
        if( feats[i] == feature ) left = 1;
    }

    double p;
    if( left ) {
        p = findprob( root->left, feats );
    }
    else {
        p = findprob( root->right, feats );
    }

    return root->prob * p;
}

void print_tree(node *root, string pre) {
    
    cout << pre << "TREE: p=" << root->prob << " feature=" << root->feature << endl;
    cout << pre << "LEFT [" << endl;
    if( root->left != NULL ) {
        print_tree(root->left, pre+'\t');
    }
    else {
        cout << pre << "NULL" << endl;
    }
    cout << pre << "]," << endl;

    cout << pre << "RIGHT [" << endl;
    if( root->right != NULL ) {
        print_tree(root->right, pre+'\t');
    }
    else {
        cout << pre << "NULL" << endl;
    }
    cout << pre << "]" << endl;
}

int main () {
    int T, C;
    cin >> T;
    for(C = 1; C <= T; C++) {
        int L;
        cin >> L;
        string fulltree;

        string foo;
        getline(cin, foo);
        for(int i = 0; i < L; i++) {
            string line;
            getline(cin, line);
            fulltree += line;
        }
        int end;
        node *root = readnode(fulltree, 0, end);
        
        //print_tree(root, "");

        int A;
        cin >> A;
        cout << "Case #" << C << ":" << endl;
        cout.precision(7);
        cout << fixed;
        for(int i = 0; i < A; i++) {
            string aname;
            int x;
            cin >> aname >> x;

            vector< string > feats;
            for(int j = 0; j < x; j++) {
                string f;
                cin >> f;
                feats.push_back(f);
            }

            double proba = findprob(root, feats);
            cout << proba << endl;
            
        }
    }
    return 0;
}

