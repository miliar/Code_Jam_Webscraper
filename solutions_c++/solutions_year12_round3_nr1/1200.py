#include <iostream>

#include <cstdio>
#include <cstring>

#include "stdio.h"

#include "math.h"
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

#include <iomanip>


using namespace std;


//-----------------------------graph template ------------------------------//
#define MAXV 1004 
#define MAXDEGREE 20 

typedef struct {
    int edges[MAXV+1][MAXDEGREE];
    int degree[MAXV+1]; //outdegree of each vertex
    int nVertices;
    int nEdges;
} Graph;

Graph graph;

void initializeGraph(Graph *g) {
    g->nVertices = 0;
    g->nEdges = 0;

    for(int i=1; i<=MAXV; i++) g->degree[i] = 0;
}

void insertEdge(Graph *g, int x, int y, bool directed) {//insert x->y
    if(g->degree[x] > MAXDEGREE)
        printf("Warning: insertion(%d, %d) excees max degree\n", x, y);

    g->edges[x][g->degree[x]] = y;
    g->degree[x] ++;

    if(false == directed)
        insertEdge(g,y,x,true);
    else
        g->nEdges ++;
}

//might need to be customized
void readGraph(Graph *g, int nVertex, bool directed) {
    int M, y;// edge (x,y)

    initializeGraph(g);
    g->nVertices = nVertex;
    for(int i=1; i<=nVertex; i++) {
        scanf("%d", &M);
        for(int j=1; j<=M; j++) {
            scanf("%d", &y);
            insertEdge(g,i,y,directed);
        }
    }
}

void printGraph(Graph *g) {
    for(int i=1; i<=g->nVertices; i++) {
        printf("Node %d: ", i);
        for(int j=0; j<g->degree[i]; j++)
            printf(" %d", g->edges[i][j]);
        printf("\n");
    }
}
//-----------------------------graph template ------------------------------//

int visited[MAXV];
int nPath;
void dfs(Graph *g, int start, int end) {
    if(start == end) {
       nPath ++; 
       return ;
    }
    
    visited[start]  = 1;
    for(int i=0; i<g->degree[start]; i++) {
        int w = g->edges[start][i];
        if(!visited[w]) {
            dfs(g, w, end);     
        }
    }
}

int main(void) {
    int T;
    int N;
    //2. read input
    scanf("%d", &T);    
    for(int c=1; c<=T; c++) {
        scanf("%d", &N);
        readGraph(&graph, N, true); 

        int isDiomemd = 0;
        for(int start = 1; start<=N; start++) {
            if(isDiomemd) break;

            if(1 == graph.degree[start])
                continue;

            for(int end = 1; end<=N; end++) {
                memset(visited, 0, MAXV*sizeof(int));
                nPath = 0;
                dfs(&graph, start, end);
                if(nPath>1)
                {
                    isDiomemd = 1;
                    break;
                }
            }
        }
        if(isDiomemd)
            printf("Case #%d: Yes\n",c);
        else 
            printf("Case #%d: No\n",c);
    }
    return 0;

}
