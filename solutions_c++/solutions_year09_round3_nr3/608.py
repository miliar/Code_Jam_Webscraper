#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;
int cases = 1;
int number;
int quantity;
int melhor;
int released[10500];
vector<int> adj[10500];

struct Node{
    int actual;
    int soFar;
    int qtd;
    set<int> marked;
    Node(int actual = 0, int soFar = 0, int qtd = 0, set<int> m = 0):actual(actual), soFar(soFar), qtd(qtd){
        for(set<int>::iterator it = m.begin(); it != m.end(); it++)marked.insert(*it);
    }
    bool operator < (const Node &n) const{
        return soFar < n.soFar || (soFar == n.soFar && qtd > n.qtd);
    }
};
queue<Node> bfs;
int read(){
    scanf("%d%d", &number, &quantity);
    for(int i = 0; i < quantity; i++)scanf("%d", &released[i]);
    for(int i = 0; i < quantity; i++){
        adj[released[i]].clear();
        for(int j = 0; j < quantity; j++){
            if(i==j)continue;
            adj[released[i]].push_back(released[j]);
        }
    }
    return 1;
}
void busca(int primeiro){
    while(!bfs.empty())bfs.pop();
    Node p(primeiro,0,0, set<int>());
    p.marked.insert(0);
    p.marked.insert(number+1);
    
    bfs.push(p);
    
    while(!bfs.empty()){
        Node temp = bfs.front();
//        printf("&& %d %d %d\n", temp.actual, temp.qtd, temp.soFar);
        bfs.pop();

        temp.qtd++;
        
        if(temp.marked.find(temp.actual) != temp.marked.end())continue;
        set<int>::iterator it, it1, it2;
        temp.marked.insert(temp.actual);
        it1 = temp.marked.find(temp.actual);
        it2 = temp.marked.find(temp.actual);
        it1--;
        it2++;
//        printf("() %d %d\n", *it1, *it2);
        temp.soFar += (*it2) - (*it1) - 2;
        if(temp.qtd == quantity && melhor > temp.soFar){
            melhor = temp.soFar;
//            printf("entrou aqui0\n");
            continue;
        }
        for(int i = 0; i < adj[temp.actual].size(); i++){
            Node ins(adj[temp.actual][i], temp.soFar, temp.qtd, temp.marked);
            bfs.push(ins);
        }
    }
}
void process(){
    melhor = 0x3f3f3f3f;
    for(int i = 0; i < quantity; i++){
        busca(released[i]);
    }
    printf("Case #%d: %d\n", cases++, melhor);
}
int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int casos;
    scanf("%d", &casos);
    while(casos-- && read())process();
    return 0;
}
