#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define SZ(A) (int)(A).size()
#define vi vector<int>
#define pb push_back
#define ll long long
#define ERRO 1e-12
#define DEQ(X,Y) ( fabs((X) - (Y)) < ERRO)

struct node {
    double p;
    char feat[15];
    bool leaf;
    node * l, * r;
};

char buff[10000];
char decision[10000000];
node * head;
int lines;

int pos;

node * readtree()
{
    int inc = pos;
    double p;
    char feat[20];
    node * tmp;
    while(decision[inc] == ' ' || decision[inc] == '(') inc++; if(!(decision[inc] >= '0' && decision[inc] <= '9')) inc--;
    sscanf(decision + inc, "%lf", &p);
    while((decision[inc] >= '0' && decision[inc] <= '9') || decision[inc] == '.') inc++;
    while(decision[inc] == ' ') inc++;
    if(decision[inc] == ')'){
        pos = inc + 1;
        tmp = new node();
        tmp->l = tmp->r = NULL;
        tmp->p = p;
        tmp->leaf = true;
    } else {
        sscanf(decision + inc, "%s", feat); inc++;
        while(decision[inc] >= 'a' && decision[inc] <= 'z' ) inc++;
        while(decision[inc] == ' ') inc++;
        pos = inc + 1;
        tmp = new node();
        tmp->l = tmp->r = NULL;
        tmp->feat[0] = '\0';
        tmp->p = p;
        tmp->leaf = false;
        for(int i = 0; feat[i] != ' ' && feat[i] != '\0'; i++){
            tmp->feat[i] = feat[i];
            tmp->feat[i + 1] = '\0';
        }
        tmp->l = readtree();
        inc = pos;
        tmp->r = readtree();
        inc = pos;
        while(decision[pos] != ')') pos++; if(decision[pos] == ')')pos++;
        
    }
    return tmp;
}

void print(node * h)
{
    if(h == NULL) return;
    printf("leaf: %d feat %s prob %lf\n", h->leaf, h->feat, h->p);
    print(h->l);
    print(h->r);
}

int nf;
char feats[110][15];

double cuteness(node * h)
{
    if(h->leaf) return h->p;

    FOR(i, 0, nf){
        //printf("Testando feat %d %s\n", i, feats[i]);
        if(strcmp(feats[i], h->feat) == 0){
            //printf("possui %s\n", h->feat);
            return (cuteness(h->l) * h->p);
        }
    }
    //printf("n possui %s\n", h->feat);
    return (cuteness(h->r) * h->p);
}

int main()
{
    int t, animals;
    scanf("%d", &t);
    FOR(test, 0, t){
        int counter = 0;
        scanf("%d", &lines); getchar();
        FOR(i, 0, lines){
            fgets(buff, 100, stdin);
            for(int j = 0; buff[j] != '\0' && buff[j] != '\n'; j++){
                if(buff[j] == '(' || buff[j] == ')') decision[counter++] = ' ';
                decision[counter++] = buff[j];
            }
        }
        decision[counter] = '\0';
        //FOR(i, 0, 100) printf("%d", i%10); printf("\n");

        pos = 1;
        head = NULL;
        //printf("READTREE\n");
        head = readtree();
        //printf("READTREE BACK\n");

        //printf("Imprimindo\n");
        //print(head);
       
        printf("Case #%d:\n", test + 1);
        scanf("%d", &animals);
        char ani[500];
        FOR(i, 0, animals){
            scanf("%s %d", ani, &nf);
            FOR(j, 0, nf) scanf("%s", feats[j]);
            //printf("animal: %s ", ani);
            printf("%lf\n", cuteness(head));
        }
    }
    return 0;
}

