#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;
#define abc 300

map< string, int> table;

struct Node
{
    int i;
    Node* c[abc];
};
Node* createNode();

Node* root;
int cnt, mm, list[510];

void insert(int n) {
    Node* tmp = root;
    int i;
    for ( i = 0; i < n; i++ ) {
        if ( !tmp->c[list[i]] ) {
            tmp->c[list[i]] = createNode();
            cnt++;
        }
        tmp = tmp->c[list[i]];
    }
}

char *sep = "/";

void rinsert(char* buffer) {
    char  *token;
    string tmp;
    int a = 0;
    token = strtok(buffer,sep);
    while ( token ) {
        tmp = token;
        if ( table[tmp] == 0 )
            table[tmp] = mm++;
        token = strtok(NULL,sep);
        list[a++] = table[tmp];
    }
    insert(a);
}

void clear(Node *& tmp) {
    int i;
    for ( i = 0; i < abc; i++ ) {
        if ( tmp->c[i] ) clear(tmp->c[i]);
    }
    free(tmp);
    tmp = NULL;
}

Node* createNode() {
    Node* ret = (Node*)malloc(sizeof(Node));
    memset(ret->c,0,sizeof(ret->c));
    return ret;
}

int main()
{
    int n, m, aa, nn, i;
    char buffer[1000];
    gets(buffer);
    nn = atoi(buffer);
    for ( aa = 1;aa<= nn; ++aa ) {
        gets(buffer);
        sscanf(buffer,"%d %d",&n,&m);
        cnt = 0;
        mm = 1;
        table.clear();
        root = createNode();
        for ( i = 0; i < n; i++ ) {
            gets(buffer);
            rinsert(buffer);
        }
        cnt = 0;
        for ( i = 0; i < m; i++ ) {
            gets(buffer);
            rinsert(buffer);
        }
        printf("Case #%d: %d\n",aa,cnt);
        clear(root);
    }
    return 0;
}

