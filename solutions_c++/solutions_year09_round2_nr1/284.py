#include <stdio.h>
#include <set>
#include <stdlib.h>
#include <string>

using namespace std;

string S;
int T;

typedef struct node {
        long double w;
        string feature;
        node *left,*right;
        node () {
             w = 0;
             feature = "";
             left = NULL;
             right = NULL;
        }
        ~node() {
                if (left != NULL) delete left;
                if (right != NULL) delete right;
                feature.clear();
        }
};

node *root = NULL;
int C = 0;


long double read_double() {
       string n = "";
       while (S[C] != ' ' && S[C] != ')') {
             n.push_back(S[C++]);
       }
       long double temp = (long double)strtod(n.c_str(),NULL);
       if (temp == 0.0) {
          printf("");
       }
       return temp;
}

string read_string() {
       string n = "";
       while (S[C] != ' ') {
             n.push_back(S[C++]);
       }
       return n;
}


int read_space() {
    while (S[C] == ' ' && C < S.size()) C++;
    return 0;
}

node * read_node () {

     node *ret = new node();
     read_space();
     assert(S[C] == '('); C++;
     read_space();
     ret->w = read_double();
     read_space();
     if (S[C] != ')') {
        read_space();// read ' '
        ret->feature = read_string();
        read_space();// read ' '
        ret->left = read_node();
        read_space();// read ' '        
        ret->right = read_node();
        read_space();// read ' '        
     }
     read_space();// read ' '
     assert(S[C] == ')'); C++;
     read_space();// read ' '
     return ret;
}

int read_tree() {
    char str[2000];
    int l;
    scanf("%d\n", &l);
    S = "";
    for (int i=0; i<l; i++) {
        gets(str);
        if (S == "") {
           S = str;
        } else {
          S = S+" ";
          S = S+str;
        }
    }

    if (root != NULL) delete root;

    root = read_node();
}

set<string> ss;

long double process(node * n) {
       double ttemp = 1.0;
       if (n-> left == NULL && n->right == NULL)
          return n->w;
       if (ss.find(n->feature) != ss.end()) {
          ttemp = process(n->left);
       } else {
         ttemp = process(n->right);
       }
       return n->w * ttemp;
}

int solve () {
    int N;
    scanf("%d\n", &N);
    ss.clear();
    char str[1000];
    for (int i=0; i<N; i++) {
        scanf("%s", str);
        int M;
        scanf("%d", &M);
        ss.clear();
        for (int j=0; j<M; j++) {
            scanf("%s",str);
            string ff = str;
            ss.insert(ff);
        }

        printf("%.7llf\n",process(root));
    }
    return 0;
}



int main () {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    scanf("%d\n",&T);
    for (int i=1; i<=T; i++) {
        S.clear();
        C = 0;
        
        read_tree();
        printf("Case #%d:\n",i);
        solve();
    }
    return 0;
}
