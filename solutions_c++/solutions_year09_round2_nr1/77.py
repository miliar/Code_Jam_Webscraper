#include <cstdio>
#include <cstring>
#include <map>
#include <string>
using namespace std;

const int MAXL  =   8000+10;
const int MAXA  =   100+5;
const int MAXN  =   100+5;

struct Animal{
    int fearCnt;
    int fear[MAXN];
}anim[MAXA];

struct Node{
    int chren[2];
    double w;
    int fear;
}nodes[MAXL*3];
int nodeCnt;

char str[MAXL];
map<string, int> fearmap;
int fearCnt;

int l,a;

int getNum(char name[]){
    if(fearmap.count(name) == 0){
        return fearmap[name] = ++fearCnt;
    }else
        return fearmap[name];
}

void readin(){
    char line[100];

    fearmap.clear();
    fearCnt = -1;
    str[0] = '\0';

    scanf("%d", &l);
    fgets(line, sizeof(line), stdin);
    for(int i=0; i<l; ++i){
        fgets(line, sizeof(line), stdin);
        strcat(str, line);
    }
    scanf("%d", &a);
    for(int i=0; i<a; ++i){
        scanf("%s", line);
        int n;
        scanf("%d", &n);
        anim[i].fearCnt = 0;
        for(int j=0; j<n; ++j){
            scanf("%s", line);
            anim[i].fear[anim[i].fearCnt++] = getNum(line);
        }
    }
}

void buildTree(int node, char* tree){
    char str[100];

    while(*tree == ' ')++tree;

    sscanf(tree, "(%lf%s", &(nodes[node].w), str);
    nodes[node].fear = getNum(str);

    nodes[node].chren[0] = nodes[node].chren[1] = -1;

    int in = 0, ch = 0;
    for(int i=0; tree[i] != '\0'; ++i){
        if(tree[i] == '('){
            ++in;
            if(in == 2){
                nodes[node].chren[ch] = ++nodeCnt;
                buildTree(nodeCnt, tree + i);
                ++ch;
            }
        }else if(tree[i] == ')'){
            --in;
            if(in == 0)break;
        }
    }
}

double find(int node, int ani, double v){
    v *= nodes[node].w;
    if(nodes[node].chren[0] == -1)
        return v;
    for(int i=0; i<anim[ani].fearCnt; ++i)
        if(nodes[node].fear == anim[ani].fear[i])
            return find(nodes[node].chren[0], ani, v);
    return find(nodes[node].chren[1], ani, v);
}

void solve(){
    nodeCnt = 0;
    buildTree(0, str);
    for(int i=0; i<a; ++i){
        printf("%.7lf\n", find(0, i, 1.0));
    }
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        readin();
        printf("Case #%d:\n", i);
        solve();
    }
}
