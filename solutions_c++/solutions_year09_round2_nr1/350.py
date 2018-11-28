# include <iostream>
# include <vector>
# include <cmath>
# include <string>
# include <set>
# include <algorithm>
# include <cstring>
# include <queue>
# include <stack>
# include <map>
using namespace std;

char c;

struct node
{
    double prob;
    string feature;
};

struct tree
{
    node *n;
    tree *left;
    tree *right;
};

tree* leerArbol(bool leido)
{
    tree* t;
    t=new tree;
    t->n=new node;
    t->left=NULL;
    t->right=NULL;
    double prob;
    string str="";
    bool buscar;
    if (!leido) {
        while((c=getchar())!='(');
    }
    scanf("%lf", &prob);
    while(isspace(c=getchar()));
    if (c==')') {
        t->n->prob=prob;
        t->n->feature="";
    }
    else {
        t->n->prob=prob;
        str.push_back(c);
        while(isalpha(c=getchar())) {
            str.push_back(c);
        }
        t->n->feature=str;
        if (c=='(') {
            t->left=leerArbol(true);
        }
        else {
            t->left=leerArbol(false);
        }
        t->right=leerArbol(false);
        while((c=getchar())!=')');
    }
    return t;
}

void imprimir(tree *t)
{
    if (t!=NULL) {
        cout<<t->n->prob<<" "<<t->n->feature<<"( ";
        imprimir(t->left);
        cout<<", ";
        imprimir(t->right);
        cout<<")";
    }
}

double cuteness(tree *t, vector <string> vv, int n)
{
    int i;
    if (t->n->feature.compare("")==0) {
        return t->n->prob;
    }
    for (i=0; i<n; i++) {
        if (t->n->feature.compare(vv[i])==0) {
            return t->n->prob*cuteness(t->left, vv, n);
        }
    }
    return t->n->prob*cuteness(t->right, vv, n);
}

int main()
{
    int t, tt=1, n, i, j, m;
    tree *arb;
    string str;
    vector <string> vv;
    scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        arb=leerArbol(false);
        printf("Case #%d:\n", tt++);
        scanf("%d", &n);
        for (j=0; j<n; j++) {
            vv.clear();
            cin>>str;
            scanf("%d", &m);
            for (i=0; i<m; i++) {
                cin>>str;
                vv.push_back(str);
            }
            printf("%0.7lf\n", cuteness(arb, vv, m));
        }
    }
    return 0;
}
