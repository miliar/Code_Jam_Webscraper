#include <stdio.h>
#include <string.h>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int matrix[50][50];

// 0..3 = ENWS
typedef struct Node {
    int x,y;
    int d;
    int h1x, h1y;
    int h2x, h2y;
} Node;

int dfx[]={1,0,-1,0};
int dfy[]={0,1,0,-1};

bool operator< (const Node& a, const Node& b){
    if (a.d>b.d) return true;
    if (a.d<b.d) return false;
    
    if (a.x<b.x) return true;
    if (a.x>b.x) return false;
    
    if (a.y<b.y) return true;
    if (a.y>b.y) return false;
    
    if (a.h1x<b.h1x) return true;
    if (a.h1x>b.h1x) return false;
    
    if (a.h1y<b.h1y) return true;
    if (a.h1y>b.h1y) return false;
    
    
    if (a.h2x<b.h2x) return true;
    if (a.h2x>b.h2x) return false;
    
    if (a.h2y<b.h2y) return true;
    return false;
}
struct compare {
    bool operator() (const Node& a, const Node& b){
        if (a.x<b.x) return true;
        if (a.x>b.x) return false;
        
        if (a.y<b.y) return true;
        if (a.y>b.y) return false;
        
        if (a.h1x<b.h1x) return true;
        if (a.h1x>b.h1x) return false;
        
        if (a.h1y<b.h1y) return true;
        if (a.h1y>b.h1y) return false;
        
        
        if (a.h2x<b.h2x) return true;
        if (a.h2x>b.h2x) return false;
        
        if (a.h2y<b.h2y) return true;
        return false;
    }
};



char buffer[1000];

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int n,m;
        scanf("%d%d", &n,&m);
        memset(matrix,0,sizeof(matrix));
        for (int i=0;i<=n+1;i++)
        for (int j=0;j<=m+1;j++)
            {
                matrix[i][j]=1;
            }
            
        int sx,sy;
        int tx,ty;
        
        for (int i=1;i<=n;i++){
            scanf("%s", buffer);
            for (int j=1;j<=m;j++){
                if (buffer[j-1]=='#'){
                    matrix[i][j]=1;
                } else if (buffer[j-1]=='O'){
                    sx=i;sy=j;
                    matrix[i][j]=0;
                } else if (buffer[j-1]=='X'){
                    tx=i;ty=j;                
                    matrix[i][j]=0;
                } else {
                    matrix[i][j]=0;
                }
            }
        }
        
//        printf(">%d %d\n", sx,sy);
//        for (int i=0;i
        
        set<Node, compare> visited;
        priority_queue<Node> pq;
        
        int found=0;
        pq.push((Node){sx,sy,0,0,0,0,0});
        
        while (pq.size()){
            Node cur = pq.top();pq.pop();
            if (visited.find(cur)==visited.end()){
                visited.insert(cur);
               // printf("%d %d\n", cur.x, cur.y);
                
                if (cur.x==tx && cur.y==ty){
                    printf("Case #%d: %d\n", ++ttc,cur.d);            
                    found = 1;
                    break;
                }
                
                // move 
                for (int i=0;i<4;i++){
                    int nx = cur.x+dfx[i];
                    int ny = cur.y+dfy[i];
                   // printf(">%d %d\n", nx,ny);
                    if (!matrix[nx][ny]){
                        Node temp = (Node){nx,ny,cur.d+1,cur.h1x,cur.h1y,cur.h2x,cur.h2y};
                        if (visited.find(temp)==visited.end()){
                            pq.push(temp);
                        }
                    }
                }
                // teleport
                if (cur.x == cur.h1x && cur.y == cur.h1y && !matrix[cur.h1x][cur.h1y] && !matrix[cur.h2x][cur.h2y]){
                    Node temp = (Node){cur.h2x,cur.h2y,cur.d+1,cur.h1x,cur.h1y,cur.h2x,cur.h2y};
                    if (visited.find(temp)==visited.end()){
                        pq.push(temp);
                    }
                }
                // shoot 1
                for (int i=0;i<4;i++){
                    int nx = cur.x;
                    int ny = cur.y;
                    while (!matrix[nx+dfx[i]][ny+dfy[i]]){
                        nx+=dfx[i]; ny+=dfy[i];
                    }
                    Node temp = (Node){cur.x,cur.y,cur.d,nx,ny,cur.h2x,cur.h2y};
                    if (visited.find(temp)==visited.end()){
                        pq.push(temp);
                    }                    
                }
                // shoot 2                
                for (int i=0;i<4;i++){
                    int nx = cur.x;
                    int ny = cur.y;
                    while (!matrix[nx+dfx[i]][ny+dfy[i]]){
                        nx+=dfx[i]; ny+=dfy[i];
                    }
                    Node temp = (Node){cur.x,cur.y,cur.d,cur.h1x,cur.h1y,nx,ny};
                    if (visited.find(temp)==visited.end()){
                        pq.push(temp);
                    }                    
                }
            }    
        }          
        if (!found){
            printf("Case #%d: THE CAKE IS A LIE\n", ++ttc);            
        }                      
    }
    
    return 0;
}
