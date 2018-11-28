#include <string>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

FILE *in = fopen("input.txt","rt");
FILE *out = fopen("output.txt","wt");

char tree_str[100000];
char fea[100][100];
int n;

struct _tree {
    int left, right;
    char name[20];
    double p;
};

vector<_tree> tree;

int make_tree(int start, int end) {
    int f, s, oc=0, i;
    f = s = -1;
    _tree temp;
    if( start == 12 && end == 30 )
        start=start;
    temp.left = -1;
    for( i=start+1; i<end; i++ ) {
        if( tree_str[i] == '(' ) { 
            if(f==-1) f=i; oc++; 
        }
        if( tree_str[i] == ')' ) { 
            if(s==-1) s=i; oc--; 
        }
        if( (tree_str[i] == ')') && !oc ) {
            if( temp.left == -1 ) {
                temp.left = make_tree(f, i);
                f = s = -1;
            } else {
                temp.right = make_tree(f, i);
            }
        }
    }
    if( temp.left == -1 ) {
        char tmp[100];
        for( i=start+1; i<end; i++ ) tmp[i-start-1] = tree_str[i];
        tmp[i-start-1] = '\0';
        sscanf(tmp, "%lf", &temp.p);
    } else {
        char tmp[100];
        for( i=start+1; i<end; i++ ) {
            if( tree_str[i] == '(' ) break;
            tmp[i-start-1] = tree_str[i];
        }
        sscanf(tmp, "%lf %s", &temp.p, temp.name);
    }
    tree.push_back( temp );
    return tree.size()-1;
}

void input(){
    int i, temp, j;
    char tstr[100];
    tree.clear();
    memset( tree_str, 0, sizeof(tree_str) );
    fscanf(in,"%d\n",&temp);
    for( i=0; i<temp; i++ ) {
        fgets(tstr, 100, in);
        tstr[strlen(tstr)-1]='\0';
        strcat(tree_str,tstr);
    }
    make_tree(0, strlen(tree_str));
}

double dfs(int node) {
    double res;
    if( tree[node].left == -1 ) return tree[node].p;
    int i;
    for( i=0; i<n; i++ ) 
        if( strcmp(fea[i], tree[node].name) == 0 ) break;
    if( i < n ) {
        res = tree[node].p * dfs( tree[node].left ) ;
    } else {
        res = tree[node].p * dfs( tree[node].right ) ;
    }
    return res;
}

void process(){
    int q, i, j;
    char temp[100];
    fscanf(in,"%d",&q);
    for( i=0; i<q; i++ ) {
        fscanf(in,"%s %d",temp,&n);
        for( j=0; j<n; j++ ) fscanf(in,"%s",fea[j]);
        fprintf(out,"%.7lf\n", dfs(tree.size()-1));
    }
}

void output(){
}

int main(){
    int tcnt;
    int t;
    fscanf(in,"%d\n",&t);
    for( tcnt=1; tcnt<=t; tcnt++ ) {
        input();
        fprintf(out,"Case #%d:\n", tcnt);
        process();
        output();
    }
    return 0;
}